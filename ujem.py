def ile_ujemnych(lista):
    ile = 0
    for liczba in lista:
        if liczba < 0:
            ile = ile + 1
    return ile


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5]
    print(ile_ujemnych(lista))
