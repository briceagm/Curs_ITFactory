# o tupla este o lista care nu poate fi modificata in nici un fel
# tupla este IMUTABILA ( nu poate fi modificata)
t = ()
tuple1 = (5, 6, 3, 8, -3)
tuple2 = ("Ana", "are", "mere")
tuple3 = (True, False, False, True, False, True)

print(tuple1[1])
# tuple1[1] = 4 # EROARE

print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(tuple1.count(8))