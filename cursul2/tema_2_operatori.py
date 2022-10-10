#OBLIGATORII
#  Ex.1
# Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
# else.
"""
if else = evalueaza conditii si bifurca codul in functie de rezultat
  if conditie:
        fa ceva
        daca conditia este
        adevarata
 else:
      fa altceva
      daca conditia nu este adevarata
"""
# Ex. 2
"""
Verifică și afișează dacă x este număr natural sau nu.
"""
print("Exercitiul 2")
x = int(input("Introdu numarul x:\n"))
if x > 0:
    print("Numarul este natural")
else:
    print("Numarul nu este natural")
print()
# Ex. 3
"""
Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
print("Exercitiul 3")
if x >= 1:
    print("Numarul este pozitiv")
    if x == 1:
        print("Numarul este neutru pentru inmultire")
elif x < 0:
    print("Numarul este negativ")
elif x == 0:
    print("Numarul este neutru pentru adunare")
print()
# Ex. 4
"""
Verifică și afișează dacă x este între -2 și 13.
"""
print("Exercitiul 4")
if (x >= -2 and x <= 13):
    print("X se afla intre -2 si 13")
else:
    print("X nu se afla intre -2 si 13")
print()
# Ex. 5
"""
Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
print("Exercitiul 5")
y = int(input("Introduceti numarul y:\n"))
if (x - y < 5):
    print("Diferenta dintre x si y este mai mica decat 5")
else:
    print("Diferenta dintre x si y  este mai mare decat 5 ")
print()
# Ex. 6
"""
Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
"""
print("Exercitiul 6")
if x not in range(5, 27):
    print("Numarul  nu se afla in intervalul 5-27")
else:
    print("Numarul  se afla in intervalul 5-27")
print()
# Ex. 7
"""
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
"""
print("Exercitiul 7")
if x == y:
    print("Numerele sunt egale")
elif x > y:
    print("X este mai mare ")
elif x < y:
    print("Y este mai mare ")
print()
# Ex. 8
"""
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""
print("Exercitiul 8") # nu am reusit sa obtin rezultatul corect
X = int(input("Introduceti latura X:\n"))
Y = int(input("Introduceti latura Y:\n"))
Z = int(input("Introduceti latura Z:\n"))

if X == Y == Z:
    print("Triunghiul este echilateral")
elif X == Y or X == Z or Y == Z:
    print("Triunghiul este isoscel")
else:
   print("Triunghi oarecare")

# Ex.9
"""
Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu
"""
print("Exercitiul 9")
litera = input("Introduceti litera: \n")
if litera in {"a", "e", "i","o", "u", "ă", "î"}:
    print(f"Litera {litera} este o vocala")
else:
    print(f"Litera {litera} este consoana")
print()

