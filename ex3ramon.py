cuvant = input("Introdu cuvantul tau: ")
cuvant_invers = cuvant[::-1] #::-1 citeste string-ul invers (de la dreapta la stanga)

if cuvant == cuvant_invers:
     print("Cuvantul " + cuvant + " este palindrom ")

else:
    print("Cuvantul " + cuvant + " nu este palindrom")