class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = ""

    def set_leiter(self, leiter):
        self.leiter = leiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)