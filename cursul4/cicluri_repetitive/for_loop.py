# For- ciclu repetitiv in care eu stiu exact numarul de pasi efectuati de la inceput
# for index in range(nr):
#    fa ceva de nr

# functia range(x) ne ofera pe rand, toate numerele de la 0 la x - 1 inclusiv

#0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
print(list(range(10)))
for index in range(10):
    print(f"Index are acum valoarea {index}")

print("Am terminat prima bucla repetitiva! \n")

for idx in range(3, 7):
    print("Acum invat sa numar de la 3 la 7")
    print(f"  am ajuns la {idx}")

print("Am terminat a doua bucla repetitiva! \n")

# 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print("Acum invat sa numar din 2 in 2")
    print(f"  am ajuns la {i}")
print("Am terminat a 3-a bucla repetitiva! \n")

x = 55
print(f"X este initial {x}")
# pentru X de la 0 la 2
for x in range(3):
    print(f"X este acum {x}")
print(f"X este la final {x}")
'''
Putem declara indexul din for si inaintea for-ului, dar acesta va fi suprascris cu ultima valoare obtinuta din for.
'''
x = 0
print(f"x este acum {x}")
x = 1
print(f" x este acum {x}")

nr_zile_sapt = 7
for i in range(1, nr_zile_sapt + 1):
    if i == 1:
        print(f"Este prima zi din saptamana!")
    else:
        print(f"Este a {i}-a zi din saptamana!")

