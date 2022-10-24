class Car(object):
    wydajnoscPaliwowa: float
    maxPaliwo: float
    paliwo: float

    def __init__(self, wydajnoscPaliwowa: float, maxPaliwo: float, paliwo: float):
        self.wydajnoscPaliwowa = wydajnoscPaliwowa
        self.maxPaliwo = maxPaliwo
        self.paliwo = paliwo

    def drive(self, kilometry:float):
        if kilometry*self.wydajnoscPaliwowa > self.paliwo:
            self.paliwo = 0
            return "zabraklo paliwa"
        self.paliwo -= kilometry*self.wydajnoscPaliwowa

    def get_fuel_level(self):
        return self.paliwo

    def add_fuel(self, fuel: float):
        self.paliwo += fuel
        if self.paliwo > self.maxPaliwo:
            text = "rozlalo sie "+self.maxPaliwo-self.paliwo+" litrow paliwa"
            self.paliwo = self.maxPaliwo
            