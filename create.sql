-- create patient database and table

drop database if exists patient;
create database patient;
use patient;

CREATE TABLE patient (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  allergies VARCHAR(255),
  hp VARCHAR(15) NOT NULL,
  email VARCHAR(255)
);
INSERT INTO patient
  (name,age,allergies,hp,email)
VALUES
  ('Kim Kardashian',41,'Amoxicillin, ampicillin',98443918,'hello@gmail.com'),
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
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  doctor_id INT NOT NULL,
  patient_id INT NOT NULL,
  description VARCHAR(65535),
  medicines VARCHAR(65535) NOT NULL,
  status VARCHAR(255) NOT NULL
);
INSERT INTO prescription
  (doctor_id,patient_id,description,medicines,status)
VALUES
  (1,1,'Runny nose, sore throat','{"Cymbalta":1, "Omeprazole":2, "Fentanyl":1}','pending'),
  (2,2,'Covid','{"Ibuprofen":2}','pending'),
  (3,3,'Diarrhea','{"Methotrexate":1, "Wellbutrin":1}','confirmed'),
  (6,4,'Fever','{"Xanax":1, "Azithromycin":1}','pending'),
  (4,5,'Headache','{"Clonazepam":1}','completed'),
  (3,6,'Runny nose, sore throat','{"Citalopram":1}','pending'),
  (2,7,'Flu','{"Imbruvica":2, "Gabapentin":1}','pending'),
  (5,8,'Dry cough','{"Naloxone":3}','confirmed'),
  (3,9,'Dizzy','{"Naproxen":2, "Metoprolol":4, "Gabapentin":2}','completed'),
  (4,10,'Flu','{"Amitriptyline":3}','pending'),
  (4,11,'Nausea','{"Cyclobenzaprine":2, "Lexapro":1, "Amlodipine":3}','completed'),
  (2,12,'Fatigue','{"Acetaminophen":2}','completed'),
  (4,13,'Knee pain','{"Omeprazole":1}','completed'),
  (2,11,'Dizzy spells, nauseous','{"Januvia":3}','confirmed'),
  (5,1,'Flu symptoms','{"Entresto":2, "Benzonatate":1, "Hydroxychloroquine":2, "Gabapentin":3}','confirmed'),
  (5,2,'Food poisoning','{"Methadone":1, "Loratadine":2}','confirmed'),
  (6,3,'Stomach flu','{"Adderall":4}','pending');
  


-- create inventory database and table

drop database if exists inventory;
create database inventory;
use inventory;

CREATE TABLE inventory (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price FLOAT NOT NULL,
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
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  prescription_id INT NOT NULL,
  patient_id INT NOT NULL,
  medicines VARCHAR(65535) NOT NULL,
  total FLOAT NOT NULL,
  order_id VARCHAR(255),
  status VARCHAR(255) NOT NULL
);
INSERT INTO payment
  (prescription_id,patient_id,medicines,total,order_id,status)
VALUES
  (1,1,'{"Cymbalta":1, "Omeprazole":2, "Fentanyl":1}',13.12,'dummy','unpaid'),
  (2,2,'{"Ibuprofen":2}',1.90,'dummy','paid'),
  (3,3,'{"Methotrexate":1, "Wellbutrin":1}',24.12,'dummy','paid'),
  (4,4,'{"Xanax":1, "Azithromycin":1}',15.00,'dummy','paid'),
  (5,5,'{"Clonazepam":1}',7.05,'dummy','paid'),
  (6,6,'{"Citalopram":1}',3.49,'dummy','paid'),
  (7,7,'{"Imbruvica":2, "Gabapentin":1}',25.68,'dummy','unpaid'),
  (8,8,'{"Naloxone":3}',1.32,'dummy','unpaid'),
  (9,9,'{"Naproxen":2, "Metoprolol":4, "Gabapentin":2}',37.03,NULL,'paid'),
  (10,10,'{"Amitriptyline":3}',6.18,NULL,'unpaid'),
  (11,11,'{"Cyclobenzaprine":2, "Lexapro":1, "Amlodipine":3}',17.99,NULL,'unpaid'),
  (12,12,'{"Acetaminophen":2}',11.56,NULL,'unpaid'),
  (13,13,'{"Omeprazole":1}',3.71,NULL,'unpaid'),
  (14,11,'{"Januvia":3}',14.32,NULL,'unpaid'),
  (15,1,'{"Entresto":2, "Benzonatate":1, "Hydroxychloroquine":2, "Gabapentin":3}',41.66,NULL,'unpaid'),
  (16,2,'{"Methadone":1, "Loratadine":2}',16.33,NULL,'unpaid'),
  (17,3,'{"Adderall":4}',0.81,NULL,'unpaid');
