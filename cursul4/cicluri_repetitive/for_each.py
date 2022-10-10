note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# for idx in range(len(note_muzicale)):
#     print(f" La indexul {idx} am gasit nota muzicala {note_muzicale[idx]}")
# print()  # pentru spatiu
#
# # For each
# # for element in colectie:
# #     facem ceva cu elementul respectiv
# # unde colectie = lista, set, dictionar, tupla
#
# for  nota in note_muzicale:
#     print(f"NOta curenta este: '{nota}'")
# print()
#
# # vreau sa aflu de cate ori apare nota do in lista, fara sa folosesc count.
# count_do = 0
# for nota in note_muzicale:
#     print(f"Acum testez nota '{nota}'...")
#     if nota == "do":
#         count_do += 1
#         print(f"    am gasit un 'do' controlul a ajuns acum la- {count_do}")
# print()
# print(f"Am gasit nota 'do' in lista de note muzicale de- {count_do} ori!")

'''
Problema: vreau sa gasesc cu nota x primita de la utilizator) in note muzical.
Daca o gasesc, vreau sa ma opresc prima data cand am gasit-o.
Daca nu exista in lista, vreau sa afisez ca nu exista.
'''
# break - for-ul se opreste automat cand intalneste un break, chiar daca mai existau elemente in colectie
# nota_cautata = input("INtroduceti nota cautata: \n")
# gasit = False  #flag pentru a sti daca am gasit ceea ce cautam sau nu
#
# for nota in note_muzicale:
#     print(f"Acum testam nota '{nota}'...")
#     if nota == nota_cautata:
#         print("AM gasit nota cautata de dvs! ")
#         gasit = True
#         break
# if not gasit:
#     print("Nu am gasit deloc nota cautata de dvs")
#
# print("AM terminat bucla de cautare")

# varianta 2 pentru problema de mai sus
nota_cautata = input("INtroduceti nota cautata: \n")

for nota in note_muzicale:
    print(f"Acum testam nota '{nota}'...")
    if nota == nota_cautata:
        print("AM gasit nota cautata de dvs! ")
        break
else:
    # aici se ajunge doar daca for-ul a ajuns la final fara sa dea de vreun break
    print("Nu am gasit nota cautata")

'''
For- else
Atunci cand folosim brek intr=un for, putem avea si o ramura else pentru for, care va fi executate DOAR DACA for-ul a rulat fara sa ajunga deloc la break.
'''
# Vreau sa printez toate notele muzicale mai putin cele care incep cu 'S'
print("Notele muzicale care nu incep cu s sunt:")
for nota in note_muzicale:
    if nota[0] == 's':
        # sari peste aceasta nota. nu vreau sa o printez, incepe cu s
        continue
    print(nota)

# vreau sa afisez numerele mai mici ca 10 care nu sunt divizibile cu 3
for index in range(10):
    if index % 3 == 0:
        continue
    print(f"NUmarul {index} nu este divizibil cu 3!")

