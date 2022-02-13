class Mieszkanie:
    def __init__(self, typ, cena, poziom, umeblowane, rynek, rodzaj_zab, pow, pokoje):
        self.typ = typ
        self.cena = cena
        self.poziom = poziom
        self.umeblowane = umeblowane
        self.rynek = rynek
        self.rodzaj_zabudowy = rodzaj_zab
        self.powierzchnia = pow
        self.liczba_pokoi = pokoje

    def __str__(self):


a = Mieszkanie("Firmowe", "10700", "parter", "nie", "pierwotny", "Apartamentowiec", "70,38", "4")
print(a.typ)
