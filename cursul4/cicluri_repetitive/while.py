# WHILE - un ciclu repetitiv, in care nu stim exact numarul de pasi, dar stim ca avem o conditie de indeplinit
# while - cat timp
# while conditie:
#      fa ceva

i = 0
while i < 5:
    print(i)
    i += 1  # daca nu incrementam noi i-ul, programul va crash-ui doarece bucla se va tot repeta pana ramane calculatorul fara memorie

'''
In viata reala vom folosi while atunci cand nu stim exact cat timp trebuie sa executam un cod, dar avem o conditie de oprire. Exemple:
- validarea unui input de la utilizator
- validare user/parola
- pentru a forta un numar maxim de incercari pentru o anumita actiune
'''
age_is_correct = False
while not age_is_correct:
    age = int(input("Varsta dvs:"))
    if 1 < age < 99:
        age_is_correct = True
    else:
        print("Varsta nu este corecta, trebuie sa fie intre 1 si 99, Incercati din nou!")

user, parola = "marcela", "hopapenelopa"
print("NU seunteti logat, trebuie sa va logati")
nr_incercari = 0
nr_max_incercari = 3
'''
While- else functioneaza la fel ca si for-else
!!!!de completat
'''
while nr_incercari < nr_max_incercari:
         my_password = input("Introduceti parola dvs: \n")
         if parola == my_password:
             print("Felicitari, sunteti logat in cont")
             break
         else:
             print("Parola gresita, mai incearca")
         nr_incercari += 1
         print(f"Ai incercat sa te loghezi de  {nr_incercari} ori")
else:
    print("Ai incercat sa te loghezi gresit, nu mai ai voie sa incerci timp de 1 minut!")
print("Am terminat cu logarea")
