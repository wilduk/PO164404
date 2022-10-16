plik = open("wypiszileliter.txt", "r")
slowo = plik.read()
slownik = {}
for litera in slowo:
    if not litera == "\n" and litera.isalpha():
        if litera in slownik:
            slownik[litera] += 1
        else:
            slownik[litera] = 1
plik.close()
print(slownik)
