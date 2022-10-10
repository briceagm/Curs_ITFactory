# if conditie1:
#     fa ceva daca conditie1 este adevarat
# elif conditie2:
#     fa ceva daca conditie2 ese adevarata
# elif conditie3:
#     fa ceva daca cond3 este adevarata
# else:
#     fa ceva daca nici o conditie de pana acum nu a fost adevarat

varsta = int(input("varsta:\n"))
if varsta <= 2:
    print("esti bebelus")
elif varsta <= 12:
    print("esti copil")
elif varsta <= 18:
    print("esti adolescent")
elif varsta <= 65:
    print("esti adult")
else:
    print("esti pensionar")

#if in if
# if este_lapte:
#     if este_zuzu:
#         cumpara zuzu
#     else:
#         cumpara orie este
# else:
#     asta este, nu mai cumpara nimic

if varsta > 18:
    print("esti major")
    if varsta > 65:
        print("adult")
    else: # varsta mai maica decat 65 si mai mare decat 18
        print("adult")
else:
    print("esti minor")
    if varsta <= 2:
        print("bebelus")
    elif varsta <= 12:
        print("copil")
    else:
        print("adolscent")