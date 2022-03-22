from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/prescription' 
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Prescription(db.Model):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    patient_id = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(65535))
    medicines = db.Column(db.String(65535), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    sendToPayment = db.Column(db.String(255), nullable=False)

    def __init__(self, id, doctor_id, patient_id, description, medicines, status, sendToPayment):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.description = description
        self.medicines = medicines
        self.status = status
        self.sendToPayment = sendToPayment

    def json(self):
        return {"id": self.id, 
        "doctor_id": self.doctor_id, 
        "patient_id": self.patient_id, 
        "description": self.description, 
        "medicines": self.medicines, 
        "status": self.status,
        "sendToPayment": self.sendToPayment}


@app.route("/prescription/<string:status>")
def get_prescriptions_by_status(status):
    plist = Prescription.query.filter_by(status=status)
    if plist:
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
            "message": "There are no " + status + " prescriptions."
        }
    ), 404


@app.route("/prescription/<string:status>/<string:sendToPayment>")
def get_prescritions_by_status_and_STP(status,sendToPayment):
    plist = Prescription.query.filter_by(status=status, sendToPayment=sendToPayment)
    if plist:
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
            "message": "There are no " + status + " and sendToPayment = " + sendToPayment + " prescriptions."
        }
    ), 404


@app.route("/prescription/create", methods=['POST'])
def create_prescription():
    data = request.get_json()
    prescription = Prescription(id = None, **data, status='pending', sendToPayment='no')

    try:
        db.session.add(prescription)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the prescription. " + str(e)
            }
        ), 500
    
    print(json.dumps(prescription.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Prescription created successfully.",
            "data": prescription.json()
        }
    ), 201


@app.route("/prescription/<int:id>", methods=['PUT'])
def update_prescription_status(id):
    try:
        prescription = Prescription.query.filter_by(id=id).first()
        if not prescription:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "id": id
                    },
                    "message": "Prescription id = " + str(id) + " not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['status']:
            prescription.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": prescription.json(),
                    "message": "Status for prescription id = " + str(id) + " updated successfully."
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred while updating the prescription id = " + str(id) + ". " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

