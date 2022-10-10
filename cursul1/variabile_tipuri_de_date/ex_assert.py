# folosim pentru a verifica pentru o anumita conditie
# daca conditia este adevarata , codul merge mai departe
#daca conditia este falsa, codul se opreste si da eroare
anul_nasterii = 1988
varsta = 32

# verific ca anul nasterii e introdus corect in raport cu varsta
#assert 2022 - anul_nasterii == varsta

anul_nasterii == 2001 == 2001
varsta = 88
#putem pune dupa virgula un mesaj personalizat dde eroare ca sa stim ce nu a mers bine
#assert 2022 - anul_nasterii == varsta, f"Anul nasterii este {anul_nasterii} , si nu se potriveste cu varsta {varsta}"

s1 = "43"
my_int = int(s1)
assert my_int == 43, f"{my_int} nu este in integer egal cu 43"

