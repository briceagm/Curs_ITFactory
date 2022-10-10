# Ex.4
"""
Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""
print("Exercitiul 4")
class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul: {self.iban} suma de: {self.sold} lei")

    def debitare_cont(self):
        suma = float(input("Introduceti suma dorita extragerii: \n"))
        self.sold -= suma
        print(f"Ati extras din cont: {suma} lei")
        print(f"Soldul contului este: {self.sold} lei")
    def creditare_cont(self):
        suma = float(input("Introduceti suma dorita depunerii: \n"))
        self.sold += suma
        print(f"Suma depusa de dumneavoastra este: {suma} lei")
        print(f"Soldul contului este: {self.sold} lei")

cont1 = Cont("RO345678900", "Maria Plamadeala", 3400)
cont1.afisare_sold()
cont1.debitare_cont()
cont1.creditare_cont()
print()
cont2 = Cont("RO569023871", "Viorica Nasture", 6789)
cont2.afisare_sold()
cont2.debitare_cont()
cont2.creditare_cont()