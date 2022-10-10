# Ex.3
"""
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
print("Exercitiul 3")
class Angajat:
    # Toti parametrii constructorului(in afara de self) reprezinta atributele cu care construim un obiect
    def __init__(self, nume, prenume, salariu, cim=True):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.cim = cim

    def descrie(self):
        print("-"*25)
        print(f"Angajat: {self.nume} {self.prenume}")
        print(f"Salariu: {self.salariu} lei")
        if self.cim:
            print(f"Contract: CIM")
        else:
            print(f"Contract: PFA/SRL")
    print()

    def nume_complet(self):
        print(f"Nume complet: {self.nume} {self.prenume}")

    def salariu_lunar(self):
        print(f"Salariu lunar: {self.salariu}")

    def salariu_anual(self):
        print(f"Salariul anual: {self.salariu * 12}")

    def marire_salariu(self, procent):
        # daca facem o marire de salariu, trebuie sa modificam self.salariu
        # altfel, imediat dupa apelarea metodei, noul salariu se pierde
        self.salariu += (procent * self.salariu) / 100
        return self.salariu

angajat1 = Angajat("Vasile", "Motilica", 2300, cim=False)
print("Angajat nr.1")
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()

# Daca dam print la o functie care nu returneaza nimic, va printa None
print(f"Salariul dupa marire: {angajat1.marire_salariu(15)}")
print()
angajat2 = Angajat("Marinela", "Boboc", 1880)
print("Angajat nr.2")
angajat2.descrie()
angajat2.nume_complet()
angajat2.salariu_lunar()
angajat2.salariu_anual()
print(f"Salariul dupa marire: {angajat2.marire_salariu(10)}")
print()