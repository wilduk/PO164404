def nwd(p, q):
    reszta = p % q
    if reszta == 0:
        return q
    return nwd(q, reszta)


class Wymierna:
    p: int
    q: int

    def __init__(self, p=0, q=1) -> None:
        dzielnik = nwd(p, q)
        self.p = p//dzielnik
        self.q = q//dzielnik

    def get_licznik(self):
        return self.p

    def get_mianownik(self):
        return self.q

    def __repr__(self):
        return str(self.p/self.q)

    def __float__(self):
        return self.p/self.q

    def __int__(self):
        return self.p//self.q

    def __add__(self, other):
        return Wymierna(self.p*other.q+other.p*self.q, self.q*other.q)

    def __sub__(self, other):
        return Wymierna(self.p*other.q-other.p*self.q, self.q*other.q)

    def __eq__(self, other):
        liczba1 = self.p/self.q
        liczba2 = other.p/other.q
        if not liczba1 > liczba2 and not liczba1 < liczba2:
            return True
        return False

    def __ne__(self, other):
        if self.p == other.p and self.q == other.q:
            return False
        return True

    def __lt__(self, other):
        if self.p/self.q < other.p/other.q:
            return True
        return False

    def __le__(self, other):
        if self.p/self.q <= other.p/other.q:
            return True
        return False

    def __gt__(self, other):
        if self.p/self.q > other.p/other.q:
            return True
        return False

    def __ge__(self, other):
        if self.p/self.q >= other.p/other.q:
            return True
        return False

    def __mul__(self, other):
        if type(other) == int:
            return Wymierna(self.p * other, self.q)
        return Wymierna(self.p * other.p, self.q * other.q)

    def __truediv__(self, other):
        if type(other) == int:
            return Wymierna(self.p, self.q*other)
        return Wymierna(self.p * other.q, other.p * self.q)


if __name__ == "__main__":
    jeden = Wymierna(1, 2)
    dwa = Wymierna(2, 4)
    print("%d %d" % (jeden.get_licznik(), jeden.get_mianownik()))
    print("%d %d" % (dwa.get_licznik(), dwa.get_mianownik()))
    print("%0.0f" % (float(jeden + dwa)))
    print("%0.2f %0.2f" % (float(jeden * dwa), float(jeden / dwa)))
    print("%0.2f %0.2f" % (jeden * 2, jeden / 2))
    assert(jeden == dwa)
