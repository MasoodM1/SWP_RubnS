from raum import Raum

class Doppelzimmer(Raum):
    def __init__(self, nummer):
        super().__init__(nummer)
        self.betten = 2