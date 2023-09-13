from random import randint

rounds = int(input("Anzahl der Runden eingeben: "))
min_einsatz = 2
max_einsatz = 100
aktRound = 0

budget = float(input("Budget eingeben: "))

totalverlust_count = 0
durchschnittlicher_gewinn_verlust = 0

def roulette_simulation(startguthaben, anzahl_runden, min_einsatz, max_einsatz):
    aktuelles_guthaben = startguthaben

    for _ in range(anzahl_runden):
        aktueller_einsatz = min_einsatz

        zahl = randint(1, 36)

        if zahl % 2 == 1:
            aktuelles_guthaben -= aktueller_einsatz
            aktueller_einsatz *= 2
        else:
            aktuelles_guthaben += aktueller_einsatz
            aktueller_einsatz = min_einsatz

        if aktuelles_guthaben <= 0:
            return aktuelles_guthaben

    return aktuelles_guthaben

durchläufe = 1000

for _ in range(durchläufe):
    endguthaben = roulette_simulation(budget, rounds, min_einsatz, max_einsatz)
    if endguthaben <= 0:
        totalverlust_count += 1
    durchschnittlicher_gewinn_verlust += (endguthaben - budget)

durchschnittlicher_gewinn_verlust /= durchläufe

print(f"Durchschnittlicher Gewinn/Verlust: {durchschnittlicher_gewinn_verlust:.2f} EUR")
print(f"Totalverlust in {totalverlust_count} von {durchläufe} Durchläufen ({(totalverlust_count/durchläufe)*100:.2f}%)")
