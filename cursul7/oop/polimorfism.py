"""
Pilonii OOP(en): inheritance(mostenire), abstraction(abstractizare), polymorphism(polimorfism), encapsulation(incapsulare).


3.Polimorfism- mai multe functii cu acelasi nume, dar comportament sau parametrii diferiti.
Polimorfism -> poli(mai mult/e) morfis(forma/forme) ==> ceva care poate lua mai multe forme.
In cazul nostru, o functie de excemplu care desi are acelasi nume, are implementari/definitii diferite.
Exemple: Aria si perimetru.

Metoda language este polimorfica, deoarece returneaza lucruri diferite in functie de obiectul care o apeleaza, DAR numele metodei este mereu acelasi.
"""

class Romania:

    def language(self):
        return "ro"

class Franta:

    def language(self):
        return "fr"

instanta_ro = Romania()
instanta_fr = Franta()

print(instanta_ro.language())
print(instanta_fr.language())

def add(a, b):
    return a + b

def add(a, b, c=0):
    return a + b + c

print(add(3, 5))
print(add(4, 5, 2))