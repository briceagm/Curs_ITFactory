# Obligatorii
# Ex.1
"""
Funcție care să calculeze și să returneze suma a două numere
"""
print("Exercitiul 1")

def sum_numere(nr1, nr2):
    suma = nr1 + nr2
    return suma

nr1 = int(input("Introduceti primul numar: \n"))
nr2 = int(input("Introduceti al doilea numar: \n"))
print(f"Suma este: {sum_numere(nr1, nr2)}")
print()

# Ex.2
"""
Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""
print("Exercitiul 2")
# atntie la cum alegem numele functiilor
# folosim verbe, incercam sa evidentiem ce o sa returnam si sa fim cat mai clari
def functia_numar(numar):  # este_nr_par
    if numar % 2 == 0:
        return True
    else:
        return False

numar = int(input("Introduceti numarul: \n"))
print(functia_numar(numar))
print()

# Ex.3
"""
Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
print("Exercitiul 3")

def nume_complet(nume, prenume): # lungime_totala
    total_caractere = len(nume) + len(prenume)
    # return len(nume) + len(prenume)
    return total_caractere

print(f"Numarul total de caractere al numelui este: {nume_complet('marcela', 'briceag')}")
print()

# Ex.4
"""
Funcție care returnează aria dreptunghiului
"""
print("Exercitiul 4")

def area_rectangle(width, height):
    area = width * height
    return area

print(f"Aria dreptunghiului este: {area_rectangle(4, 5)}")
print()

# Ex.5
"""
Funcție care returnează aria cercului
"""
print("Exercitiul 5")

def aria_cercului(raza):
    PI = 3.14
    return PI * (raza * raza)
raza = int(input("Introduceti valoare razei: \n"))
print(f"Aria cercului este: {aria_cercului(raza)} cm")
print()

# Ex.6
"""
Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
"""
print("Exercitiul 6")

def caracter_string(string_dat, caracter_cautat):  #is_in_string
    for caracter in string_dat:
        if caracter_cautat in string_dat:
            return True
        else:
            return False
# variabilele definite in afara functiei se numesc GLOBALE
# astfel, avem acces la ele si in interiorul functiei
# DAR nu e ok sa facem asa, si variabilele de care avem nevoie in functie AR TREBUi MEREU
# sa fie transmise [rin parametri
string_dat = input("Introduceti textul dorit: \n")
x = input("Caracterul cautat: \n")
print(caracter_string(string_dat, x))
print()

# Ex.7
"""
Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""
print("Exercitiul 7")
def functie_fara_return(string):
    x = 0
    y = 0
    for caracter in string:
         if caracter.upper() == caracter:
            x += 1
         else:
             y += 1
    print(f"Nr.de caractere upper case este: {x}")
    print(f"Nr de caractere lower case este: {y}")

functie_fara_return("AlaBALAportocaLAa")
print()

# Ex.8
"""
Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""
print("Exercitiul 8")

def lista_numere(list):
    lista_noua = []
    for numar in list:
        if numar > 0:
            lista_noua.append(numar)

    return lista_noua

lista = [-2, 3, -5, 8, -2, 4, 1, -6]
print(f"Lista returnata doar cu numerele pozitive este: {lista_numere(lista)}")
print()

# Ex.9
"""
Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""
print("Exercitiul 9")

def doua_numere(x,y):
    if x == y:
        print("Numerele sunt egale")
    elif x > y:
        print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
    else:
        print(f"Al doilea numar {y} este mai mare decat primul numar {x}")

doua_numere(5, 8)
print()

# Ex.10
"""
Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""
print("Exercitiul 10")

def functia_10(numar, set_de_numere):
     if numar in set_de_numere:
        print("Nu am adaugat numarul in set. Acesta exista deja. ")
        return False
     else:
        set_de_numere.add(numar)
        print("Am adaugat numarul nou in set.")
        return True

numar = int(input("Introduceti numarul: \n"))
set = {1, 7, 9, 8}
print(functia_10(numar, set))
print()

#OPTIONALE
# Ex.2
"""
Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
"""
print("Exercitiul 2 opt.")
# atunci cand returnam mai multe valori dintr-o functie, acestea sunt puse automat intru-un tuple
def calculator(a, b):
    return a+b, a-b, a*b, a/b

rezultat = calculator(4, 12)
print(rezultat)

s, d, p, c = calculator(4, 6)
print(f"Suma: {s}, Diferenta: {d}, Produsul: {p}, Catul: {c}")
print()

# Ex.3
"""
Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""
print("Exercitiul 3 opt.")
def cifre(lista):
    dictionar = {}
    for key in range(10):
        dictionar[key] = lista.count(key)
    return dictionar

lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(cifre(lista))
print()

# Ex.4
"""
Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
"""
print("Exercitiul 4 opt.")

def valoarea_maxima(a, b, c):
    if a >= b and a >= c:
        cel_mai_mare = a
    elif b >= a and b >= c:
        cel_mai_mare = b
    else:
        cel_mai_mare = c
    return cel_mai_mare

a = int(input("Numarul 1: \n"))
b = int(input("Numarul 2: \n"))
c = int(input("Numarul 3: \n"))
print(f"Valoarea maxima dintre cele 3 numere: {valoarea_maxima(a, b, c)}")
print()

# Ex.5
"""
Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""
print("Exercitiul 5 opt.")
def suma_de_numere(numar):
    suma = 0
    for i in range(0, numar+1):
        suma += i
    return suma
valoare = 3
print(f"Suma tuturor numerelor de la 0 la {valoare}: {suma_de_numere(valoare)}")
print()

