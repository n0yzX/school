Aufgabe 1

SELECT a.artikelnummer, a.artikelname, a.artikelart, h.herstellername
FROM artikel a
INNER JOIN hersteller h ON a.herstellernummer = h.herstellernummer


Aufgabe 2
SELECT a.artikelnummer, a.artikelname ap.menge, au.kundennummer, au.auftragsnummer
FROM auftrag au
INNER JOIN auftragsposition ap ON au.auftragsnummer = ap.auftragsnummer
INNER JOIN artikel a ON a.artikelnummer = ap.artikelnummer
WHERE au.auftragsnummer = 201;

Aufgabe 3

SELECT a.artikelnummer, a.artikelname, ap.menge, k.vorname, k.nachname, au.auftragsnummer
FROM auftrag au
INNER JOIN auftragsposition ap ON au.auftragsnummer = ap.auftragsnummer
INNER JOIN artikel a ON a.artikelnummer = ap.artikelnummer
INNER JOIN kunde k ON au.kundennummer = k.kundennummer
WHERE au.auftragsnummer = 201;

Aufgabe 4
SELECT a.artikelnummer, a.artikelname, l.lieferantenname, h.herstellername
FROM artikel a
INNER JOIN artikellieferant al ON a.artikelnummer = al.artikelnummer
INNER JOIN lieferant l ON al.lieferantennummer = l.lieferantennummer
INNER JOIN hersteller h ON h.herstellernummer = a.herstellernummer;