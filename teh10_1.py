class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        """
        Siirtää hissin haluttuun kerrokseen.

        Args:
            kohdekerros: Kerros, johon hissi siirtyy.

        Returns:
            None.
        """
        if kohdekerros > self.ylin_kerros:
            print(f"Virhe: Kohdekerros {kohdekerros} on ylimmän kerroksen ({self.ylin_kerros}) yläpuolella.")
            return
        elif kohdekerros < self.alin_kerros:
            print(f"Virhe: Kohdekerros {kohdekerros} on alimman kerroksen ({self.alin_kerros}) alapuolella.")
            return

        while self.kerros != kohdekerros:
            if self.kerros < kohdekerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

        print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def kerros_ylös(self):
        """
        Siirtää hissin yhden kerroksen ylöspäin.

        Args:
            None.

        Returns:
            None.
        """
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")
        else:
            print(f"Hissi on jo ylimmässä kerroksessa ({self.ylin_kerros}).")

    def kerros_alas(self):
        """
        Siirtää hissin yhden kerroksen alaspäin.

        Args:
            None.

        Returns:
            None.
        """
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")
        else:
            print(f"Hissi on jo alimmassa kerroksessa ({self.alin_kerros}).")


# Pääohjelma

h = Hissi(1, 10)  # Luodaan hissi, joka kulkee kerrosten 1-10 välillä

# Siirrytään kerrokseen 5
h.siirry_kerrokseen(5)

# Siirrytään takaisin alimpaan kerrokseen
h.siirry_kerrokseen(1)
