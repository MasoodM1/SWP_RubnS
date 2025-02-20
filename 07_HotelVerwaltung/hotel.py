from einzellzimmer import Einzelzimmer
from doppelzimmer import Doppelzimmer

class Hotel:
    def __init__(self, name):
        self.name = name
        self.zimmer = []

    def zimmer_hinzufuegen(self, zimmer):
        self.zimmer.append(zimmer)
    
    def zimmer_entfernen(self, nummer):
        for zimmer in self.zimmer:
            if zimmer.nummer == nummer:
                self.zimmer.remove(zimmer)
                return f"Zimmer {nummer} wurde entfernt."

    def freie_zimmer(self):
        return [z for z in self.zimmer if not z.besetzt]

    def belegte_zimmer(self):
        return [z for z in self.zimmer if z.besetzt]

    def zimmer_liste(self):
        result = ""
        for z in self.zimmer:
            result += str(z) + "\n"
        return result

    def einchecken(self, nummer):
        for zimmer in self.zimmer:
            if zimmer.nummer == nummer:
                return zimmer.einchecken()
        else:
            return f"Zimmer {nummer} nicht gefunden."

    def auschecken(self, nummer):
        for zimmer in self.zimmer:
            if zimmer.nummer == nummer:
                return zimmer.auschecken()
        else:
            return f"Zimmer {nummer} nicht gefunden."
