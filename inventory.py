from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/inventory' 
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def json(self):
        return {"id": self.id, 
        "name": self.name, 
        "price": self.price, 
        "stock": self.stock}


@app.route("/inventory")
def get_all_medicines():
    mlist = Inventory.query.all()
    if mlist:
        return jsonify(
            {
            "code": 200,
            "data": {
                    "medicines": [m.json() for m in mlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no medicines in inventory."
        }
    ), 404


@app.route("/inventory/<string:name>")
def find_medicine_by_name(name):
    medicine = Inventory.query.filter_by(name=name).first() #here assume no duplicated names
    if medicine:
        return jsonify(
            {
                "code": 200,
                "data": medicine.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Medicine " + name + " not found."
        }
    ), 404


@app.route("/inventory/<string:name>", methods=['PUT'])
def update_medicine_inventory(name):
    try:
        medicine = Inventory.query.filter_by(name=name).first() #here assume no duplicated names
        if not medicine:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "name": name
                    },
                    "message": "Medicine " + name + " not found."
                }
            ), 404

        # update inventory
        data = request.get_json()
        if data['used_quantity']:
            medicine.stock -= data['used_quantity']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": medicine.json(),
                    "message": "Inventory for medicine " + name + " updated successfully."
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "name": name
                },
                "message": "An error occurred while updating medicine " + name + " inventory. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

    