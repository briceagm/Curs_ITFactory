import math
from abc import ABC
"""
Pilonii OOP(en): inheritance(mostenire), abstraction(abstractizare), polymorphism(polimorfism), encapsulation(incapsulare).
2.Abstractizarea - ca si mostenira , DAR clasa parinte este o clasa abstracta,adica nu putem face obiecte din ea, 
                   si o folosim doar  ca si un template pentru metodele pe care ar trebui sa le implementeze copiii
                   
Clasa abstracta trebuie sa mosteneasca clasa ABC(from abc import ABC).
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia  No ImplementedError.
Clasa abstracta NU are constructor, deoarece nu putem face obiecte abstracte.

3.Polimorfism -> poli(mai mult/e) morfis(forma/forme) ==> ceva care poate lua mai multe forme.
In cazul nostru, o functie de excemplu care desi are acelasi nume, are implementari/definitii diferite.
Exemple: Aria si perimetru.


"""

class FormGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError


class Cerc(FormGeometrica):

    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return self.raza**2 * 3.14

    def perimetru(self):
        return self.raza * 3.14


class Dreptunghi(FormGeometrica):

    def __init__(self, latura1, latura2):
        self.latura1 = latura1
        self.latura2 = latura2

    def aria(self):
        return self.latura1 * self.latura2

    def perimetru(self):
        return 2*(self.latura1 +self.latura2)

    def diagonala(self):
        return  math.sqrt(self.latura1**2 + self.latura2**2)


cerc = Cerc(10)
dreptunghi = Dreptunghi(4, 6)
print(cerc.aria())
print(dreptunghi.aria())

print(cerc.perimetru())
print(dreptunghi.perimetru())

lista_fg = [Cerc(3), Dreptunghi(3, 4), Cerc(10), Dreptunghi(5, 6), Dreptunghi(7,2), Cerc(8)]
for fg in lista_fg:
    print()
    print(f"Perimetrul: {fg.perimetru()} ")
    print(f"Aria: {fg.aria()}")
