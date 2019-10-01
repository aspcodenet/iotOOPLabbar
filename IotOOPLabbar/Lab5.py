class Dog:
    def __init__(self, namn, ras,alder,vikt):
        self._namn = namn
        self._ras = ras
        self._alder = alder
        self._vikt = vikt

    def GetNamn(self):
        return self._namn

    def GetVikt(self):
        return self._vikt

    def GetRas(self):
        return self._ras


    def TailLength(self):
        if self._ras == "tax":
           return 3.7
        return self._alder * self._vikt / 10.0

class Kennel:
    def __init__(self):
        self._dogs = []

    def AddDog(self, dog):
        self._dogs.append(dog)

    def ListDogs(self, length):
        list = []
        for d in self._dogs:
            if d.GetTailLength() > length:
                list.append(d)
        return list


    def RemoveDog(self, dog):
        self._dogs.remove(dog)

    def DogExists(self, namn):
        for dog in self._dogs:
            if book.GetNamn() == namn:
                return dog
        return None



ourKennel = Kennel()
while True:
    print("1. Lägg till hund")
    print("2. Lista")
    print("3. Returnera bok")
    s = input("Välj ->")
    if s == "1":
        print("Namn på hund")
        namn = input("->")
        print("Ras")
        ras = input("->")
        print("Ålder")
        alder = int(input("->"))
        print("Vikt")
        vikt = float(input("->"))
        ourKennel.AddDog(Dog(namn,ras,alder,vikt))
    elif s == "2":
        print("Minsta svanslängd")
        lent = float(input("->"))
        for dog in ourKennel.ListDogs(lent):
            print(f"{dog.GetName()} {dog.GetRas()} {dog.GetVikt()} kg svans={dog.GetTailLength()}")
    elif s == "3":
        print("Namn hund att ta bort")
        namn = input("->")
        dog =  ourKennel.DogExists(namn)
        if dog is None:
            print("Hund med det namnet fanns ej i registret")
        else:
            ourKennel.RemoveDog(dog)
    elif s == "4":
        break
    