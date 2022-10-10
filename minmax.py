def minmax(lista):
    min = lista[1]
    max = lista[1]
    for liczba in lista:
        if liczba < min:
            min = liczba
        if liczba > max:
            max = liczba
    return (min,max)


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    print(minmax(lista))