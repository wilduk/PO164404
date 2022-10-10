def suma(lista):
    suma = 0
    for liczba,i in enumerate(lista,start=1):
        suma=suma+(liczba*((i%2-0.5)*2))
    return int(suma)


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    print(suma(lista))