from random import randint

class Mitarbeiter:
    def __init__(self, vorname, nachname, gehalt, abteilung):
        self.__id = randint(1,1000)
        self.__vorname = vorname
        self.__nachname = nachname
        self.__gehalt = gehalt
        self.__abteilung = abteilung

    def GetMitarbeiterInfo(self):
        return f"ID: {self.__id}\nName: {self.__vorname} {self.__nachname}\nGehalt: {self.__gehalt} Euro\nAbteilung: {self.__abteilung}"

    def ErhoeheGehalt(self, prozentsatz):
        erhoehterGehalt = self.gehalt * (1 + prozentsatz / 100)
        self.gehalt = round(erhoehterGehalt, 2)

    def WechsleAbteilung(self, neueAbteilung):
        self.abteilung = neueAbteilung
        
Mitarbeiterarray = [Mitarbeiter("Thomas", "Müller", 3450.32, "Rechnungswesen"),
                    Mitarbeiter("Michael", "Bauer", 2630.21, "Lager")]


for x in range(0, len(Mitarbeiterarray)):
    
    print(" ")
    print(Mitarbeiterarray[x].GetMitarbeiterInfo())