def z1(lista):
    a = lista[0]
    b = lista[len(lista)-1]
    lista[0] = b
    lista[len(lista)-1] = a


def z2(lista):
    a = lista[len(lista)-1]
    for i in range(-1, -len(lista), -1):
        lista[i] = lista[i-1]
    lista[0] = a


def z3(lista):
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            lista[i] = 0


def z4(lista):
    for i in range(1, len(lista)-1, 2):
        if lista[i] > lista[i+1]:
            lista[i+1] = lista[i]
        else:
            lista[i] = lista[i + 1]


def z5(lista):
    if len(lista)%2 == 1:
        lista.pop(int(len(lista)/2))
    else:
        lista.pop(int(len(lista)/2))
        lista.pop(int(len(lista)/2))


def z6(lista):
    parzyste = []
    nieparzyste = []
    for liczba in lista:
        if liczba % 2 == 0:
            parzyste.append(liczba)
        else:
            nieparzyste.append(liczba)
    lista.clear()
    lista += parzyste + nieparzyste


def z7(lista):
    clone = lista.copy()
    max: int
    for i in range(2):
        max = clone[0]
        for liczba in clone:
            if liczba > max:
                max = liczba
        clone.remove(max)
    return max


def z8(lista):
    max = lista[0]
    for liczba in lista:
        if liczba < max:
            return False
        max = liczba
    return True


def z9(lista):
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            return True
    return False


def z10(lista):
    for x in range(len(lista)):
        for y in range(len(lista)):
            if lista[x] == lista[y] and not x == y:
                return True
    return False


if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10]
    z7(lista)
    print(z10(lista))
