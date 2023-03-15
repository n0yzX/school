DROP DATABASE IF EXISTS LiveSmarter;
CREATE DATABASE LiveSmarter;

CREATE TABLE kunde(
kundennummer INT NOT NULL,
vorname VARCHAR(50),
nachname VARCHAR(50),
telefon VARCHAR(50),
strasse VARCHAR(50),
plz VARCHAR(10),
ort VARCHAR(50),
CONSTRAINT pk_kunde PRIMARY KEY (kundennummer)
);

CREATE TABLE auftrag(
auftragsnummer INT NOT NULL,
kundennummer INT NOT NULL,
auftragsdatum date,
frist date,
erledigt TINYINT,
bezahlt TINYINT,
CONSTRAINT pk_auftrag PRIMARY KEY (auftragsnummer),
CONSTRAINT fk_auftrag_kunde FOREIGN KEY (kundennummer) REFERENCES kunde (kundennummer)
);

CREATE TABLE lieferant
(
lieferantennummer INT NOT NULL,
lieferantenname VARCHAR(255),
telefonnummer VARCHAR(50),
webseite VARCHAR(255),
CONSTRAINT pk_lieferant PRIMARY KEY(lieferantennummer)
);

CREATE TABLE hersteller
(
herstellernummer INT NOT NULL,
herstellername VARCHAR(255),
kontaktnummer VARCHAR (50),
CONSTRAINT pk_hersteller PRIMARY KEY (herstellernummer)
);

CREATE TABLE artikel
(
artikelnummer INT NOT NULL,
artikelname VARCHAR (255) NOT NULL,
artikelart VARCHAR (100),
herstellernummer INT,
verkaufspreis DECIMAL(10,2),
CONSTRAINT pk_artikel PRIMARY KEY (artikelnummer),
CONSTRAINT fk_artikel_hersteller FOREIGN KEY (herstellernummer) REFERENCES hersteller (herstellernummer)
);

CREATE TABLE artikellieferant
(
artikelnummer INT NOT NULL,
lieferantennummer INT NOT NULL,
einkaufspreis DECIMAL(10,2),
CONSTRAINT pk_artikel PRIMARY KEY (artikelnummer,lieferantennummer),
CONSTRAINT fk_artikellieferant_artikel FOREIGN KEY (artikelnummer) REFERENCES artikel (artikelnummer),
CONSTRAINT fk_artikellieferant_lieferant FOREIGN KEY (lieferantennummer) REFERENCES lieferant (lieferantennummer)
);

CREATE TABLE auftragsposition
(
artikelnummer INT NOT NULL,
auftragsnummer INT NOT NULL,
auftragspos INT NOT NULL,
menge INT NOT NULL,
CONSTRAINT pk_artikel PRIMARY KEY (artikelnummer,auftragsnummer),
CONSTRAINT fk_auftragsposition_artikel FOREIGN KEY (artikelnummer) REFERENCES artikel (artikelnummer),
CONSTRAINT fk_auftragsposition_auftragsnummer FOREIGN KEY (auftragsnummer) REFERENCES auftrag (auftragsnummer)
);