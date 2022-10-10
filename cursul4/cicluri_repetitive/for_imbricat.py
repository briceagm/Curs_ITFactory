# for imbricat -> for in for
hotel = {
    "parter": ["Birou managment", "Toalete oaspeti", 10, 11, 12, 13, 14], # parter
    "etaj 1":[20, 21, 22, 23, 24, 25, 26], # etaj 1
    "etaj2":[30, 31, 32, 33, 34, 35, 36], # etaj 2
   "etj":[42],# ultimul etaj
}

for etaj in hotel:
    print(f"Etaj nou: {etaj}")
    for camera in etaj:
        print(f"  camera {camera}")
print()

# Tabla inmultirii
for i in range(1, 10): # 0,1,2,3,4
    for j in range(1, 10): # 0, 1, 2, 3
        print(f" {i} x {j} = {i*j}")
    print()