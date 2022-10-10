# # Ex.1
"""
Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""
print("Exercitiul 1")
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
if note_muzicale == note_muzicale[0:len(note_muzicale):1]:  # daca lista initiala == lista afisata cu slicing
    note_muzicale = note_muzicale[len(note_muzicale)::-1]   # atunci se inverseaza lista
    print(note_muzicale)

note_muzicale.reverse()
print(note_muzicale)  # lista inversata cu reverse
print()
# Ex.2
"""
De câte ori apare ‘do’?
"""
print("Exercitiul 2")
note_muzicale.count("do")
print(f"'do' apare de {note_muzicale.count('do')} ori")
print()
# Ex.3
"""
Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
"""
print("Exercitiul 3")
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
# prima metoda sa unesti 2 liste
list3 = list1 + list2
print(f"Lista 1: {list1}\nLista 2: {list2}")
print(f"Lista a treia dupa adunarea celor 2 liste: {list3}")
# a doua metoda de a uni 2 liste
list1.extend(list2)
print(f"List 1 este acum modificata: {list1}")
print()
# Ex.4
"""
Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
"""
print("Exercitiul 4")
list3.sort()  # am sortat lista [0, 1, 2, 3, 4, 5, 6]
print(f"Lista sortata: {list3}")

var_pop = list3.pop(0)
print(f"Am scos din lista, de la indicile 0, valoarea: {var_pop}")
print(f"Lista dupa scoaterea valorii 0: {list3}")
print()
# Ex.5
"""
 Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
"""
print("Exercitiul 5")
if len(list3) != 0:  # daca lungimea listei 3 este diferita de 0(adica are elemente)
    print("Lista nu este goala")
else:
    print("Lista este goala")
print()
# Ex.6
"""
Folosește o funcție care să șteargă lista de la exercițiul 3.
"""
print("Exercitiul 6")
list3.clear() # aceasta functie sterge elementele din lista
print(f"Lista actuala dupa stergerea elementelor: {list3}")
print()
# Ex.7
"""
Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""
print("Exercitiul 7")
if len(list3) != 0: # daca lungimea listei 3 este diferita de 0(adica are elemente)
    print("Lista nu este goala")
else:
    print("Lista este goala")
print()
# Ex.8
"""
Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
print("Exercitiul 8")
dict1 = {
    'Ana': 9,
    'Gigel': 10,
    'Dorel': 5
}
print(dict1.keys())
print()
# Ex.9
"""
Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
print("Exercitiul 9")
print(f"Ana a luat nota:{dict1['Ana']}.")
print(f"Gigel a luat nota:{dict1['Gigel']}.")
print(f"Dorel a luat nota:{dict1['Dorel']}.")
print()
# Ex.10
"""
Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
"""
print("Exercitiul 10")
dict1['Dorel'] = 6  # modificam elementul
print(f"Dorel a facut contestatie si a primit nota: {dict1['Dorel']}")
print()
# Ex.11
"""
Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
"""
print("Exercitiul 11")
del dict1['Gigel']  # l-am sters pe Gigel din dictionar
print(f"clasa dupa transferarea lui Gigel {dict1}")
dict1['Ionica'] = 9  # l-am adaugat pe Ionica
print(f"Clasa dupa venirea noului coleg: {dict1}")
print()
# Ex.12
"""
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
"""
print("Exercitiul 12")
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(f"'luni' nu sa adaugat pentru ca deja este in set: {zile_sapt}")
print()
# Ex.13
"""
Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
"""
print("Exercitiul 13")
if weekend.issubset(zile_sapt):
    print(f"{weekend} este un subset al zilelor saptamanii")
else:
    print(f"{weekend} nu este un subset al zilelor saptamanii")
print()
# Ex.14
"""
Afișează diferențele dintre aceste 2 seturi.
"""
print("Exercitiul 14")
print(f"Diferenta dintre cele 2 seturi este: {zile_sapt - weekend} ")

# Ex.15
"""
Afișază intersecția elementelor din aceste 2 seturi.
"""
print("Exercitiul 15")
print(f"Intersectia seturilori: {zile_sapt.intersection(weekend)}")

print('-'*66)
# Optionale
print("Fotbal pe teren sintetic")
jucatori = ["J1", "J2", "J3", "J4", "J5"]
schimbari_efectuate = 0
schimbari_maxim = 3
# am incercat, dar nu am reusit sa ajung la un rezultat bun
# for item in jucatori:
#     if item:
#         if schimbari_maxim > 0 and schimbari_maxim <= 3:
#             print(f"Jucatorul {item} este in teren")
#             print("Efectuam schimbarea")
#             schimbari_maxim -= 1
#             schimbari_efectuate += 1
#             print(schimbari_maxim)
#             print(schimbari_efectuate)
#             jucatori.remove(item)
#             jucatori.append("J6")
#         else:
#             print("Nu mai avem schimbari")
#             break
#     else:
#         print(f"Nu se poate efectua schimbare deoarece jucatorul {item} nu este in teren")
#         print(f"Nu mai ai schimbari")
# print(jucatori)