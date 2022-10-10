'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
'''
def get_numere_pare(lista_nr):
    noua_lista = []
    for nr in lista_nr:
        if nr % 2 == 0:
            noua_lista.append(nr)
    return noua_lista

def get_numere_pozitive(lista_nr):
    noua_lista = []
    for nr in lista_nr:
        if nr > 0:
            noua_lista.append(nr)
    return noua_lista


alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = get_numere_pare(alte_numere)
print(f"Numerele pare sunt: {numere_pare}")
numere_pozitive = get_numere_pozitive(alte_numere)
print(f"Numerele pozitive sunt: {numere_pozitive}")
print()

'''
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333
'''
def piramida(numar):
    for i in range(1, numar + 1):
        print(f"{i}"* i)

numar_piramida = int(input("Introduceti numarul: \n"))
piramida(numar_piramida)