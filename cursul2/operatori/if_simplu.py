#IF - daca
# if conditie:
#     fa ceva
#     mai fa ceva
#     si inca ceva
# aici nu mai sunt in blocul IF
varsta = int(input("varsta:\n"))

print("Urmeaza sa facem un if")
if varsta < 18:
    print("ESti minor")
    print(f"Ai doar {varsta} ani")
print("AM terminat if")

# exemplul 2 _verificare nota de trecere
nota = int(input("ce nota ai luat?\n"))
if nota > 4:
    print("zfelicitari, ai trecut")
print(f"Ai luat nota {nota}")


