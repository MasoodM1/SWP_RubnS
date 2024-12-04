from geraet import Geraet

class Fernseher(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, groesse, aufloesung):
        super().__init__(hersteller, modell, stromverbrauch)
        self.groesse = groesse  # in Zoll
        self.aufloesung = aufloesung  # z.B. "4K", "1080p"

    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, Größe: {self.groesse} Zoll, Auflösung: {self.aufloesung}"

class Laptop(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, cpu, ram):
        super().__init__(hersteller, modell, stromverbrauch)
        self.cpu = cpu
        self.ram = ram  # in GB

    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, CPU: {self.cpu}, RAM: {self.ram}GB"

class Smartphone(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, kamera_megapixel, speicher):
        super().__init__(hersteller, modell, stromverbrauch)
        self.kamera_megapixel = kamera_megapixel
        self.speicher = speicher  # in GB

    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, Kamera: {self.kamera_megapixel}MP, Speicher: {self.speicher}GB"

class Tablet(Geraet):
    def __init__(self, hersteller, modell, stromverbrauch, groesse, speicher):
        super().__init__(hersteller, modell, stromverbrauch)
        self.groesse = groesse  # in Zoll
        self.speicher = speicher  # in GB

    def info(self):
        grundinfo = super().info()
        return f"{grundinfo}, Größe: {self.groesse} Zoll, Speicher: {self.speicher}GB"