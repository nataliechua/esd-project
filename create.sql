-- create patient table

drop database if exists patient;
create database patient;
use patient;


CREATE TABLE patient (
  id VARCHAR(15) PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  allergies VARCHAR(255),
  hp VARCHAR(15) NOT NULL,
  email VARCHAR(255)
);
INSERT INTO patient
  (id,name,age,allergies,hp,email)
VALUES
  ('t1234567a','Kim Kardashian',41,'Amoxicillin, ampicillin',91234567,'hello@gmail.com'),
  ('t1234568a','Dwayne Johnson',49,'Aspirin',92345643,'hello@gmail.com'),
  ('t1234569a','Cardi B',29,'Ibuprofen',91345675,'hello@gmail.com'),
  ('t1234570a','Ben Affleck',49,'',91345675,'hello@gmail.com'),
  ('t1234571a','Tom Hanks',65,'',91345675,'hello@gmail.com'),
  ('t1234572a','Drake',35,'',91345675,'hello@gmail.com'),
  ('t1234573a','Ellen DeGeneres',64,'',91345675,'hello@gmail.com'),
  ('t1234574a','Justin Bieber',28,'',91345675,'hello@gmail.com'),
  ('t1234575a','Adele',30,'',91345675,'hello@gmail.com'),
  ('t1234576a','Leonardo Dicaprio',34,'',91234567,'hello@gmail.com'),
  ('t1234577a','George Clooney',45,'Cetuximab',91234567,'hello@gmail.com'),
  ('t1234578a','Jessica Alba',29,'',91234567,'hello@gmail.com'),
  ('t1234579a','Angeline Jolie',30,'',91234567,'hello@gmail.com');

  
-- create doctor table, not using

drop database if exists doctor;
create database doctor;
use doctor;

CREATE TABLE doctor (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  hp VARCHAR(15),
  email VARCHAR(255)
);
INSERT INTO doctor
  (name,hp,email)
VALUES
  ('Meredith Grey',12345678,'doctor@hospital.com'),
  ('Owen Hunt',12345678,'doctor@hospital.com'),
  ('Derek Shepherd',12345678,'doctor@hospital.com'),
  ('Mark Sloan',12345678,'doctor@hospital.com'),
  ('Alex Karev',12345678,'doctor@hospital.com'),
  ('Jackson Avery',12345678,'doctor@hospital.com'),
  ('Amelia Shepherd',12345678,'doctor@hospital.com'),
  ('Callie Torres',12345678,'doctor@hospital.com'),
  ('Izzie Stevens',12345678,'doctor@hospital.com'),
  ('Andrew Deluca',12345678,'doctor@hospital.com'),
  ('Cristina Yang',12345678,'doctor@hospital.com'),
  ('Kai Bartley',12345678,'doctor@hospital.com');

  
-- create prescription table

drop database if exists prescription;
create database prescription;
use prescription;

CREATE TABLE prescription (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  doctor_id INT NOT NULL,
  patient_id VARCHAR(15) NOT NULL,
  description VARCHAR(65535),
  medicines VARCHAR(65535) NOT NULL,
  status VARCHAR(255) NOT NULL,
  sendToPayment VARCHAR(255) NOT NULL
);
INSERT INTO prescription
  (doctor_id,patient_id,description,medicines,status,sendToPayment)
VALUES
  (1,'t1234567a','Runny nose, sore throat','{"Cymbalta":1, "Omeprazole":2, "Fentanyl":1}','pending','yes'),
  (2,'t1234568a','Covid','{"Ibuprofen":2}','pending','yes'),
  (3,'t1234569a','Diarrhea','{"Methotrexate":1, "Wellbutrin":1}','confirmed','yes'),
  (6,'t1234570a','Fever','{"Xanax":1, "Azithromycin":1}','pending','no'),
  (4,'t1234571a','Headache','{"Clonazepam":1}','completed','yes'),
  (3,'t1234572a','Runny nose, sore throat','{"Brilinta":1}','pending','no'),
  (2,'t1234573a','Flu','{"Imbruvica":2, "Gabapentin":1}','pending','no'),
  (5,'t1234574a','Dry cough','{"Naloxone":3}','confirmed','yes'),
  (3,'t1234575a','Dizzy','{"Naproxen":2, "Metoprolol":4, "Gabapentin":2}','completed','yes'),
  (4,'t1234576a','Flu','{"Amitriptyline":3}','pending','no'),
  (4,'t1234577a','Nausea','{"Cyclobenzaprine":2, "Lexapro":1, "Amlodipine":3}','completed','yes'),
  (2,'t1234578a','Fatigue','{"Acetaminophen":2}','completed','yes'),
  (4,'t1234579a','Knee pain','{"Omeprazole":1}','completed','yes'),
  (2,'t1234577a','Dizzy spells, nauseous','{"Januvia":3}','confirmed','yes'),
  (5,'t1234567a','Flu symptoms','{"Entresto":2, "Benzonatate":1, "Hydroxychloroquine":2, "Gabapentin":3}','confirmed','yes'),
  (5,'t1234568a','Food poisoning','{"Methadone":1, "Loratadine":2}','confirmed','yes'),
  (6,'t1234569a','Stomach flu','{"Adderall":4}','pending','no');

  
-- create inventory table

drop database if exists inventory;
create database inventory;
use inventory;

CREATE TABLE inventory (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price FLOAT NOT NULL,
  stock INT NOT NULL
);
INSERT INTO inventory
  (name,price,stock)
VALUES
  ('Acetaminophen',10.37,29),
  ('Adderall',14.00,67),
  ('Amitriptyline',5.74,11),
  ('Amlodipine',12.69,60),
  ('Amoxicillin',13.18,21),
  ('Ativan',8.15,45),
  ('Atorvastatin',3.92,55),
  ('Azithromycin',7.68,26),
  ('Benzonatate',7.74,76),
  ('Brilinta',13.72,94),
  ('Bunavail',9.42,79),
  ('Buprenorphine',3.45,13),
  ('Cephalexin',3.43,71),
  ('Cyclobenzaprine',10.99,54),
  ('Cymbalta',11.35,38),
  ('Doxycycline',4.97,88),
  ('Dupixent',12.97,50),
  ('Entresto',6.22,23),
  ('Entyvio',3.15,9),
  ('Farxiga',12.23,54),
  ('Fentanyl',13.46,33),
  ('Fentanyl Patch',14.82,58),
  ('Gabapentin',2.02,60),
  ('Gilenya',10.75,65),
  ('Humira',0.72,53),
  ('Hydrochlorothiazide',1.85,61),
  ('Hydroxychloroquine',2.51,43),
  ('Ibuprofen',5.46,1),
  ('Imbruvica',0.12,6),
  ('Januvia',6.28,73),
  ('Jardiance',8.49,67),
  ('Kevzara',10.08,86),
  ('Lexapro',6.31,2),
  ('Lisinopril',4.97,74),
  ('Lofexidine',13.57,79),
  ('Loratadine',10.16,10),
  ('Lyrica',2.58,66),
  ('Melatonin',8.60,91),
  ('Meloxicam',13.19,13),
  ('Metformin',1.30,24),
  ('Methadone',14.78,22),
  ('Methotrexate',6.09,25),
  ('Metoprolol',12.86,36),
  ('Naloxone',7.20,86),
  ('Naltrexone',12.77,81),
  ('Naproxen',6.16,34),
  ('Omeprazole',6.19,46),
  ('Onpattro',12.04,69),
  ('Otezla',13.99,28),
  ('Ozempic',1.50,37),
  ('Pantoprazole',7.82,63),
  ('Prednisone',7.90,5),
  ('Probuphine',6.19,60),
  ('Rybelsus',7.69,14),
  ('secukinumab',5.23,57),
  ('Sublocade',12.61,2),
  ('Tramadol',3.39,41),
  ('Trazodone',3.18,36),
  ('Viagra',13.10,37),
  ('Wellbutrin',1.79,79),
  ('Xanax',6.20,46),
  ('Zubsolv',9.79,65);



-- create payment table

drop database if exists payment;
create database payment;
use payment;

CREATE TABLE payment (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  prescription_id INT NOT NULL,
  patient_id VARCHAR(15) NOT NULL,
  medicines VARCHAR(65535) NOT NULL,
  total FLOAT NOT NULL,
  order_id VARCHAR(255),
  status VARCHAR(255) NOT NULL
);

INSERT INTO payment
  (prescription_id,patient_id,medicines,total,order_id,status)
VALUES
  (1,'t1234567a','{"Cymbalta":1, "Omeprazole":2, "Fentanyl":1}',37.19,'dummy','paid'),
  (2,'t1234568a','{"Ibuprofen":2}',10.92,'dummy','paid'),
  (3,'t1234569a','{"Methotrexate":1, "Wellbutrin":1}',7.88,'dummy','paid'),
  (5,'t1234571a','{"Clonazepam":1}',7.05,'dummy','paid'),
  (8,'t1234574a','{"Naloxone":3}',21.6,'dummy','paid'),
  (9,'t1234575a','{"Naproxen":2, "Metoprolol":4, "Gabapentin":2}',67.8,NULL,'unpaid'),
  (11,'t1234577a','{"Cyclobenzaprine":2, "Lexapro":1, "Amlodipine":3}',66.36,NULL,'unpaid'),
  (12,'t1234578a','{"Acetaminophen":2}',20.74,NULL,'unpaid'),
  (13,'t1234579a','{"Omeprazole":1}',6.19,NULL,'unpaid'),
  (14,'t1234577a','{"Januvia":3}',18.84,NULL,'unpaid'),
  (15,'t1234567a','{"Entresto":2, "Benzonatate":1, "Hydroxychloroquine":2, "Gabapentin":3}',31.26,NULL,'unpaid'),
  (16,'t1234568a','{"Methadone":1, "Loratadine":2}',35.10,NULL,'unpaid');
