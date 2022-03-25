from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/patient'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/patient'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.String(15), primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    allergies = db.Column(db.String(255))
    hp = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(255))

    def __init__(self, id, name, age, allergies, hp, email):
        self.id = id
        self.name = name
        self.age = age
        self.allergies = allergies
        self.hp = hp
        self.email = email

    def json(self):
        return {"id": self.id, 
        "name": self.name, 
        "age": self.age, 
        "allergies": self.allergies, 
        "hp": self.hp, 
        "email": self.email}


@app.route("/patient/<string:id>")
def find_patient_by_id(id):
    patient = Patient.query.filter_by(id=id).first()
    if patient:
        return jsonify(
            {
                "code": 200,
                "data": patient.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Patient which id = " + id + " not found."
        }
    ), 404


@app.route("/patient/create", methods=['POST'])
def create_patient():
    data = request.get_json()
    patient = Patient(**data)

    try:
        db.session.add(patient)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the patient. " + str(e)
            }
        ), 500
    
    print(json.dumps(patient.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Patient created successfully.",
            "data": patient.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

