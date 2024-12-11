from person import Person

class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung