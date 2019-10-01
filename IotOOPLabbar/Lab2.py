
import datetime

class Person:
    def __init__(self, birthDate, namn="", gatuadress="", postnummer="", postort=""):
        self._birthDate = birthDate
        self._namn = namn
        self._gatuadress = gatuadress
        self._postnummer = postnummer
        self._postort = postort
        self._skola = ""
    
    def GetGatuAdress(self):
        return self._gatuadress
    def GetPostNummer(self):
        return self._postnummer
    def GetPostOrt(self):
        return self._postort

    def Namnge(self, nyttNamn):
        if len(nyttNamn) > 255:
            raise ValueError("För långt namn")
        self._namn = nyttNamn

    def BytAdress(self, gatuadress, postnummer, postort):
        self._gatuadress = gatuadress
        self._postnummer = postnummer
        self._postort = postort

    def FlyttaInHos(self, otherPerson):
        self.BytAdress(otherPerson.GetGatuAdress(), otherPerson.GetPostNummer(),otherPerson.GetPostOrt())

barnet = Person(datetime.date(2008,5,28))
barnet.BytAdress("Testgatan 12", "11111", "Teststad")


jag = Person(datetime.date(1972,8,3),"Stefan","Testgatan 123","11111", "Teststad")
fru = Person(datetime.date(1973,3,5),"Kerstin","Hejvägen 1","22222", "Tvåstad")
#jag.BytAdress(fru.GetGatuAdress(), fru.GetPostNummer(), fru.GetPostOrt())
jag.FlyttaInHos(fru)
print(f"Nu bor jag på {jag.GetGatuAdress()} {jag.GetPostNummer()}  {jag.GetPostOrt()} ")