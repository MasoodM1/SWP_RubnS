from raum import Raum

class Einzelzimmer(Raum):
    def __init__(self, nummer):
        super().__init__(nummer)
        self.betten = 1