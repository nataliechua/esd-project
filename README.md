# esd-project

## patient MS
* GET - get specific patient info: http://localhost:5000/patient/<name>
eg. http://localhost:5000/patient/Adele

## prescription MS
* GET - get prescriptions by status: http://localhost:5001/prescription/<status>
eg.http://localhost:5001/prescription/pending
* POST - create prescription: http://localhost:5001/prescription/create
example input see postman
* PUT - update prescription status: http://localhost:5001/prescription/<id> (id is prescription id)
eg: http://localhost:5001/prescription/17
example input see postman

## inventory MS
* GET - get medicine by name: http://localhost:5002/inventory/<name>
eg.http://localhost:5002/inventory/Amlodipine
* Put - update inventory by name: http://localhost:5002/inventory/<name>
eg.http://localhost:5002/inventory/Adderall
example input see postman

## payment MS
* POST - get payment by status and patient_id: http://localhost:5003/payment/<status>
example input see postman
* POST - create payment: http://localhost:5003/payment/create
* GET - get payment: http://localhost:5003/payment/<id>
e.g. http://localhost:5003/payment/1
* PUT - update payment details:  http://localhost:5003/payment/update