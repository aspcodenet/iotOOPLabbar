
import datetime

class Person:
    def __init__(self, birthDate, namn="", gatuadress="", postnummer="", postort=""):
        self._birthDate = birthDate
        self._namn = namn
        self._gatuadress = gatuadress
        self._postnummer = postnummer
        self._postort = postort
    
    def GetGatuAdress(self):
        return self._gatuadress
    def GetPostNummer(self):
        return self._postnummer
    def GetPostOrt(self):
        return self._postort

    def Namnge(self, nyttNamn):
        self._namn = nyttNamn

    def BytAdress(self, gatuadress, postnummer, postort):
        self._gatuadress = gatuadress
        self._postnummer = postnummer
        self._postort = postort

    def GetAge(self):
        return datetime.datetime.now().year - self._birthDate.year

    def FlyttaInHos(self, otherPerson):
        self.BytAdress(otherPerson.GetGatuAdress(), otherPerson.GetPostNummer(),otherPerson.GetPostOrt())


jag = Person(datetime.date(1972,8,3),"Stefan","Testgatan 123","11111", "Teststad")
print(f" jag är {jag.GetAge()}")