verbrauch = input("wie viel Liter haben sie verbraucht?")
strecke = input("wie viel km sind sie gefahren?")

ausgabe = (int(verbrauch ) * 100 ) /  int(strecke)
print("Der Durschnittsverbrauch beträgt bei {:.2f} l/100km".format(ausgabe))