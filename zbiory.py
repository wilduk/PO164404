def z1(a, b):
    og = []
    for x in a:
        for y in b:
            if x == y:
                break
        else:
            og.append(x)
    for x in b:
        for y in a:
            if x == y:
                break
        else:
            og.append(x)
    return set(og)


def z2(a, b, c):
    og = []
    zbiory = [a, b, c]
    for zbior in zbiory:
        for liczba in zbior:
            istnieje = False
            for inny in zbiory:
                if zbior == inny or istnieje:
                    continue
                for liczba2 in inny:
                    if liczba == liczba2:
                        istnieje = True
                        break
            if not istnieje:
                og.append(liczba)
    return set(og)


def z3(a, b, c):
    og = []
    zbiory = [a, b, c]
    for zbior in zbiory:
        for liczba in zbior:
            ile = 0
            for inny in zbiory:
                if zbior == inny or ile > 1:
                    continue
                for liczba2 in inny:
                    if liczba == liczba2:
                        ile += 1
                        break
            if ile == 1:
                og.append(liczba)
    return set(og)


def z4(a):
    og = []
    for i in range(1, 26):
        for liczba in a:
            if i == liczba:
                break
        else:
            og.append(i)
    return set(og)


def z5(a, b, c):
    og = []
    zbiory = [a, b, c]
    for i in range(1, 26):
        for zbior in zbiory:
            for liczba in zbior:
                if i == liczba:
                    break
            else:
                og.append(i)
    return set(og)


def z6(a, b, c):
    og = []
    zbiory = [a, b, c]
    for i in range(1, 26):
        for zbior in zbiory:
            bigbreak = False
            for liczba in zbior:
                if i == liczba:
                    bigbreak = True
                    break
            if bigbreak:
                break
        else:
            og.append(i)
    return set(og)


if __name__ == "__main__":
    set1 = {1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24}
    set2 = {1, 3, 6, 9, 12, 15, 18, 21, 24}
    set3 = {1, 5, 10, 15, 20, 25}
    print(z6(set1, set2, set3))
