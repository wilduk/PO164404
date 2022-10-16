plik = open("wypiszileliczb.txt", "r")
linijki = plik.readlines()
slownik = {}
for linia in linijki:
    slowa = linia.split()
    for slowo in slowa:
        if slowo.isdecimal():
            if slowo in slownik:
                slownik[slowo] += 1
            else:
                slownik[slowo] = 1
plik.close()
print(slownik)
