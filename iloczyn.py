def iloczyn(lista):
    ile = 1
    for liczba in lista:
        ile = ile * liczba
    return ile


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    print(iloczyn(lista))
