class Geraet:
    def __init__(self, hersteller, modell, stromverbrauch):
        if not hersteller or not modell:
            raise ValueError("Hersteller und Modell müssen angegeben werden")  # Neuer Fehler, nicht behebbar
        elif stromverbrauch <= 0:
            raise ValueError("Stromverbrauch darf nicht kleiner oder gleich 0 sein")
        else:
            self.hersteller = hersteller
            self.modell = modell
            self.stromverbrauch = stromverbrauch

    def einschalten(self):
        print(f"{self.hersteller} {self.modell} wird eingeschaltet.")

    def ausschalten(self):
        print(f"{self.hersteller} {self.modell} wird ausgeschaltet.")

    def info(self):
        return f"Hersteller: {self.hersteller}, Modell: {self.modell}, Stromverbrauch: {self.stromverbrauch}W"