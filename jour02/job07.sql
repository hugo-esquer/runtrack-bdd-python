CREATE DATABASE Entreprise

USE Entreprise

CREATE TABLE employe(
id INT PRIMARY KEY AUTO_INCREMENT,
nom VARCHAR(255),
prenom VARCHAR(255),
salaire DECIMAL (10, 2),
id_service INT);

INSERT INTO employe (nom, prenom, salaire, id_service)
VALUES
('Esquer', 'Hugo', 3200, 1),
('Clavis', 'Tom', 3200, 1),
('Mazard', 'Pierre', 2800, 2),
('Aschehoug', 'Erika', 2800, 3),
('Frah', 'Mohamed', 2800, 3);

CREATE TABLE service (
id INT PRIMARY KEY AUTO_INCREMENT,
nom VARCHAR(255));

INSERT INTO service (nom)
VALUES
('Cybersecurite'),
('Logiciel'),
('Web');

