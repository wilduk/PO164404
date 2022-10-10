def wypelnij_liste(lista):
    i = 0
    while i  < 10:
        lista.append((i+1)*(i+1))
        i=i+1


lista = []
wypelnij_liste(lista)
print(lista)
