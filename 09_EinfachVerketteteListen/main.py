import random


class Liste:
    def __init__(self, wert):
        # Erstellt einen neuen Liste mit einem Wert und einem Verweis auf den nächsten Liste
        self.wert = wert
        self.next = None


class EinfacheVerketteteListe:
    def __init__(self):
        # Erstellt eine leere einfach verkettete Liste
        self.kopf = None
        self.laenge = 0  # Speichert die Länge der Liste

    def ende_hinzufuegen(self, wert):
        # Fügt einen neuen Liste mit dem gegebenen Wert am Ende der Liste hinzu
        neuer_Liste = Liste(wert)
        if self.kopf is None:
            self.kopf = neuer_Liste  # Falls die Liste leer ist, wird der neue Liste zum Kopf
        else:
            akt_Liste = self.kopf
            while akt_Liste.next:  # Gehe bis zum letzten Liste
                akt_Liste = akt_Liste.next
            akt_Liste.next = neuer_Liste  # Setze den neuen Liste ans Ende
        self.laenge += 1  # Erhöhe die Länge der Liste um 1

    def get_laenge(self) -> int:
        # Gibt die gespeicherte Länge der Liste zurück
        return self.laenge

    def ausgeben(self):
        # Gibt alle Elemente der Liste aus
        akt_Liste = self.kopf
        while akt_Liste:
            print(akt_Liste.wert, end=" -> ")  # Drucke den aktuellen Wert
            akt_Liste = akt_Liste.next  # Gehe zum nächsten Liste
        print("None")  # Markiere das Ende der Liste

    def __iter__(self):
        # Initialisiert den Iterator
        self.akt_Liste = self.kopf
        return self

    def __next__(self):
        # Definiert das Verhalten des Iterators beim nächsten Element
        if self.akt_Liste is None:
            raise StopIteration  # Stoppe die Iteration, wenn das Ende erreicht ist
        wert = self.akt_Liste.wert
        self.akt_Liste = self.akt_Liste.next  # Gehe zum nächsten Liste
        return wert


if __name__ == "__main__":
    liste = EinfacheVerketteteListe()

    # Liste mit Zufallszahlen befüllen
    for _ in range(10):
        liste.ende_hinzufuegen(random.randint(1, 100))

    # Ausgabe der Liste
    print("Liste:")
    liste.ausgeben()

    # Ausgabe der Länge der Liste
    print(f"Länge der Liste: {liste.get_laenge()}")

    # Iterieren über die Liste mit dem Iterator-Protokoll
    print("Elemente durch Iteration:")
    for wert in liste:
        print(wert, end=" ")
