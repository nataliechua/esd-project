# ESD project - Group 6
## About
ESDT6 Pharmacy is a pharmacy that assesses and prescribes prescription drugs based on the patient's medical conditions and distributes them to the patient at the counter. Our two staffs will be the doctor and the pharmacist. The doctor is responsible for checking the allergies of the patient and creating prescriptions in the system, while the pharmacist is responsible for preparing the prescription drugs and verifying the patient has made the payment before dispensing it to them.
- To know more about our project and different senarios, please refer to Report.
- For a big overview about our project senarios flows, please refer to ESD project flow.PNG

## Note before running our APP
1. For one part of senario 2 sending SMS to patient by Twilio to inform them about medicine collection, in order for patient to get the message, the patient's number need to be registered inside our twilio account as a caller. Thus if you want to receive SMS as a patient, please contact the team to add your number in the account. Otherwise, the current Twilio will not send the message for collection to your phone.
2. If you want to test each microservice individually by its own [API endpoints](https://drive.google.com/drive/u/1/folders/1kpU5b04oDoB0SYhtcUaB6DPn06s1nv4a) or the Postman file we provided, please replace steps 7 to 12 in the next section to the followings: <br>
    7. in terminal: python run *microservice_name*.py, eg. python run patient.py <br>
    8. real logs of each microservice can be seen in the corresponding terminal <br>
    9. OPTIONAL: IF WANT TO SEE RabbitMQ management website <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- go http://localhost:15672 <br>
    &nbsp;&nbsp;&nbsp;&nbsp;- The default username / password = guest / guest <br>
    10. use can now test each microservice's endpoints via Postman <br>
    11. if finished testing, simply delete all the terminals

## What you need to do before running our APP
1. start WAMP(MySQL) and docker(stop/remove the previous same-name containers/images before running)
2. import sql database from file create.sql (remember to allow remote database access, if never did see lab 3 page 8)
3. open current folder in Visual Studio Code
4. change all *< dockerid >* in docker-compose.yml to your own docker id
5. in twilio_message.py line 42 and 43, enter twillio SID and TOKEN, see secret.txt
6. copy the *frontend* folder to C:\wamp64\www
7. create and start containers in terminal: docker-compose up -d
8. OPTIONAL: show realtime logs of a service in terminal: docker-compose logs -f *servicename*
9. OPTIONAL: IF WANT TO SEE RabbitMQ management website
   - go http://localhost:15672 
   - The default username / password = guest / guest
10. you can now go through our app for all the senarios by accessing http://localhost/frontend/login.html
    - for information about current login system accounts to be used in our senarios, see secret.txt
    - for medicines that doctors can prescript to patients in senario 1, see medicineList.pdf
    - for information about paypal sandbox accounts you can use in senario 3, see secret.txt
12. once you finish running through our app, stop and remove containers in terminal: docker-compose down

## API endpoints
The following is a brief summary for our API endpoints. For detailed infomation, pls visit [API documents](https://drive.google.com/drive/u/1/folders/1kpU5b04oDoB0SYhtcUaB6DPn06s1nv4a) or see project.postman_collection.json via Postman
### patient microservice
* GET - get specific patient info by patient id: http://localhost:5000/patient/*id* <br>
eg. http://localhost:5000/patient/t1234567a
* POST - create patient: http://localhost:5000/patient/create <br>
sample input see postman
### inventory microservice
* GET - get all medicines info in inventory MS: http://localhost:5002/inventory
* GET - get specific medicine info by medicine name: http://localhost:5002/inventory/*name* <br>
eg. http://localhost:5002/inventory/Amlodipine
* PUT - update medicine inventory by medicine name: http://localhost:5002/inventory/*name* <br>
eg. http://localhost:5002/inventory/Adderall <br>
sample input see postman
### prescription microservice
* GET - get prescriptions by status: http://localhost:5001/prescription/*status* <br>
eg. http://localhost:5001/prescription/pending
* GET - get prescriptions by status and sendToPayment: http://localhost:5001/prescription/*status*/*sendToPayment* <br>
eg. http://localhost:5001/prescription/pending/no
* POST - create prescription: http://localhost:5001/prescription/create <br>
sample input see postman
* PUT - update prescription status or sendToPayment by prescription id: http://localhost:5001/prescription/*id* <br>
eg. http://localhost:5001/prescription/17 <br>
sample inputs see postman
### payment service
* GET - get all prescription records in payment MS: http://localhost:5003/payment
* GET - get specific prescription info by payment id: http://localhost:5003/payment/*id* <br>
eg. http://localhost:5003/payment/1
* GET - get prescriptions by patient_id and payment status: http://localhost:5003/payment/*patient_id*/*status* <br>
eg. http://localhost:5003/payment/t1234567a/paid
* POST - record prescription in payment MS: http://localhost:5003/payment/create <br>
sample input see postman
* PUT - update prescription order_id and payment status by payment id: http://localhost:5003/payment/*id* <br>
eg. http://localhost:5003/payment/6 <br>
sample input see postman
### process complex microservice
* GET - complete senario2 3) to 8): http://localhost:5100/processPendingPrescriptions <br>
pharmacist UI pending page invokes this when loads and get all the pending prescriptions
* PUT - complete scenario2 12) to 16): http://localhost:5100/confirmPrescription <br>
pharmacist UI pending page invokes this when the comfirm buttom is pressed for each prescription <br>
sample UI input: {prescription_id: 1}



