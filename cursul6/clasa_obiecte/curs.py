from prima_mea_clasa import Person

"""
Clasa este un concept, o suma de caracteristici (atribute) si actiuni (metode).
"""
class CursProgramare:

    def __init__(self, compania, nume, durata, data_inceput, nr_locuri=10):
        self.compania = compania
        self.nume = nume
        self.durata = durata
        self. data_inceput = data_inceput
        self.nr_locuri_disponibile = nr_locuri
        self.studenti = []

    def inscriere_student(self, student):
        # Aici am putea de exemplu sa verificam daca a trecut data de inceput, si daca nu, sa inscriem studentul
        if self.nr_locuri_disponibile > 0:
            self.studenti.append(student)
            self.nr_locuri_disponibile -= 1
            print(f"Studentul {student.nume} {student.prenume} a fost inscris cu succes!")
        else:
            print("Nu mai sunt locuri disponibile")

    def descriere_curs(self):
        print(f"{self.nume} [{self.compania}] - {self.durata} zile")
        print("-"*80)
        for student in self.studenti:
            print(f"{student.nume} {student.prenume} ({student.varsta})")
        if not self.studenti:
            print("NU sunt inca studenti")
        print()

curs_python = CursProgramare("IT Factory", "Introducere in Python", 120, "2023-01-02")
curs_python.descriere_curs()

student1 = Person("Marcela", "Briceag", 22, 1.62)
student2 = Person("Florin", "Voda", 27, 1.78)

curs_python.inscriere_student(student1)
curs_python.inscriere_student(student2)
print()

curs_python.descriere_curs()

curs_python.inscriere_student(
    Person("Vladut", "Anastase", 45, 1.89)
)
curs_python.inscriere_student(
    Person("Maria", "Popovici", 33, 1.67)
)
curs_python.descriere_curs()