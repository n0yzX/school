dividend= int(input("dividend: "))
divisor= int(input("divisor: "))


def ganz_teil (dividend, divisor):
    ergebnis = False
    check = dividend % divisor
    if(check is 0):
        ergebnis = True
        return ergebnis
    
    else:
        ergebnis = False
        return ergebnis
    return ergebnis


print(ganz_teil(dividend, divisor))