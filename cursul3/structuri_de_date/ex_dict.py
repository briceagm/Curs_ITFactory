from pprint import pprint    # afiseaza textul frumos
# dictionar : o structura de date care stocheaza informatii in perechi Key- Value
# unde cheile actioneaza ca si indicii de la lista, adica ne permit sa ne referim la valori bazat pe chei
dict_gol = {}
dict_1 = {
    "s": 12,
    3: 45,
    3.14: " un alt string"
}
tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": ["hrisca", "amaranth"],
    "galben": "quinoa",
    "alb": "porumb",
    # "rosu": "amaranth"
}
# cheile din dictionar trebuie sa fie unice
# cheile trebuie sa fie tiouri de date simple (int, float, bool, string)
print(f"In vagonul rosu avem { tren_colorat['rosu'] }")
print(f" In vagonul albastru avem { tren_colorat ['albastru'][0]} si { tren_colorat['albastru'][1]}")

# Exemplu: vreau sa vad de cate ori apare o litera anume intrun text
cuvant = "abracadabra"
# daca facem asa, vo avea nevoie de 26 de variabile....cam multe
litera_a_cnt = cuvant.count("a")
litera_b_cnt = cuvant.count("b")

# Facem un dictionar in care key este litera cautata, iar value este de cate ori apare in text
dict_litere_cnt = {
    "a": cuvant.count("a"),
    "b": cuvant.count("b"),
    "r": cuvant.count("r"),
}
print(dict_litere_cnt)

# Exemplu: grupare date in mod logic
student_name = "Briceag"
student_fistname = "Lolita"
student_age = 23
student_weight = 50.1

student = {
    "name": "Briceag",
    "firstname": "Lolita",
    "age": 23,
    "weight": 50.1,
    "birthdate": {
        "day": 26,
        "month": "May",
        "year": 2000
    }
}
print(f"Ma cheama {student['name']} {student['firstname']}. "
      f"Am {student['age']} ani si {student['weight']} kg.")

print(f"M-am nascut pe {student['birthdate']['year']} {student['birthdate']['month']} {student['birthdate']['day']} ")
birthdate = student['birthdate']
print(f"M-am nascut pe {birthdate['day']} {birthdate['month']} {birthdate['year']}")

# operatii pe dictionare
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": "hrisca",
    "galben": "quinoa",
    "alb": "porumb",
    "negru": "amaranth"
}

# adaugare element: folosim o cheie care nu mai exista, si elementul e adaugat
tren_colorat['roz'] = "naut"
print(tren_colorat)

# stergere element
del tren_colorat['roz']
print(tren_colorat)

# Modificare element
tren_colorat['rosu'] = "pietre"
print(tren_colorat)
# pentru a "schimba" Key, trebuie de fapt sa adaugam un nou element cu noua cheie, si sa o stergem pe cea veche
pietre = tren_colorat['rosu']
del tren_colorat['rosu'] # va sterge pietre
tren_colorat['turcuoaz'] = "pietre"
print(tren_colorat)

# Values se pot repeta, nu trebuie sa fie unice
tren_colorat['maro'] = "orz"
tren_colorat['magenta'] = "orz"

# Daca key nu este in dictionat , cu adresare directa vom primi eroare
print(tren_colorat)
# print(tren_colorat['portocaliu'])  # EROARE, nu este nici un vagon portocaliu
if 'portocaliu' in tren_colorat:  # pot testa daca o Key este in dictionar sau nu
    print(tren_colorat['portocaliu'])
else:
    print("nu este nici un vagon portocaliu")

# pprint = pretty print
pprint(tren_colorat)