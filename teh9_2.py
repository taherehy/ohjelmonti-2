class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus <0:
            self.nopeus = 0

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Matka: {self.matka}")
        print(f"Nopeus: {self.nopeus}")




bmw = Auto("ABC-123", 142)

bmw.kiihdytä(30)
bmw.kiihdytä(50)
bmw.kiihdytä(70)
bmw.tulosta_tiedot()

bmw.kiihdytä(-200)
bmw.tulosta_tiedot()
