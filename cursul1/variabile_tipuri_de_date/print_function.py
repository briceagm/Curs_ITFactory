varsta = 25
prenume = "Marcela"
nume = "Briceag"

# print este o functie care 'scrie' in consola , dar care asteapta stringuri
print("Pe mine ma cheama " + prenume + " " +  nume)
print("Eu am " + str(varsta) + " ani") #nu putem concatena varsta (int) cu sring, deci trebuie sa facem type casting

#F- strings (formatet strings)
print(f"Pe mine ma cheama {prenume} {nume}  si am {varsta} ani") # este varianta recoamndata de a folosi print
#print(f"ce se intampla {prenume, nume}") #  aici se formeaza o tupla (nu folosim inca acest format)

print(f"Am mai crescut un an, acum am {varsta + 1} ani")

