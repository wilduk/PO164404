import math


def mult(tab):
    iloczyn = 1
    for i in tab:
        iloczyn = iloczyn * i
    return iloczyn


def mult_ints(tab):
    iloczyn = 1
    for i in tab:
        if isinstance(i, int):
            iloczyn *= i
    return iloczyn


def multiply(*args):
    iloczyn = 1
    for i in args:
        iloczyn *= i
    return iloczyn


def multiply_ints(*args):
    iloczyn = 1
    for i in args:
        if isinstance(i, int):
            iloczyn *= i
    return iloczyn


def make_car(firma, model, **kwargs):
    dictio = {"firma": firma, "model": model}
    for i in kwargs:
        dictio[i] = kwargs[i]
    return dictio


def macierz():
    matrix = []
    for x in range(3):
        matrix.append([])
        for y in range(10):
            matrix[x].append(int(math.pow(y+1, x+1)))
    return matrix


def sumy():
    matrix = []
    i = 1
    for x in range(10):
        matrix.append([])
        for y in range(x+1):
            matrix[x].append(i)
            i+=1
    for x in matrix:
        suma = 0
        for y in x:
            suma += y
        print(suma)
    return matrix


def sum(a, b):
    suma = []
    length = len(a[0])
    if not len(a) == len(b):
        return "down bad"
    for x in range(len(a)):
        if not len(a[x]) == len(b[x]) == length:
            return "down bad"
        suma.append([])
        for y in range(len(a[x])):
            suma[x].append(a[x][y]+b[x][y])
    return suma


def product(a, b):
    row = len(a)
    iloczyn = []
    for x in range(row):
        iloczyn.append([])
        for y in range(row):
            iloczyn[x].append(0)
            if not len(b[x]) == len(a[y]):
                return "down bad"
            for i in range(len(a[x])):
                iloczyn[x][y] += a[x][i]*b[i][y]
    return iloczyn


def multMacierz(a, n):
    iloczyn = []
    for x in range(len(a)):
        iloczyn.append([])
        for y in range(len(a[x])):
            iloczyn[x].append(a[x][y]*n)
    return iloczyn


def transp(a):
    col = len(a)
    row = len(a[0])
    macierz = []
    for i in range(col):
        if not len(a[i]) == row:
            return "down bad"
    for y in range(row):
        macierz.append([])
        for x in range(col):
            macierz[y].append(a[x][y])
    return macierz


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5.5]
    #print(mult_ints(lista))
    assert(mult([3, 5, 7]) == 105)
    assert(mult(range(3, 8, 2)) == 105)
    assert(mult_ints([3, 3.14, 5, "abc", 7]) == 105)
    assert(multiply(3, 5, 7) == 105)
    assert(multiply_ints(3, 3.14, 5, "abc", 7) == 105)
    #print(make_car(firma="BMW", model="B5", kolor="niebieski", rocznik=1995))
    #print(macierz())
    print(sumy())
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #print(sum(a,b))
    #print(product(a,b))
    print(multMacierz(a,5))
    print(transp(a))