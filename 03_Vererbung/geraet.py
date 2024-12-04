class Geraet:
    def __init__(self, hersteller, modell, stromverbrauch):
        self.hersteller = hersteller
        self.modell = modell
        self.stromverbrauch = stromverbrauch

    def einschalten(self):
        print(f"{self.hersteller} {self.modell} wird eingeschaltet.")

    def ausschalten(self):
        print(f"{self.hersteller} {self.modell} wird ausgeschaltet.")

    def info(self):
        return f"Hersteller: {self.hersteller}, Modell: {self.modell}, Stromverbrauch: {self.stromverbrauch}W"