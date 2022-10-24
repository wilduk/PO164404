class Adres(object):
    nrDomu: str
    ulica: str
    nrMieszkania: str
    miasto: str
    kodPocztowy: str

    def __init__(self, nrDomu: str, ulica: str, miasto: str, kodPocztowy: str, nrMieszkania: str = None):
        self.nrDomu = nrDomu
        self.ulica = ulica
        self.miasto = miasto
        self.kodPocztowy = kodPocztowy
        self.nrMieszkania = nrMieszkania

    def show(self):
        print(self.ulica+" "+self.nrDomu+" "+self.nrMieszkania+"\n"+self.miasto+" "+self.kodPocztowy)

    def comes_before(self, adres: 'Adres'):
        if self.kodPocztowy == adres.kodPocztowy and self.ulica <= adres.ulica and self.nrDomu < adres.nrDomu:
            return True
        return False
