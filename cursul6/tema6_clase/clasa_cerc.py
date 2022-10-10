#OBLIGATORII
# Ex.1
"""
Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
print("Exercitiul 1")
import math

class Cerc:

    def __init__(self, raza, culoare="roz"):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Raza cercului este de: {self.raza} cm")
        print(f"Culoarea cercului este: {self.culoare}")

    def aria(self):
        return round(self.raza * self.raza * math.pi, 2)

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        # PI = 3.14
        return round(self.raza * math.pi * 2, 2)

cerc1 = Cerc(4)
print("Cerc nr. 1")
cerc1.descrie_cerc()
print(f"Cercul are aria de: {cerc1.aria()}  cm")
print(f"Cercul are diametrul de: {cerc1.diametru()} cm")
print(f"Circumferinta cercului este de: {cerc1.circumferinta()} cm")
print()
cerc2_galben = Cerc(14, "galben")
print("Cerc nr.2")
cerc2_galben.descrie_cerc()
print(f"Cercul are aria de: {cerc2_galben.aria()}  cm")
print(f"Cercul are diametrul de: {cerc2_galben.diametru()} cm")
print(f"Circumferinta cercului este de: {cerc2_galben.circumferinta()} cm")
print()