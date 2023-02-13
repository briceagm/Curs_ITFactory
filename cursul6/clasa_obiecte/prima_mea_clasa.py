'''
O clasa este un sablon pe care il folosim ca sa creem 'obiecte' din acea clasa.
Obiectele au 2 proprietati importante:
 - caracteristici(pe care in clasa le numim ARIBUTE)
 - metode: adica functii definite in interiorul clasei care ne zic noua ce pot face obiectele
'''


class Person:

    nume = ""
    prenume = ""
    varsta = 0
    inaltime = 0.0
    """
    Metoda speciala init este folosita ca si punct de intrare pentru crearea de obiecte
    """
    def __init__(self, name, first_name, age, height):
        self.nume = name
        self.prenume = first_name
        self.varsta = age
        self.inaltime = height

    '''
    Self este un cuvant cheie care reprezinta obiectul la care ne referim la momentul apelarii metodei
    '''
    def present_me(self):
        print(f"Salut, eu sunt {self.nume} {self.prenume} si am {self.varsta} ani")

    def creste_varsta(self):
        self.varsta += 1

'''
new_person1 si new_person2 sunt OBIECTE create din clasa Person
'''
# new_person1 = Person("Briceag", "Marcela", 26, 1.65)
# new_person2 = Person("Bostan", "Ion", 66, 1.77)
# '''
# deoarece am folosit clasa Person ca si sablon pentru a crea aceste obiecte,
# putem apela metoda present_me pe ambele
# '''
#
# new_person1.present_me()
# new_person2.present_me()
# print()
# new_person3 = Person("Ghita", "Luta", 21, 1.88)
#
# persoane = [new_person1, new_person2, new_person3]
# for pers in persoane:
#     pers.creste_varsta()
#     pers.present_me()