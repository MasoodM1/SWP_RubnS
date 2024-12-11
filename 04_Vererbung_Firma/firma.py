from abteilung import Abteilung

class Firma:
    def __init__(self):
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def anzahl_mitarbeiter(self):
        return sum(abt.anzahl_mitarbeiter() for abt in self.abteilungen)

    def anzahl_abteilungsleiter(self):
        return len([abt for abt in self.abteilungen if abt.leiter])

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        groesste = self.abteilungen[0]
        for abt in self.abteilungen:
            if abt.anzahl_mitarbeiter() > groesste.anzahl_mitarbeiter():
                groesste = abt
        return groesste

    def geschlechterverhaeltnis(self):
        gesamt_mitarbeiter = [mitarbeiter for abt in self.abteilungen for mitarbeiter in abt.mitarbeiter]
        anzahl_maenner = len([mitarbeiter for mitarbeiter in gesamt_mitarbeiter if mitarbeiter.gender == "m"])
        anzahl_frauen = len([mitarbeiter for mitarbeiter in gesamt_mitarbeiter if mitarbeiter.gender == "w"])
        gesamt = len(gesamt_mitarbeiter)
        return (anzahl_frauen / gesamt * 100, anzahl_maenner / gesamt * 100)