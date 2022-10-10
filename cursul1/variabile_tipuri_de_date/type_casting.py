#aceset 2 variabile sunt de tipul string
sir1 = "42"
sir2 = "True"

print(type(sir1))  # adica string
print(type(sir2))
#CTRL +D se copiaza randul si se afiseaza unde e cursorul

# type casting - formam conversia unuei variabile de la un tip la altul
# sir1 -> il convertim de la string la int (sau la float)
my_int = int(sir1)
# my_int este creat din valoarea pe care o avem la sir1, DAR sir1 nu se modifica, si nici nu isi modifica tipul
print(sir1, type(sir1))
print(my_int, type(my_int))

sir1 = int(sir1)  # acum am modificat sir1 prin suprascriere (sir1 acum este int)

my_bool = bool(sir2)
print(sir2, type(sir2))
print(my_bool, type(my_bool))

#string-> float
sir3 = "42"
my_float = float(sir3)
print(sir3, type(sir3))
print(my_float, type(my_float))

#Int -> float
another_float = float(my_int)
print(another_float, type(another_float))

#INt -> bool
adevarat = bool(5)  #orice valoare diferita de 0 este considerat adevarat
fals = bool(0)
print(adevarat, type(adevarat))
print(fals, type(fals))

#Toate variabilele se pot converti in string
my_string = str(another_float)
print(my_string, type(my_string))
