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
    stock = db.Column(db.Integer)

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
            "message": "Medicine not found."
        }
    ), 404

# still working on this, dont call
@app.route("/inventory/<string:name>", methods=['PUT'])
def update_medicine_inventory(name):
    try:
        medicine = Inventory.query.filter_by(name=name).first()
        if not medicine:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "id": id
                    },
                    "message": "Medicine not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['stock']:
            medicine.stock = data['stock']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": medicine.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "name": name
                },
                "message": "An error occurred while updating the medicine inventory. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)