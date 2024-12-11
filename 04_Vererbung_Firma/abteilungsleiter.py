from mitarbeiter import Mitarbeiter

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)