w1 = input("widerstand 1: ")
w2 = input ("widerstand 2: ")

berechnung = (int(w1) * int(w2))/ (int(w1)+ int(w2))
print("Ihr Ergebnis: Der Gesamtwiderstand beträgt {:.2f} Ohm".format(berechnung))