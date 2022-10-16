def z1(slowo, znaki):
    slownik = {}
    for znak in znaki:
        slownik[znak] = 0
    for litera in slowo:
        if litera in slownik:
            slownik[litera] += 1
    return slownik


def z2(slowo):
    slownik = {}
    for litera in slowo:
        if litera in slownik:
            slownik[litera] += 1
            continue
        slownik[litera] = 1
    return slownik


def z3(slowo):
    slownik = {}
    for litera in slowo:
        litera = litera.lower()
        if litera in slownik:
            slownik[litera] += 1
            continue
        slownik[litera] = 1
    return slownik


def z4(slowo):
    slownik = {}
    for litera in slowo:
        litera = litera.lower()
        if litera in slownik:
            slownik[litera] += 1
            continue
        slownik[litera] = 1
    max = 0
    maxl = ""
    for litera in slownik:
        ile = slownik[litera]
        if ile > max:
            max = ile
            maxl = litera
    return maxl


if __name__ == "__main__":
    zadania = [z1, z2, z3, z4]
    zad = int(input())
    plik = open("slowniki.txt", "r")
    slowo = plik.read()
    plik.close()
    if not 0 < zad < 5:
        print("nie ma takiego zadania")
    else:
        print(zadania[zad-1](slowo))
