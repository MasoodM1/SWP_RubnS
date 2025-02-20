class Raum:
    def __init__(self, nummer):
        self.nummer = nummer
        self.besetzt = False

    def einchecken(self):
        if self.besetzt == False:
            self.besetzt = True
            return f"Raum {self.nummer} ist nun belegt."
        else:
            return f"Raum {self.nummer} ist bereits belegt."

    def auschecken(self):
        if self.besetzt:
            self.besetzt = False
            return f"Raum {self.nummer} ist nun frei."
        else:
            return f"Raum {self.nummer} ist bereits frei."

    def __str__(self):
        status = "belegt" if self.besetzt else "frei"
        return f"Raum {self.nummer}: {status}"