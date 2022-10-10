'''
Parametrii (input- datele de intrare in functie) sunt niste nume pe care noi le folosim pentru variabilele pe care le putem transmite functiei!
'''

def say_hello_to(nume):  # variabila nume se numeste PARAMETRU al functiei
    print("Hello, eu sunt functia")
    print(f"Tu esti {nume}")

say_hello_to("Marcela")
say_hello_to("Florian")
say_hello_to("Marian")
print()

def say_goodbye(nume, varsta):
    print(f"Salut, {nume} care ai {varsta} ani!")
    print("Goodbye")

say_goodbye("Ionel", 45)
say_goodbye("Laura", 23)
'''
Parametrii sunt in general pozitionali, adica atunci cand apelam functia, prima valoare va merge in prima variabila, a 2a valoare in a 2a variabila, si tot asa
'''
say_goodbye(52, "Ionel")
say_goodbye(varsta=52, nume="Ionel")
# say_goodbye("Honololu")TypeError: say_goodbye() missing 1 required positional argument: 'varsta
# say_goodbye("IOnel", "Popi", 34) TypeError: say_goodbye() takes 2 positional arguments but 3 were given
'''
Atunci cand pentru anumiti parametri dorim sa avem valori prestabilite(default), putem face asta, punand o valoare direct atunci cand definim functia

def nume_functie(param=valoare):
    etc
    
Daca oferim o valoare prestabilita, atunci parametrul nostru zicem ca este optional.
Adica putem apela cu:

nume_functie() SAU
nume_functie (alta valoare)
'''
def say_hi(nume, mesaj="Acesta este un mesaj standard"):
    print(f"{mesaj}")
    print(f"I-am zis lui MIhai")
    print(f"I-am zis hi lui {nume}")

say_hi("MIha")
say_hi("Mihai", "Alt mesaj")
say_hi("Cineva")

''''
Patrametrii "traiesc" doar in interiorul functiei !!!!
La fel si orice variabila definita in interiorul functiei

'''
#print(nume) o sa dea eroare, nume e definit DOAR in interiorul functiei
# print(contor) o sa dea eroare