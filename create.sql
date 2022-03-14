-- create patient database and table

drop database if exists patient;
create database patient;
use patient;

CREATE TABLE patient (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  age INT NOT NULL,
  allergies VARCHAR(255),
  hp VARCHAR(15) NOT NULL,
  email VARCHAR(255)
);
INSERT INTO patient
  (name,age,allergies,hp,email)
VALUES
  ('Kim Kardashian',41,'Amoxicillin, ampicillin',91234567,'hello@gmail.com'),
  ('Dwayne Johnson',49,'Aspirin',92345643,'hello@gmail.com'),
  ('Cardi B',29,'Ibuprofen',91345675,'hello@gmail.com'),
  ('Ben Affleck',49,'',91345675,'hello@gmail.com'),
  ('Tom Hanks',65,'',91345675,'hello@gmail.com'),
  ('Drake',35,'',91345675,'hello@gmail.com'),
  ('Ellen DeGeneres',64,'',91345675,'hello@gmail.com'),
  ('Justin Bieber',28,'',91345675,'hello@gmail.com'),
  ('Adele',30,'',91345675,'hello@gmail.com'),
  ('Leonardo Dicaprio',34,'',91234567,'hello@gmail.com'),
  ('George Clooney',45,'Cetuximab',91234567,'hello@gmail.com'),
  ('Jessica Alba',29,'',91234567,'hello@gmail.com'),
  ('Angeline Jolie',30,'',91234567,'hello@gmail.com');
  
  
-- create prescription database and table

drop database if exists prescription;
create database prescription;
use prescription;

CREATE TABLE prescription (
  id INT NOT NULL AUTO_INCREMENT,
  doctor_id INT,
  patient_id INT,
  description TEXT,
  medicines TEXT,
  status VARCHAR(255),
  PRIMARY KEY (id)
);
INSERT INTO prescription
  (doctor_id,patient_id,description,medicines,status)
VALUES
  (1,1,'Runny nose, sore throat','Cymbalta, Omeprazole, Fentanyl','pending'),
  (2,2,'Covid','Ibuprofen','pending'),
  (3,3,'Diarrhea','Methotrexate, Wellbutrin','confirmed'),
  (6,4,'Fever','Xanax, Azithromycin','pending'),
  (4,5,'Headache','Clonazepam','completed'),
  (3,6,'Runny nose, sore throat','Citalopram','pending'),
  (2,7,'Flu','Imbruvica, Gabapentin','pending'),
  (5,8,'Dry cough','Naloxone','confirmed'),
  (3,9,'Dizzy','Naproxen, Metoprolol, Gabapentin','completed'),
  (4,10,'Flu','Amitriptyline','pending'),
  (4,11,'Nausea','Cyclobenzaprine, Lexapro, Amlodipine','completed'),
  (2,12,'Fatigue','Acetaminophen','completed'),
  (4,13,'Knee pain','Omeprazole','completed'),
  (2,11,'Dizzy spells, nauseous','Januvia','confirmed'),
  (5,1,'Flu symptoms','Entresto, Benzonatate, Hydroxychloroquine, Gabapentin','confirmed'),
  (5,2,'Food poisoning','Methadone, Loratadine','confirmed'),
  (6,3,'Stomach flu','Adderall','pending');
  


-- create inventory database and table

drop database if exists inventory;
create database inventory;
use inventory;

CREATE TABLE inventory (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  price FLOAT,
  stock INT
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



-- create payment database and table

drop database if exists payment;
create database payment;
use payment;

CREATE TABLE payment (
  id INT NOT NULL AUTO_INCREMENT,
  prescription_id INT,
  patient_id INT,
  medicines TEXT,
  total FLOAT,
  order_id VARCHAR(255),
  status VARCHAR(255),
  PRIMARY KEY (id)
);
INSERT INTO payment
  (prescription_id,patient_id,medicines,total,order_id,status)
VALUES
  (1,1,'Cymbalta, Omeprazole, Fentanyl',13.12,'dummy','paid'),
  (2,2,'Ibuprofen',1.90,'dummy','paid'),
  (3,3,'Methotrexate, Wellbutrin',24.12,'dummy','paid'),
  (4,4,'Xanax, Azithromycin',15.00,'dummy','paid'),
  (5,5,'Cephalexin',7.05,'dummy','paid'),
  (6,6,'Cyclobenzaprine',3.49,'dummy','paid'),
  (7,7,'Imbruvica, Gabapentin',25.68,'dummy','unpaid'),
  (8,8,'Naloxone',1.32,'dummy','unpaid'),
  (9,9,'Naproxen, Metoprolol, Gabapentin',37.03,NULL,'paid'),
  (10,10,'Amitriptyline',6.18,NULL,'unpaid'),
  (11,11,'Cyclobenzaprine, Lexapro, Amlodipine',17.99,NULL,'unpaid'),
  (12,12,'Acetaminophen',11.56,NULL,'unpaid'),
  (13,13,'Omeprazole',3.71,NULL,'unpaid'),
  (14,11,'Januvia',14.32,NULL,'unpaid'),
  (15,1,'Entresto, Benzonatate, Hydroxychloroquine, Gabapentin',41.66,NULL,'unpaid'),
  (16,2,'Methadone, Loratadine',16.33,NULL,'unpaid'),
  (17,3,'Adderall',0.81,NULL,'unpaid');

  

