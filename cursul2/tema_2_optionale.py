#Optionale
# ex.1
"""
Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
# Eu am facut cu string dar cum se face cu int, cum se verifica ca x- int are minim 4 cifre?
x_ = 25
x_transform = str(x_)
if len(x_transform) >= 4:
    print("X are minim 4 cifre")
else:
    print("X nu are minim 4 cifre")

# ex 2
"""
Verifică dacă x are exact 6 cifre.
"""
if len(x_transform) == 6:
    print("X are exact 6 cifre")
else:
    print("X nu are exact 6 cifre")
print()
# ex 3
"""
Verifică dacă x este număr par sau impar (x e int).
"""
if x_ % 2 == 0:
    print("Numar par")
else:
    print("numar impar")
print()
# ex 4
"""
x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
x, y, z = 3, 2, 5
print(max(x,y,z))
print()
# ex 5
"""
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
6. Având stringul: 'Coral is either the stupidest animal or the smartest
"""
if (x + y <= z) or (x + z <= y) or (y + z <= x):
    print(" Triunghi Valid")
else:
    print(" Triunghi Invalid")
print()

# ex 6
"""
Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
string1 = "Coral is either the stupidest animal or the smartest rock"
X = int(input("Puneti x: \n"))
size = string1[: - int(x)]
print(size)
print(string1[-5])
print(string1[0:len(string1):1])
print(string1[len(string1)::-1])
print()
# ex 7
"""
Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5
"""
new_string = string1[0:5:1] + " " + string1[len(string1)-5::1]
print(new_string)
print()
# ex 8
"""
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
"""
var_index = string1.index("rock")
print(var_index)
print(string1[0:var_index:1])
print()
# ex9
"""
Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
"""
string2 = "apA ceburascA"
print(string2[0])
print(string2[len(string2)-1])
print(string2[-1])

assert string2[0].lower() == string2[-1].lower(), f"Nu sunt egale"
print()
# ex 10
"""
Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
"""
string3 = "0123456789"
print(string3[0::2])
print(string3[1::2])
print()