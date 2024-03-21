class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Matka: {self.matka}")
        print(f"Nopeus: {self.nopeus}")

    def kiihdytä(self, nopeudenlisays):

        self.nopeus += nopeudenlisays
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara


bmw = Auto("ABC-123", 142)

bmw.kiihdyttä(60)
bmw.kulje(1.5)

print(f"Matka: {bmw.matka}")
