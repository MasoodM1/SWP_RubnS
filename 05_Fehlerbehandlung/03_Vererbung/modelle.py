from geraet import Geraet

class Fernseher(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, groesse, aufloesung):
        super().__init__(hersteller, modell, stromverbrauch)
        if groesse <= 0:
            raise ValueError("Größe muss positiv sein")  # Neuer Fehler, nicht behebbar
        else:
            self.groesse = groesse
        self.aufloesung = aufloesung if aufloesung else "Unknown"  # Neuer Fehler, aber behebbar

    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, Größe: {self.groesse} Zoll, Auflösung: {self.aufloesung}"

class Laptop(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, cpu, ram):
        super().__init__(hersteller, modell, stromverbrauch)
        if ram <= 0:
            raise ValueError("RAM muss positiv sein")  # Neuer Fehler, nicht behebbar
        else:
            self.ram = ram
        self.cpu = cpu if cpu else "Unknown"  # Neuer Fehler, aber behebbar
    
    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, CPU: {self.cpu}, RAM: {self.ram}GB"

class Smartphone(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, kamera_megapixel, speicher):
        super().__init__(hersteller, modell, stromverbrauch)
        try:
            if speicher <= 0:
                raise ValueError("Speicher muss größer als 0 sein.") # Neuer Fehler, nicht behebbar
            else:
                self.speicher = speicher
        except ValueError as error:
            speicher = 64  # Hochgeblubberter Fehler, aber behebbar
            print(f"Fehler behoben: {error}, Standardwert gesetzt.")
        
        self.kamera_megapixel = kamera_megapixel if kamera_megapixel else 12  # Neuer Fehler, aber behebbar
    
    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, Kamera: {self.kamera_megapixel}MP, Speicher: {self.speicher}GB"

class Tablet(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, groesse, speicher):
        super().__init__(hersteller, modell, stromverbrauch)
        try:
            if speicher <= 0:
                raise ValueError("Speicher muss größer als 0 sein.") # Neuer Fehler, nicht behebbar
            else:
                self.speicher = speicher
        except ValueError as error:
            speicher = 64  # Hochgeblubberter Fehler, aber behebbar
            print(f"Fehler behoben: {error}, Standardwert gesetzt.")

        self.groesse = groesse if groesse >= 0 else 10  # Neuer Fehler, aber behebbar

    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, Größe: {self.groesse} Zoll, Speicher: {self.speicher}GB"