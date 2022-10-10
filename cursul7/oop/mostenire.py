"""
Pilonii OOP(en): inheritance(mostenire), abstraction(abstractizare), polymorphism(polimorfism), encapsulation(incapsulare).

1. Mostenire: uneori avem clase care impartasesc atribute.
             In cazul acesta putem face o clasa de baza(parinte) , si apoi clase copil, care sa mosteneasca parintele, si implicit toate atributele acestuia.

Mosteniare permite sa avem o ierarhie a claselor, cu oricate  nivele dorim.
Se pot mosteni atat atribute, cat si metodele clasei parinte.
Clasa copil poate avea in plus fata de clasa parinte orice atribute sau metode doreste.
In cazul metodelor, atunci cand avem in clasa copil o metoda exact ca si cea din clasa parinte, zicem ca o suprascriem(overwrite) si TREBUIE sa fim atenti ca daca vrem sa beneficiem si de ceea ce se intampla in clasa parinte, sa o apelam cu super() => exemplu in constructor.
"""
# clasa parinte (de baza)
class Person:
    #atribut de clase
    contor_persoane = 0

    def __init__(self, nume, varsta, adresa):
        Person.contor_persoane += 1
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def descrie(self):
        print("*"*30)
        print(f"Nume: {self.nume}")
        print(f"Varsta: {self.varsta}")
        print(f"Adresa: {self.adresa}")

    def anul_nasterii(self):
        return 2022 - self.varsta

# clasa copil(mosteneste Person, si implicit toate atributele acestuia)
class Student(Person):

    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        #super() reprezinta clasa parinte, in cazul nostru Person
        # deci practic aici apelam constructorul clasei parinte
        super().__init__(nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descrie(self):
        super().descrie()
        print(f"Facultate: {self.facultate}")
        print(f"An de studiu: {self.an_studiu}")

    def anul_absolvirii(self):
        return 2022 + (4 - self.an_studiu)

class Angajat(Person):

    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu

    def descrie(self):
        super().descrie()
        print(f"Companie: {self.companie}")
        print(f"Salariu: {self.salariu}")

    def salariu_anual(self):
        return self.salariu * 12

print(Person.contor_persoane)
person1 = Student("Ion", 21, "London", "UMK", 2)
person1.descrie()
# Metodele comune claselor copii vor fi puse in clase parinte (ca sa nu repetam codul)
print(person1.anul_nasterii())
# Metodele specifice fiecarui copil vor fi puse in clasa copil de care apartin
print(person1.anul_absolvirii())

person2 = Angajat("Lilu", 45, "Valea Prahovei", "Opium", 2456)
print(Person.contor_persoane)
person2.descrie()
print(person2.anul_nasterii())
print(person2.salariu_anual())

