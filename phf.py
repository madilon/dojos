nume1=input("Salut jucator 1, cum te numesti? ")
nume2=input("Salut jucator 2, cum te numesti? ")
i = "DA"
while i == "DA":
    hpf1 = input(nume1+", alege: hartia, piatra sau foarfeca: ")
    hpf2 = input(nume2+", alege: hartia, piatra sau foarfeca: ")
if hpf1 == hpf2:
    print("Este egalitate!")
elif hpf1 == "piatra":
    if hpf2 == "foarfeca":
        print(nume1+",felicitari! Ai castigat! ")
else:
    print(nume2+",felicitari! Ai castigat! ")
elif hpf1 == "foarfeca":
    if hpf2 == "hartia":
        print(nume1+",felicitari! Ai castigat! ")
else:
    print(nume2+",felicitari! Ai castigat! ")
elif hpf1 == "hartia":
    if hpf2 == "piatra":
        print(nume1+",felicitari! Ai castigat! ")
else:
    print(nume2+",felicitari! Ai castigat! ")
i = input("Joc nou? ")
print("Joc terminat!")