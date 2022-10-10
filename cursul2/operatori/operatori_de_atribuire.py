a = 10  # operatorul standard de atribuire
a += 2  # echivalentul cu a = a +2
a -= 2  # a = a -2
a *= 2  # a=a*2
a /= 2  # a= a /2  => aici va deveni 10.0 , deoarece impartirea normala are mereu un float
print(a)

a = int(a)
a //= 2 # Operatorul // este pentru impartirea FARA REST (impartirea intreaga)
print(a)

print(7 / 2)  # a printa 3.5
print(7 // 2)  # va printa 3