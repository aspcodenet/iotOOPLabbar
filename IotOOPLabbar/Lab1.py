from enum import Enum

class FoodType(Enum):
    FoodType_Vegetarisk = 1
    FoodType_Vegan = 2
    FoodType_Kott = 3

class Matratt:
    def __init__(self, name, price, type, calories):
        self._name = name
        self._price = price
        self._type = type
        self._calories = calories
    
    def GetName(self):
        return self._name

    def GetPrice(self):
        return self._price

    def GetType(self):
        return self._type.name

    def GetFoodType(self):
        return self._type




lunchMeny = []
lunchMeny.append(Matratt("Spagetti Carbonara",99,FoodType.FoodType_Kott,100))
lunchMeny.append(Matratt("Pannkakor",85,FoodType.FoodType_Vegetarisk,20))
lunchMeny.append(Matratt("Årtsoppa",60,FoodType.FoodType_Vegan,50))

print("Kött meny")
for mat in lunchMeny:
    if mat.GetFoodType() == FoodType.FoodType_Kott:
        print(f"{mat.GetName(), mat.GetPrice(), mat.GetType()}")

print("Vegetarisk meny")
for mat in lunchMeny:
    if mat.GetType() == FoodType.FoodType_Vegetarisk:
        print(f"{mat.GetName(), mat.GetPrice(), mat.GetType()}")

print("Vegan meny")
for mat in lunchMeny:
    if mat.GetType() == FoodType.FoodType_Vegan:
        print(f"{mat.GetName(), mat.GetPrice(), mat.GetType()}")
