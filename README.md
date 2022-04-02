# ESD project - Group 6
## About

## Note before run our APP
1. For Senario 2 sending the SMS to patient by Twilio, in order for patient to get the message, the patient number need to be registered inside our twilio account as a caller. Thus if you want to receive message as a patient, pls contact the team to configure it for you. Otherwise, the current Twilio will not send to you phone number.

## What you need to do to run our APP
1. start WAMP(MySQL) and docker(stop/remove the previous same-name containers before running, see useful commands below)
2. import sql database (remember to allow remote database access in order to run containers, if never did see lab 3)
3. open folder in Visual Studio Code
4. change all <dockerid> in docker-compose.yml to your own docker id
5. in twilio_message.py line 42&43, enter twillio SID and TOKEN,see secret.txt
6. put the frontend folder in www localhost to access
7. create and start containers: docker-compose up -d
8. OPTIONAL: show realtime logs of a service: docker-compose logs -f <servicename>
9. OPTIONAL: IF WANT TO SEE RabbitMQ management website
   go http://localhost:15672 
   The default username / password = guest / guest
10. you can now go through our app by front end
    OPTIONAL BUT IMPORTANT: to see all senarios, you better signup a patient info using your own phone num in order to receive msg (if hp have added in twilio account)
11. stop and remove containers: docker-compose down



### patient MS
* GET - get specific patient info by patient id: http://localhost:5000/patient/<id>
eg. http://localhost:5000/patient/t1234567a
* POST - create patient: http://localhost:5000/patient/create
sample input see postman


### inventory MS
* GET - get all medicines info in inventory MS: http://localhost:5002/inventory
* GET - get specific medicine info by medicine name: http://localhost:5002/inventory/<name>
eg. http://localhost:5002/inventory/Amlodipine
* PUT - update medicine inventory by medicine name: http://localhost:5002/inventory/<name>
eg. http://localhost:5002/inventory/Adderall
sample input see postman


### prescription MS
* GET - get prescriptions by status: http://localhost:5001/prescription/`<status>`
eg. http://localhost:5001/prescription/pending
* GET - get prescriptions by status and sendToPayment: http://localhost:5001/prescription/`<status>`/`<sendToPayment>`
eg. http://localhost:5001/prescription/pending/no
* POST - create prescription: http://localhost:5001/prescription/create
sample input see postman
* PUT - update prescription status or sendToPayment by prescription id: http://localhost:5001/prescription/`<id>`
eg. http://localhost:5001/prescription/17
sample inputs see postman


### payment MS
* GET - get all prescription records in payment MS: http://localhost:5003/payment
* GET - get specific prescription info by payment id: http://localhost:5003/payment/<id>
eg. http://localhost:5003/payment/1
* GET - get prescriptions by patient_id and payment status: http://localhost:5003/payment/`<patient_id>`/`<status>`
eg. http://localhost:5003/payment/t1234567a/paid
* POST - record prescription in payment MS: http://localhost:5003/payment/create
sample input see postman
* PUT - update prescription order_id and payment status by payment id: http://localhost:5003/payment/`<id>`
eg. http://localhost:5003/payment/6
sample input see postman


### process CMS
* GET - complete senario2 3) to 8): http://localhost:5100/processPendingPrescriptions
pharmacist UI pending page invokes this when loads and get all the pending prescriptions
* PUT - complete scenario2 12) to 16): http://localhost:5100/confirmPrescription
pharmacist UI pending page invokes this when the comfirm buttom is pressed for each prescription
sample UI input: {prescription_id: 1}


### Login System
* Patient - id: (use any Patient's ID) (e.g. t1234567a) ; pwd: patient
* Doctor - username: doctor ; pwd: doctor
the hardcoded default doctor id for now is 3 
* Pharmacist - username: pharmacist ; pwd: pharmacist

