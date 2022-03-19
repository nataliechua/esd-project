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
    patient_id = db.Column(db.Integer, nullable=False)
    medicines = db.Column(db.String(255), nullable=False)
    total = db.Column(db.Float)
    order_id = db.Column(db.Integer, nullable=False)
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

@app.route("/payment/<string:status>", methods=['POST'])
def get_all_payment_by_status(status): # need status + patient_id

    data = request.get_json()

    patient_id = data["patient_id"]

    payment_details = Payment.query.filter_by(patient_id=patient_id, status=status)# assuming that sms will send payment_id at the end of the string
    if payment_details:
        return jsonify(
            {
            "code": 200,
            "data": [payment.json() for payment in payment_details]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment record not found."
        }
    ), 404

@app.route("/payment/create", methods=['POST'])
def create_payment():
    data = request.get_json()
    payment = Payment(id = None, **data, status='unpaid')

    try:
        db.session.add(payment)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the payment. " + str(e)
            }
        ), 500
    
    print(json.dumps(payment.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Payment created successfully.",
            "data": payment.json()
        }
    ), 201

@app.route("/payment/<string:id>")
def get_payment(id):
    payment_details = Payment.query.filter_by(id=id).first() # assuming that sms will send payment_id at the end of the string
    if payment_details:
        return jsonify(
            {
            "code": 200,
            "data": payment_details.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment record not found."
        }
    ), 404

@app.route("/payment/update/<string:id>", methods=['PUT']) # update payment by order_id and status
def update_payment(id):
    try:

        data = request.get_json()

        # id = data["id"]
        order_id = data["order_id"]

        payment_details = Payment.query.filter_by(id=id).first() 

        if payment_details == None:
            return jsonify(
                {
                    "code": 404,
                    "message": "Payment record not found."
                }
            )
        
        # Change payment status to paid and update order_id
        payment_details.status = "paid"
        payment_details.order_id = order_id
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "type": "error"
            }
        ), 500
    
    return jsonify(
            {
            "code": 200,
            "data": payment_details.json()
            }
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
