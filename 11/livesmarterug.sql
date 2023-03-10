DROP Database livesmart;
CREATE DATABASE livesmart;
USE livesmart;

CREATE TABLE kunde (
    kundennr INT PRIMARY KEY AUTO_INCREMENT,
    vorname VARCHAR(30) NOT NULL,
    nachname VARCHAR(30)NOT NULL,
    telefon VARCHAR(30) NOT NULL,
    strasse VARCHAR(30) NOT NULL,
    plz INT(5) NOT NULL,
    ort VARCHAR(20)NOT NULL
);

CREATE TABLE auftrag (
    auftragsnr INT PRIMARY KEY AUTO_INCREMENT,
    kundennr INT,
    datum DATE NOT NULL,
    frist DATE NOT NULL,
    erledigt BOOLEAN NOT NULL,
    bezahlt BOOLEAN NOT NULL,
    FOREIGN KEY (kundennr) REFERENCES kunde (kundennr)
);