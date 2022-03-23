from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment' 
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    prescription_id = db.Column(db.Integer, nullable=False)
    patient_id = db.Column(db.String(15), nullable=False)
    medicines = db.Column(db.String(65535), nullable=False)
    total = db.Column(db.Float, nullable=False)
    order_id = db.Column(db.String(255))
    status = db.Column(db.String(255), nullable=False)

    def __init__(self, id, prescription_id, patient_id, medicines, total, order_id, status):
        self.id = id
        self.prescription_id = prescription_id
        self.patient_id = patient_id
        self.medicines = medicines
        self.total = total
        self.order_id = order_id
        self.status = status

    def json(self):
        return {
            "id": self.id, 
            "prescription_id": self.prescription_id,
            "patient_id": self.patient_id,
            "medicines": self.medicines,
            "total": self.total,
            "order_id": self.order_id,
            "status": self.status
        }


@app.route("/payment")
def get_all_records():
    plist = Payment.query.all()
    if plist:
        return jsonify(
            {
            "code": 200,
            "data": {
                    "prescription records": [p.json() for p in plist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no prescription records."
        }
    ), 404


@app.route("/payment/<int:id>")
def get_prescription_by_paymentId(id):
    prescription = Payment.query.filter_by(id=id).first() # assuming that sms will send payment_id at the end of the string
    if prescription:
        return jsonify(
            {
            "code": 200,
            "data": prescription.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Prescription record payment id = " + str(id) + " not found."
        }
    ), 404


@app.route("/payment/<string:patient_id>/<string:status>")
def get_prescriptions_by_patientId_and_payment_status(patient_id, status): 
    plist = Payment.query.filter_by(patient_id=patient_id, status=status)
    if plist.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "prescriptions": [pres.json() for pres in plist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no " + status + " prescriptions for patient " + patient_id + "."
        }
    ), 404


@app.route("/payment/create", methods=['POST'])
def record_prescription():
    data = request.get_json()
    prescription = Payment(id = None, **data, order_id= None, status='unpaid')

    try:
        db.session.add(prescription)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while recording the prescription. " + str(e)
            }
        ), 500
    
    print(json.dumps(prescription.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Prescription recorded successfully.",
            "data": prescription.json()
        }
    ), 201


@app.route("/payment/<int:id>", methods=['PUT'])
def update_orderId_and_payment_status(id):
    try:
        prescription = Payment.query.filter_by(id=id).first() 
        if not prescription:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "id": id
                    },
                    "message": "Prescription record which payment id = " + str(id) + " not found."
                }
            )

        # update order_id and payment status
        data = request.get_json()
        prescription.status = "paid"
        prescription.order_id = data["order_id"]
        db.session.commit()
        return jsonify(
            {
            "code": 200,
            "data": prescription.json(),
            "message": "Payment status and order_id for prescription which payment id = " + str(id) + " updated successfully."
            }
        ), 200
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred while updating payment status and order_id for prescription payment id = " + str(id) + ". " + str(e)
            }
        ), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

