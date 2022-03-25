from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

get_patient_info_URL = environ.get('get_patient_info_URL') or "http://localhost:5000/patient/" #+patientId GET
get_medicine_info_URL = environ.get('get_medicine_info_URL') or "http://localhost:5002/inventory/" #+name GET
update_inventory_URL = environ.get('update_inventory_URL') or "http://localhost:5002/inventory/" #+name PUT
get_pending_prescriptions_URL = environ.get('get_pending_prescriptions_URL') or "http://localhost:5001/prescription/pending" #GET
get_unsend_pending_prescriptions_URL = environ.get('get_unsend_pending_prescriptions_URL') or "http://localhost:5001/prescription/pending/no" #GET
update_prescription_URL = environ.get('update_prescription_URL') or "http://localhost:5001/prescription/" #+prescriptionId PUT
record_prescription_in_paymentMS_URL = environ.get('record_prescription_in_paymentMS_URL') or "http://localhost:5003/payment/create" #POST


# the pharmacist UI pending page should invoke this when loads and then get all the pending prescriptions
# this route completes scenario2 3) to 8)
@app.route("/processPendingPrescriptions")
def processPendingPrescriptions():
    
    # get all unsend pending prescriptions
    print('\n-----[START] Getting all unsend pending prescriptions-----')
    unsend_pending_prescriptions_result = invoke_http(get_unsend_pending_prescriptions_URL, method='GET')
    if unsend_pending_prescriptions_result["code"] == 200:
        unsend_prescriptions = unsend_pending_prescriptions_result["data"]["prescriptions"]
        # for each unsend pending prescription, calculate total price and send its info to the payment MS
        for unsend_prescription in unsend_prescriptions:
            prescription_id = unsend_prescription["id"]
            print('\n-----Dealing with prescription id = ' + str(prescription_id) + "-----")
            patient_id = unsend_prescription["patient_id"]
            medicines = unsend_prescription["medicines"]
            total = calculate_total(medicines)
            send_result = send_to_paymentMS(prescription_id,patient_id,medicines,total)
            # if send successfully to payment MS, update SendToPayment to 'yes'
            if send_result["code"] == 201:
                update_sendToPayment_to_yes_input = {"sendToPayment": "yes"}
                update_sendToPayment_URL = update_prescription_URL + str(prescription_id)
                print('[3] Updating sendToPayment to yes')
                update_sendToPayment_result = invoke_http(update_sendToPayment_URL, method='PUT', json=update_sendToPayment_to_yes_input)
                if update_sendToPayment_result["code"] == 200:
                    print("-----Prescription id = " + str(prescription_id) + " successfully sent to payment MS-----")

    # get all pending prescription
    print('\n-----Getting all pending prescriptions [END]-----')
    pending_prescriptions = invoke_http(get_pending_prescriptions_URL, method='GET')
    return pending_prescriptions

def calculate_total(medicines): # eg. medicines = {"Xanax":1, "Azithromycin":1}
    print('[1] Calculating total price')
    medicines = json.loads(medicines)
    total = 0 #assume no consulting fee and always have medicines
    for medicine, quantity in medicines.items():
        medicine_info_result = invoke_http(get_medicine_info_URL + medicine, method='GET')
        if medicine_info_result["code"] == 200:
            price = medicine_info_result["data"]["price"]
            total += float(price) * float(quantity)
    return round(total,2)

def send_to_paymentMS(prescription_id,patient_id,medicines,total):
    print('[2] Sending prescription to payment MS')
    input = {
        "prescription_id": prescription_id,
        "patient_id": patient_id,
        "medicines": medicines,
        "total": total
    }
    result = invoke_http(record_prescription_in_paymentMS_URL, method='POST', json=input)
    return result


# the pharmacist UI pending page should invoke this when the comfirm buttom is pressed for each prescription
# the UI should send to this route the confirmed presciption id using PUT in the form of {prescription_id: ...}
# this route completes scenario2 12) to 16)
@app.route("/confirmPrescription", methods=['PUT'])
def confirmPrescription():
    data = request.get_json()
    prescription_id = data["prescription_id"]
    print('\n-----[START] Confirming for prescription id = ' + str(prescription_id) + '-----')

    update_status_to_confirmed_input = {"status": "confirmed"}
    update_status_URL = update_prescription_URL + str(prescription_id)
    print('[1] Updating states to confirmed')
    update_status_result = invoke_http(update_status_URL, method='PUT', json=update_status_to_confirmed_input)
    if update_status_result["code"] == 200:

        updated_prescription = update_status_result["data"]
        medicines = updated_prescription["medicines"]
        patient_id = updated_prescription["patient_id"]
        # minus inventory upon confirmation
        update_inventory_result = update_inventory(medicines)
        if update_inventory_result == 200:
            # retrieve patient's phone number
            print('[3] Retrieving patient phone number')
            patient_info_result = invoke_http(get_patient_info_URL + patient_id, method='GET')
            if patient_info_result["code"] == 200:
                patient_hp = patient_info_result["data"]["hp"]
                #send phone number to rabbitAMQP
                Rabbit_result = send_to_Rabbit(patient_hp)
                if Rabbit_result == 200:
                    print('-----Notified patient to collect medicine at counter via SMS [END]-----')
                    return jsonify({
                        "code": 200,
                        "messsage": "Prescription id = " + str(prescription_id) + " confirmed successfully."
                    })

def update_inventory(medicines): # eg. medicines = {"Xanax":1, "Azithromycin":1}
    print('[2] Updating inventory')
    medicines = json.loads(medicines)
    updated = 0
    for medicine, quantity in medicines.items():
        input = {"used_quantity": quantity}
        result = invoke_http(update_inventory_URL + medicine, method='PUT', json=input)
        if result["code"] == 200:
            updated += 1
    if updated == len(medicines):
        return 200

def send_to_Rabbit(patient_hp): # eg. patient_hp = "91234567"
    # send hp to Rabbit, if successful, return 200
    print('[4] Sending ph to Rabbit')
    message='info: +65' + str(patient_hp)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.message", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2))
    # print('patient phone number is ' + patient_hp)
    # print("\nMessage published to RabbitMQ Exchange.\n")
    return 200
# send_to_Rabbit(98443918)


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for proessing prescriptions and medicines...")
    app.run(host="0.0.0.0", port=5100, debug=True)

