Aufgabe 1

SELECT a.artikelnummer, a.artikelname, a.artikelart, h.herstellername
FROM artikel a
INNER JOIN hersteller h ON a.herstellernummer = h.herstellernummer


Aufgabe 2
SELECT a.artikelnummer, a.artikelname ap.menge, au.kundennummer, au.auftragsnummer
FROM auftrag au
INNER JOIN auftragsposition ap ON au.auftragsnummer = ap.auftragsnummer
INNER JOIN artikel a ON a.artikelnummer = ap.artikelnummer
WHERE au.auftragsnummer = 201