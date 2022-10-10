def wypelnij_liste(lista):
    for i in range(10):
        lista.append(i%2)


lista = []
wypelnij_liste(lista)
print(lista)
