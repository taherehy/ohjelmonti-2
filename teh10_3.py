class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_nro, kohdekerros):
        if 0 <= hissi_nro < len(self.hissit):
            self.hissit[hissin_nro].siirry_kerrokseen(kohdekerros)
        else:
            print(f"Virhe: Hissinumero {hissin_nro} on virheellinen.")

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)
        print("Palohälytys! Kaikki hissit on ajettu pohjakerrokseen.")

# Pääohjelma

talo = Talo(1, 10, 2)

# Ajetaan hissiä 1 kerrokseen 5
talo.aja_hissiä(0, 5)

# Ajetaan hissiä 2 kerrokseen 3
talo.aja_hissiä(1, 3)

# Simuloidaan palohälytys
talo.palohälytys()
