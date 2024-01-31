CREATE DATABASE zoo;

USE zoo;

CREATE TABLE animal (
id INT PRIMARY KEY AUTO_INCREMENT,
nom VARCHAR(255),
race VARCHAR(255),
cage_id INT,
naissance VARCHAR(255),
pays VARCHAR(255));

CREATE TABLE cage (
id INT PRIMARY KEY AUTO_INCREMENT,
superficie INT,
capacite INT);

INSERT INTO cage (superficie, capacite)
VALUES
(200, 10);

