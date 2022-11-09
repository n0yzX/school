from random import *


# Aufgabe 1
list = []
count = 0
sum = 0

while count < 10:
    zahl = randint(1,20)
    list.append(zahl)
    count +=1

for i in list:
    sum = sum +i


print(list)
print(sum)




# Aufgabe 2

list2 = []
count2 = 0

while count2 < 10:
    zahl2 = randint(1,20)
    list2.append(zahl2)
    count2 +=1
print(list2)
zahlinput = int(input("Geben sie eine Zahl ein: "))
for x in list2:
    if x == zahlinput:
        ausgabe = "Die eingegeben Zahl ist vorhanden"
        break
    
    else:
        ausgabe = "Die eingegeben Zahl ist nicht vorhanden"
        
print(ausgabe)

# Aufgabe Multiplikation
zahlinput = int(input("Gebe eine Zahl ein: "))
count = 1
list = []


while count < 11 :
    summe = zahlinput * count
    list.append(summe)
    count +=1

print(list)


# Aufgabe Hufschmied
naegel = 24
count3 = 1
summe3 = 0


while count3 < naegel :
    summe3 = summe3 +  2**count3
    count3 += 1
print(summe3)