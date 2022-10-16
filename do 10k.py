def suma():
    lista = []
    for i in range(2,10001):
        lista.append(i)
    for i in range(2,101):
        for liczba in lista:
            if liczba % i == 0 and not liczba == i:
                lista.remove(liczba)
    print(lista)

if __name__ == "__main__":
    suma()
