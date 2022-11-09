import random

guthaben = 500
min = 2
max = 100
einsatz = 0
count = 0
maxCount = 500
win = 0
loose = 0

while maxCount > count :
    zahl = random.randrange(0,35)
    check = zahl % 2
    guthabencheck = guthaben - einsatz
    if guthabencheck <= 0:
        break
    
    #gerade
    if zahl != 0 and check == 0:
        count +=1        
        gewinn = einsatz *2
        guthaben = guthaben + gewinn
        einsatz = min
        win +=1

    #ungerade
    elif zahl == 0 or check != 0:
        count +=1
        einsatz = einsatz * 2
        loose +=1
        
        if einsatz > max:
            einsatz = 100
            guthaben = guthaben - einsatz
        
        else:            
            guthaben = guthaben - einsatz
        


print('count:', count)
print('guthaben',guthaben)
print('win',win)
print('loose',loose)