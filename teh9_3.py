import random

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

# Pääohjelma

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_jatkuu = True
while kilpailu_jatkuu:
    # Muuta nopeuksia
    for auto in autot:
        nopeudenlisays = random.randint(-10, 15)
        auto.kiihdytä(nopeudenlisays)

    # Aja tunnin ajan
    for auto in autot:
        auto.kulje(1)

    # Tarkista voittaja
    for auto in autot:
        if auto.matka >= 10000:
            kilpailu_jatkuu = False
            voittaja = auto

# Tulosta tulokset
print("Kilpailun tulokset:")
print("-" * 20)
for auto in autot:
    auto.tulosta_tiedot()
    print()

print(f"Voittaja: {voittaja.rekisteritunnus}")
