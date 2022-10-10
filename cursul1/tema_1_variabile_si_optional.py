# Ex.1 variabila - zona din memorie care tine date

# Ex.2
"""
Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
"""
print("Exercitiul 2")
floare = "trandafir"  #string
anul_nasterii = 2005  #int
bani_cash = 245.6     #float
soare_afara = True    #bool
print()
# Ex.3
"""
Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
"""
print("Exercitiul 3")
print(type(floare))
print(type(anul_nasterii))
print(type(bani_cash))
print(type(soare_afara))
print()
# Ex.4
"""
Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
"""
print("Exercitiul 4")
rounded_number = round(bani_cash) #am rotunjit float-ul
bani_cash = round(bani_cash)  #suprascriere
print(bani_cash)
print(type(bani_cash)) # acum bani_cash a devenit int
print()
# Ex.5
"""
Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""
print("Exercitiul 5")
print(f"Am primit cadou, un {floare}.")
print(f"Mateo s-a nascut in anul: {anul_nasterii}.")
print(f"Au cheltuit pe distractii: {bani_cash} lei.")
print(f"Mergem la plaja. {soare_afara}") #nu stiu cum sa rezolv

# Ex.6
"""
Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""
print("Exercitiul 6")
numele = "Carolina"
prenumele = "Raiu"
print(f"Numele complet are: {(len(numele) + len(prenumele))} caractere.")
print()
# Ex.7
"""
Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
"""
print("Exercitiul 7")
lungimea = 7
latimea = 5
aria_dreptunghiului = latimea * lungimea
print(f"Aria dreptunghiului este: {aria_dreptunghiului}.")

#Ex.8,9
"""
8.Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
celași string.
9.● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
"""
mesaj = "Coral is either the stupidest animal or the smartest rock"
print(f"Cuvantul  apare de: {mesaj.count(' the ')} ori")
print()

#Exercitii optionale
#Ex.1
"""
Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc
"""
print("Exercitiul 1 opt.")
# nume = input("Introduceti numele: \n")
nume ='Marcela'
if len(nume) % 2 == 1:
    print(f"Dimensiunea stringului este impara")
    print(nume[int(len(nume) / 2)])
else:
    print(f"Dimeniunea stringului este para")

#Ex.2
"""
Folosind assert, verifică dacă un string este palindrom.
"""
print("Exercitiul 2 opt.")
palindrom = 'madam'
print(palindrom)
print(palindrom[::-1])
assert palindrom == palindrom[::-1], f"{palindrom} este palindrom"
print()
# Ex.3
"""
Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""
# string_tastatura = input("Introduceti de la tastatura")
string = "alabala portocala"
a, b = "alabala", "portocala"
# print(a, b)

# Ex.4
"""
Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""
print("Exercitiul 4 opt.")
string1 = "alabala portocala"
primul_caracter = string1[0]
for i in range(0, len(string1)):
    if primul_caracter == string1[i]:
        majuscula = string1[i].upper()
        inlocuire = string1.replace(string1[i], majuscula)
print(string1[0] + inlocuire[1:-1] + string1[-1])
print()
# Ex.5
"""
Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""

user = 'Marcela'
parola = '1111'
print(f'Parola pentru user {user} este {parola.replace(parola,"****")} si are {len(parola)} caractere')


#verificare tema
#Asta merge doar daca avem un singur nume si un singur prenume
#nume, prenume = input (Introduceti numele si prenumele separate de spatii: