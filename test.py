from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
import json

import mysql.connector

app = Flask(__name__)
CORS(app)

# FIRST APPROACH
# tried to use sqlalchemy to fetch data from two database but had issue

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/prescription' 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# SECOND APPROACH
# tried to use api routes to fetch data but didn't return any result

pres_URL = "http://localhost:5001/prescription/<string:status>"
inventory_URL = "http://localhost:5002/inventory/price/<string:name>"

# not related to the process required in complex microservice
# just wanted to check if the route is working in this complex microservice
@app.route("/process_prescription/<string:status>", methods=['GET'])
def process_prescription(status):
    result = invoke_http(pres_URL, method='GET', json=status)
    return result

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)

# THIRD APPROACH
# tried to fetch data through my local database

# db1=mysql.connector.connect(host="localhost", user="root", password="",database="esd_project")
# db2=mysql.connector.connect(host="localhost", user="root", password="",database="esd_project")

# cursor1=db1.cursor()
# cursor2=db2.cursor()

# cursor1.execute("SELECT name,price FROM inventory")
# cursor2.execute("SELECT id, medicines FROM prescription")

# # create a dict to store medicines with price, data retrieved from inventory
# medicine_dict = {}
# for table_name in cursor1:
#     medicine_dict[table_name[0]] = table_name[1]

# # calculate total price for each prescription
# # run this python file to check for the result in the terminal
# for table_name in cursor2:
#     json_object = json.loads(table_name[1])
#     total = 0
#     for k,v in json_object.items():
#         if k in medicine_dict:
#             total += medicine_dict[k] * v
#     print("Prescription ID " + str(table_name[0]) + ", total price: $" + str(total))


