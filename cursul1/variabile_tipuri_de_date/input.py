# input - functia cu care preluam date de la utilizator (de la tastatura)
# \n = newline , adcia ducem cursorul pe urmatoarea linie, ca sa arate frumos
nume = input("introdu numele:\n")

print(f"Salut, {nume}")

# By default, ce primim noi de la input este INTOTDEAUNA string
varsta = input("cati ani ai? \n")
print(type(varsta))
# daca dorim alte tipuri de date, trebuie sa facem type casting
varsta = int(varsta)
print(type(varsta))

#Exercitiu cu assert si input : cod de captcha
x, y = 5, 17
rezultat_captcha = int(input(f"Cat este {x} + {y}?\n"))
assert rezultat_captcha == x + y, "Nu esti om!"