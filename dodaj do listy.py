def suma():
    slen = len(lista)
    for i in range(10-slen):
        while True:
            input_a = input()
            input_a = int(input_a)
            if input_a not in lista:
                lista.append(input_a)
                break


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    suma(lista)
    print(lista)
