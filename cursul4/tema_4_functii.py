#  EXERCITII OBLIGATORII
#  Ex.1
"""
Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""
print("Exercitiul 1")
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

print("Rezolvat cu for")
for i in range(len(masini)):  # for simplu cu range (i se foloseste de obicei cand avem un numar)
    # if masini[i] == 'Mercedes':
        print(f"{i}: masina mea preferata este: {masini[i]} ")

print()
print("Rezolvat cu for-each")
for masina in masini:
    # if masina == "Mercedes":
        print(f"Masina preferata este: {masina}")
print()
print("Rezolvat cu while")
i = 0
while i < len(masini):
    # if masini[i] == 'Mercedes':
    print(f"Masina mea preferata este: {masini[i]}")
    i += 1 #incrementare
print()
#Ex.2
"""
Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista
"""
print("Exercitiul 2")
for i in range(0, len(masini)):
    if i == 0 or i == len(masini)-1:
        continue

    masini[i] = masini[i].upper()
print(f"Lista scrisa cu majuscule: {masini}")
print()

# Ex.3
"""
Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
print("Exercitiul 3")
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina_dorita = 'Volvo'
for masina in masini:
    # print(f"Acum cautam in lista de masini '{masina}'...")
    if masina == masina_dorita:
        print("Am gasit masina dorita de dvs! ")
        break
    else:
        print(f"Am gasit masina '{masina}'. Mai cautam...")
print()

# Ex.4
"""
Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""
print("Exercitiul 4")
for masina in masini:
    if masina == "Lastun" or masina == 'Trabant':
        continue
    print(f"S-ar putea sa va placa masina {masina}")
print()

# Ex.5
"""
Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
"""
print("Exercitiul 5")
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)):
    if masini[i] == "Lastun" or masini[i] == "Trabant":
        masini_vechi.append(masini[i])
        masini[i] = "Tesla"
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")
print()

#Ex.6
"""
Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
"""
print("Exercitiul 6")
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000,
}
buget = 15000
print(pret_masini.items())
# for masina in pret_masini:
#     if buget >= pret_masini[masina]:
#         print(f"Masina {masina} cu pretul {pret_masini[masina]} se incadreaza in bugetul clientului")
for marca, pret in pret_masini.items():
    if buget >= pret:
        print(f"Pentru un buget de sub {buget} euro puteti alege masina {marca}")
print()
#Ex.7
"""
Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
print("Exercitiul 7")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
counter = 0
for numar in numere:
    if numar == 3:
        counter += 1
print(f"Cifra 3 apare de: {counter} ori")
print()

#Ex.8
"""
Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
print("Exercitiul 8")
suma = 0
for numar in numere:
    suma += numar
print(f"Suma numerelor este {suma}")
print()

# Ex. 9
"""
Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""
print("Exercitiul 9")
max = -999
# max = numere[0] pentru a fi mai siguri
for numar in numere:
    if max < numar:
        max = numar
print(f"Cel mai mare numar este: {max}")
print()

# Ex.10
"""
Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""
print("Exercitiul 10")
numere_nou = []
for numar in numere:
    if numar > 0:
        numar = -numar
        numere_nou.append(numar)
    else:
        numere_nou.append(numar)
print(f"Lista noua este: {numere_nou}")
print()

# OPTIONALE
# Ex.1
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""
print("Exercitiul 1 opt.")
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
         numere_pare.append(numar)
    else:
         numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f"Lista numerelor pare este: {numere_pare}")
print(f"Lista numerelor impare este: {numere_impare}")
print(f"Lista numerelor pozitive este: {numere_pozitive}")
print(f"Lista numerelor negative este: {numere_negative}")
