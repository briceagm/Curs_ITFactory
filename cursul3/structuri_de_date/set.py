# Set = structuri de date (colectie) care are doar elemente unice
# seturile sunt bune pentru un singur lucru sa am elemente unice si sa pot verifica daca ceva se afla in elementele acelea

set_gol = {} # nu putem face asa, astae un DIOCtioNAr
set_gol1 = set()
print(set_gol1)

an = {'primavara', 'vara', 'toamna', 'iarna'}
print(an)

an.add('primavara')
print(an)

an.add('ceva')
print(an)

# print(an[0]) # eroare, nu pot accesa un set

# Set membership
anotimp = "vara"
if anotimp in an:
    print("gasit")
else:
    print("nu exista in set")

an.remove('vara')
print(an)

if anotimp in an:
    print("gasit")
else:
    print("nu exsita in set")

print(f"lungimea setului este {len(an)}")

