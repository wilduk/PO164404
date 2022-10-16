slownik = {}
while True:
    Input = input()
    if Input == "":
        break
    else:
        if float(int(float(Input))) == float(Input):
            if int(Input) in slownik:
                slownik[int(Input)] += 1
            else:
                slownik[int(Input)] = 1
        else:
            print("liczba "+Input+" nie jest liczbą całkowitą")
print(slownik)
