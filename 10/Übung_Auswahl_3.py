year = int(input("Geben Sie eine Jahreszahl ein: \n"))
schaltyear = false

if year >= 1582 :
    if year%4 == 0 :
        schaltyear = true

    elif year%100 != 0 :
        if year%400 == 0 :
            schaltyear = true
        
        else:
            schaltyear = false
    if schaltyear = true :
        print("Das Jahr {} ist ein Schaltjahr".format(year))
    else:
        print("Das Jahr {} ist kein Schaltjahr".format(year))
else:
    print("Das Jahr {} ist kein Schaltjahr. Schaltjahre gibt es erst seit 1582".format(year))
