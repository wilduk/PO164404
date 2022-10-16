def equals(a, b):
    if not len(a) == len(b):
        return False
    for i in range(len(a)):
        if not a[i] == b[i]:
            return False
    return True


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(equals(lista, lista2))
