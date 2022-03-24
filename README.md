# esd-project

## patient MS
* GET - get specific patient info by patient id: http://localhost:5000/patient/<id>
eg. http://localhost:5000/patient/t1234567a


## inventory MS
* GET - get all medicines info in inventory MS: http://localhost:5002/inventory
* GET - get specific medicine info by medicine name: http://localhost:5002/inventory/<name>
eg. http://localhost:5002/inventory/Amlodipine
* PUT - update medicine inventory by medicine name: http://localhost:5002/inventory/<name>
eg. http://localhost:5002/inventory/Adderall
example input see postman


## prescription MS
* GET - get prescriptions by status: http://localhost:5001/prescription/<status>
eg. http://localhost:5001/prescription/pending
* GET - get prescriptions by status and sendToPayment: http://localhost:5001/prescription/<status>/<sendToPayment>
eg. http://localhost:5001/prescription/pending/no
* POST - create prescription: http://localhost:5001/prescription/create
example input see postman
* PUT - update prescription status or sendToPayment by prescription id: http://localhost:5001/prescription/<id>
eg. http://localhost:5001/prescription/17
example inputs see postman


## payment MS
* GET - get all prescription records in payment MS: http://localhost:5003/payment
* GET - get specific prescription info by payment id: http://localhost:5003/payment/<id>
eg. http://localhost:5003/payment/1
* GET - get prescriptions by patient_id and payment status: http://localhost:5003/payment/<patient_id>/<status>
eg. http://localhost:5003/payment/t1234567a/paid
* POST - record prescription in payment MS: http://localhost:5003/payment/create
example input see postman
* PUT - update prescription order_id and payment status by payment id: http://localhost:5003/payment/<id>
eg. http://localhost:5003/payment/6
example input see postman


# process CMS
* GET - complete senario2 3) to 8): http://localhost:5100/processPendingPrescriptions
pharmacist UI pending page invokes this when loads and get all the pending prescriptions
* PUT - complete scenario2 12) to 16): http://localhost:5100/confirmPrescription
pharmacist UI pending page invokes this when the comfirm buttom is pressed for each prescription
sample UI input: {prescription_id: 1}

## Login MS
* Patient - id: (use any Patient's ID) (e.g. t1234567a) ; pwd: patient
* Doctor - username: doctor ; pwd: doctor
* Pharmacist - username: pharmacist ; pwd: pharmacist