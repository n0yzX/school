from datetime import date

zugehörigkeit = int(input("zugehörigkeit: "))
geburtsjahr = int(input("Geburtsjahr: "))

def betriebszugehoerigkeit(zugehörigkeit, geburtsjahr):
    if zugehörigkeit <=5:
        praemie = "Praline";
    elif zugehörigkeit >=10:
        praemie = "Geschenkekorb";
    elif zugehörigkeit <=11 and zugehörigkeit >=19:
        praemie = "halben Urlaubstag";
    elif zugehörigkeit <=20:
        praemie = "1 Urlaubstag";
    else:
        return false;
    
    if(date.today().year-geburtsjahr)%5==0:
        praemie= praemie + "und ein Blumenstrauß";

    return praemie;

print("Deine Prämie ist" ,betriebszugehoerigkeit(zugehörigkeit, geburtsjahr))