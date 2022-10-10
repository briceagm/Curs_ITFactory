# Ex.2
"""
Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""
print("Exercitiul 2")
class Dreptunghi:

    def __init__(self, lungime, latime, culoare="portocalie"):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Avem dreptunghiul cu lungimea de {self.lungime} cm; latimea de {self.latime} cm si culoarea {self.culoare}")

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return self.latime * 2 + self.lungime * 2

    def schimba_culoare(self, noua_culoare="albastru"):
         self.culoare = noua_culoare


dreptunghi1 = Dreptunghi(4, 5)
print("Dreptunghi nr.1")
dreptunghi1.descrie()
print(f"Aria dreptunghiului  este de: {dreptunghi1.aria()} cm")
print(f"Perimetrul dreptunghiului este de: {dreptunghi1.perimetrul()} cm")
#culoare lipseste, nu inteleg cum merge
print()
dreptunghi2 = Dreptunghi(6, 9, "verde")
print("Dreptunghi nr.2")
dreptunghi2.descrie()
print(f"Aria dreptunghiului  este de: {dreptunghi2.aria()} cm")
print(f"Perimetrul dreptunghiului este de: {dreptunghi2.perimetrul()} cm")
print()