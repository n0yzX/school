zahlinput = 8

def reku_fak(zahl):
    if zahl == 1:
        return 1
    else:
        return zahl * reku_fak(zahl-1)

print(reku_fak(zahlinput))

def iter_fak (zahl):
    if zahl == 1:
        return 1

    else:
        sum = 1
        for n in range(2, zahl +1):
            sum *= n
        
        return sum


print(iter_fak(zahlinput))