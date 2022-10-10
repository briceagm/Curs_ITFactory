"""
Pilonii OOP(en): inheritance(mostenire), abstraction(abstractizare), polymorphism(polimorfism), encapsulation(incapsulare).

4.Incapulare(Encapsulation)- posibilitatea de a proteja atributele clasei, folosind modificatorii de vizibilitate
 - private(privat, adica  atributul poate fi accesat DOAR in interiorul clasei in care a fost definit)
  se defineste cu dublu undersore in fata(__asa)

  - protected(protejat, adica atributul poate fi accesat din clasa in care a fost definit, dar si in clasele copil ale acesteia, INSA nu din exterior)
   se defineste cu un singur undersore(_asa)

Atunci cand avem un atribut ascuns(privat), putem folosi niste metode speciale pentru a interactiona  cu el numite getter(pentru a-l vedea) si setter(pentru a-i schimba valoarea)

In general, metodele acestea se vor denumi cu set_/ get_ PLUS numele initial al variabilei:

Class X:
     __ceva

     def get_ceva(self):
        return __ceva

     def set_ceva(slef, ceva_nou):
        __ceva = ceva_nou

"""

class Factura:
    # atributele de clasa, daca modificam o data, modificam pentru TOATE obiectele
    __seria = "xyz" # atributele cu doua underscore in fata sunt PRIVATE
    numar = 1

    def __init__(self, nume_produs, cantitate, pret_buc):
        self.nr_fact = Factura.numar
        self.prdus = nume_produs
        self.cantitate = cantitate
        self.pret = pret_buc
        Factura.numar += 1

    #getter
    def get_seria(self):
        return self.__seria

    #setter
    def schimba_serie(self, noua_serie):
        # Aici putem face validari, de exemplu poate vrem ca seria sa fie de minim3, maxim 6 caractere
        if 3 <= len(noua_serie) <= 6:
            self.__seria  = noua_serie
        else:
            print("NU e buna seria, mai incearca")

    def descrie(self):
        print(f"{self.__seria} {self.nr_fact}")
        print(f"Produs | Cantitate | Pret unitar | Total")
        print(f"{self.prdus} | {self.cantitate} | {self.pret} | {self.cantitate * self.pret}")

factura1 = Factura("Telefon", 10, 120)
# print(factura1.__seria, factura1.numar)

factura2 = Factura("TV", 6, 45)
# print(factura2.seria, factura2.numar)
#
# Factura.seria = "ABC"
#
# # factura2.seria = "lop"  se schimba doar seria facturei nr.2
# print(factura1.seria, factura1.numar)
# print(factura2.seria, factura2.numar)

factura1.descrie()
factura1.schimba_serie("ABC")
factura1.descrie()
factura1.schimba_serie("2334456677")
