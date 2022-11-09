def reku_fak(zahl):
    if zahl == 1:
        return 1
    else:
        return zahl * reku_fak(zahl-1)

print(reku_fak(4))