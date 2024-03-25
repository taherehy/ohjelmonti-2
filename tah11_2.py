from math import floor

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, aika):
        self.matkamittari += self.huippunopeus * aika

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Matkamittari: {self.matkamittari} km")


class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def aja(self, aika):
        # Lasketaan, kuinka kauan auto voi ajaa akun kapasiteetilla
        ajoaika = self.akkukapasiteetti / (self.huippunopeus * 0.1)

        # Jos ajettava aika on lyhyempi kuin annettu aika, rajoitetaan ajoaikaa
        if aika > ajoaika:
            aika = ajoaika

        super().aja(aika)


class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def aja(self, aika):
        # Lasketaan, kuinka kauan auto voi ajaa bensatankin koolla
        ajoaika = self.bensatankin_koko / (self.huippunopeus * 0.07)

        # Jos ajettava aika on lyhyempi kuin annettu aika, rajoitetaan ajoaikaa
        if aika > ajoaika:
            aika = ajoaika

        super().aja(aika)


# Pääohjelma

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

sahkoauto.tulosta_tiedot()
print()
polttomoottoriauto.tulosta_tiedot()
