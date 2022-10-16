def z1(a, b):
    slowo = ""
    for literaa in a:
        for literab in b:
            if literaa == literab:
                slowo += literaa
                break
    return set(slowo)


def z2(a, b):
    slowo = a + b
    return set(slowo)


def z3(a, b):
    slowo = []
    zdania = [a, b]
    for litera in range(97, 123):
        slowo += chr(litera) + chr(litera).upper()
    for zdanie in zdania:
        for literaa in zdanie:
            for literab in slowo:
                if literaa == literab:
                    slowo.remove(literaa)
                    break
    return set(slowo)


def z4(a, b):
    nieliterya = ""
    nieliteryb = ""
    for litera in a:
        if not litera.isalpha():
            nieliterya += litera
    for litera in b:
        if not litera.isalpha():
            nieliteryb += litera
    return set(nieliterya) & set(nieliteryb)


def z5(a, b):
    nielitery = ""
    for litera in a:
        if not litera.isalpha():
            nielitery += litera
    for litera in b:
        if not litera.isalpha():
            nielitery += litera
    return set(nielitery)


if __name__ == "__main__":
    set1 = "AlaMaKota123"
    set2 = "KotMaAle234"
    print(z5(set1, set2))
