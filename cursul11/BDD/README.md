## Behaviour Driven Development

### Gherkin

In Gherkin, avem posibilitatea de a translata un user story in sintaxa de test.
Avem 3 pasi principali:
 - Given : ne da starea initiala a sistemului
 - When : actiunile pe care le face utilizatorul
 - Then : aici facem assert, deoarece am ajuns in starea finala a sistemului.

Toate acestea pot fi legate cu `And` si `But`, dar  ATENTIE: acesti pasi iau valoarea "parintelui lor"e.g.
`When ceva And altceva`, inseamna ca `And` devine `When`.

Testele Gherkin stau in fisiere cu extensia `.feature`, iar un astfel de fisier are o structura dupa cum urmeaza:

```gherkin
Feature: numele feature-ului (de exemplu Register User)

   Scenario: numele scenariului de utiliyare (de exemplu Register with succes)
     Given: starea initiala
     When: actiunile utilizatorului
     Then: starea finala(assert)
   
```

Un feature poate avea mai multe scenarii(aproape sigur o sa aiba).
Denumirile date fiecarui scenariu/pass trebuie implementate in Python.
In feature mai putem avea `Background`, `Scenario Outline`.

### Prerequisites(ce trebuie instalat)

Avem nevoie de o librarie de Python care implementeaza sintaxa Gherkin: [behave](https://behave.readthedocs.io/en/stable/)
Mai avem nevoie de selenium si de webdriver-manager, 
si de o librarie pentru formatarea rapoartelor [behave-html-formatter](https://pypi.org/project/behave-html-formatter/)

### Structura unui proiect Gherkin
```
/features
     fisier1.feature
     fisier2.feature
     ```
     environment.py # aici punem anumite setari legate de behave
     /steps
          fisier1.py # aici sunt implementati pasii din fisier1.feature
          fisier2.py
          ```
```

Structura fisierului de python care implementeaza pasii de Gherkin:

```python
from behave import *

@given("nume pas")
def step_impl(context):
     #aici facem logica pasului resepctiv
     pass
     ...
@when("nume pas")
def step_impl(context):
     #aici facem logica pasului resepctiv
     ...

@then("nume pas")
def step_impl(context):
     #aici facem logica pasului resepctiv
     ...
```

Obiectul `context`, este transmis automat de catre `behave` ca parametru la fiecare pas, pentru a ne permite noua sa 
stocam si sa transmitem informatii intre pasi.

#### Generare rapoarte HTML

Este necesar un fisier numit `behave.ini`, care trebuie sa existe in folderul principal al proiectului(pe acelasi nivel 
cu folderul de `features`). In aceste fisier, setam formatorul pentru raport cu urmatoarea sintaxa:

```ini
[behave.formatters]
html = behave_html_formatter:HTMLFormatter
```

Apoi, rulam testele `behave -f html -o nume_raport.html`.

- `-f hmtl` - inseamna ca setam formatul sa fie html
- `-o nume_raport.html` - aici setam numele fisierului de output

Dupa aceea, putem vizualiza fisierul obtinut intr-un browser, si vom vedea rezultatele testelor colorate frumos.

