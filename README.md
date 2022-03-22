# esd-project

## patient MS
* GET - get specific patient info by patient id: http://localhost:5000/patient/<id>
eg. http://localhost:5000/patient/t1234567a


## inventory MS
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
* PUT - update prescription status by prescription id: http://localhost:5001/prescription/<id>
eg. http://localhost:5001/prescription/17
example input see postman


## payment MS
* GET - get specific prescription info by payment id: http://localhost:5003/payment/<id>
eg. http://localhost:5003/payment/1
* GET - get prescriptions by patient_id and payment status: http://localhost:5003/payment/<patient_id>/<status>
eg. http://localhost:5003/payment/t1234567a/paid
* POST - record prescription in payment MS: http://localhost:5003/payment/create
example input see postman
* PUT - update prescription order_id and payment status by payment id: http://localhost:5003/payment/<id>
eg. http://localhost:5003/payment/6
example input see postman

