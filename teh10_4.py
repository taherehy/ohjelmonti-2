class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeudenlisays = random.randint(-10, 15)
            auto.kiihdytä(nopeudenlisays)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailun {self.nimi} tilanne:")
        print("-" * 20)
        for auto in self.autot:
            auto.tulosta_tiedot()
            print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


# Pääohjelma

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

# Simuloidaan kilpailua
for _ in range(100):
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi():
        break

# Tulosta tilanne
kilpailu.tulosta_tilanne()

# Tulosta voittaja
if kilpailu.kilpailu_ohi():
    voittaja = max(autot, key=lambda auto: auto.matka)
    print(f"Voittaja: {voittaja.rekisteritunnus}")
else:
    print("Kilpailu ei ole vielä ohi.")
