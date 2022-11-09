import random 

zahl1 = random.randrange(1,7)
zahl2 = random.randrange(1,7)

print(zahl1)
print(zahl2)

if zahl1 == zahl2 :
    print("unentschieden!!")

elif zahl1 > zahl2:
    print("Spieler 1 hat gewonnen: Spieler 1 würfelt eine {} und Spieler2 eine {}".format(zahl1,zahl2))

else:
        print("Spieler 2 hat gewonnen: Spieler 1 würfelt eine {} und Spieler2 eine {}".format(zahl1,zahl2))

if zahl1 == zahl2 +1 or zahl2 == zahl1 +1:
    print("knapper Sieg")

else:
    ("deutlicher Sieg")
