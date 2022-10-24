class Student(object):
    imie: str
    nazwisko: str
    wynik: int = 0
    ile: int = 0

    def __init__(self, imie: str, nazwisko: str):
        self.imie = imie
        self.nazwisko = nazwisko

    def get_name(self):
        return self.imie, self.nazwisko

    def add_quiz(self, score: int):
        self.wynik += score
        self.ile += 1

    def get_total_score(self):
        return self.wynik

    def get_average_score(self):
        return self.wynik/self.ile
