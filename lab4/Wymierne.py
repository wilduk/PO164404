from typing import Union


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

    def get_licznik(self) -> int:
        return self.p

    def get_mianownik(self) -> int:
        return self.q

    def __repr__(self) -> str:
        return str(self.p/self.q)

    def __float__(self) -> float:
        return self.p/self.q

    def __int__(self) -> int:
        return self.p//self.q

    def __add__(self, other: Union['Wymierna', int]) -> 'Wymierna':
        if type(other) == int:
            return Wymierna(self.p+other*self.q, self.q)
        return Wymierna(self.p*other.q+other.p*self.q, self.q*other.q)

    def __sub__(self, other: Union['Wymierna', int]) -> 'Wymierna':
        if type(other) == int:
            return Wymierna(self.p-other*self.q, self.q)
        return Wymierna(self.p*other.q-other.p*self.q, self.q*other.q)

    def __eq__(self, other: Union['Wymierna', int]) -> bool:
        if type(other) == int:
            if not self.q > 1 and not self.q < 1 and not self.p > other and not self.p < other:
                return True
            return False
        elif type(other) == float: # tego już mi się nie chciało robić bez == :p
            if self.p/self.q == other:
                return True
            return False
        liczba1 = self.p/self.q
        liczba2 = other.p/other.q
        if not liczba1 > liczba2 and not liczba1 < liczba2:
            return True
        return False

    def __ne__(self, other: Union['Wymierna', int]) -> bool:
        if type(other) == int:
            if self.q == 1 and self.p == other:
                return False
            return True
        elif type(other) == float:
            if self.p/self.q == other:
                return False
            return True
        if self.p == other.p and self.q == other.q:
            return False
        return True

    def __lt__(self, other: Union['Wymierna', int]) -> bool:
        if type(other) == int or type(other) == float:
            if self.p/self.q < other:
                return True
            return False
        if self.p/self.q < other.p/other.q:
            return True
        return False

    def __le__(self, other: Union['Wymierna', int]) -> bool:
        if type(other) == int or type(other) == float:
            if self.p/self.q <= other:
                return True
            return False
        if self.p/self.q <= other.p/other.q:
            return True
        return False

    def __gt__(self, other: Union['Wymierna', int]) -> bool:
        if type(other) == int or type(other) == float:
            if self.p/self.q > other:
                return True
            return False
        if self.p/self.q > other.p/other.q:
            return True
        return False

    def __ge__(self, other: Union['Wymierna', int]) -> bool:
        if type(other) == int or type(other) == float:
            if self.p/self.q >= other:
                return True
            return False
        if self.p/self.q >= other.p/other.q:
            return True
        return False

    def __mul__(self: 'Wymierna', other: Union['Wymierna', int]) -> 'Wymierna':
        if type(other) == int:
            return Wymierna(self.p * other, self.q)
        return Wymierna(self.p * other.p, self.q * other.q)

    def __truediv__(self: 'Wymierna', other: Union['Wymierna', int]) -> 'Wymierna':
        if type(other) == int:
            return Wymierna(self.p, self.q*other)
        return Wymierna(self.p * other.q, other.p * self.q)


if __name__ == "__main__":
    jeden = Wymierna(1, 2)
    dwa = Wymierna(2, 4)
    trzy = Wymierna(2, 1)
    print("%d %d" % (jeden.get_licznik(), jeden.get_mianownik()))
    assert(jeden.get_licznik() == 1 and jeden.get_mianownik() == 2)
    print("%d %d" % (dwa.get_licznik(), dwa.get_mianownik()))
    assert(dwa.get_licznik() == 1 and dwa.get_mianownik() == 2)
    print("%0.0f" % (float(jeden + dwa)))
    assert(jeden + dwa == 1)
    print("%0.2f %0.2f" % (float(jeden * dwa), float(jeden / dwa)))
    assert(jeden * dwa == 0.25 and jeden / dwa == 1)
    print("%0.2f %0.2f" % (jeden * 2, jeden / 2))
    assert(jeden * 2 == 1.0 and jeden / 2 == 0.25)
    assert(jeden == 0.5)
    assert(jeden == dwa)
    assert(trzy == 2)
    assert(trzy > 1)
    assert(trzy < 5)
    
