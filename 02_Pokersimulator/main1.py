import random

# Kartenfarben und Symbole werden festgelegt
farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

# Kartenstapel erstellen mit jeweils Farbe und Symbol als ein List
kartenstapel = [(farbe, symbol) for farbe in farben for symbol in symbole]

# Funktion, um Karten zu ziehen
def kartenZiehen(anzahl):
    random.shuffle(kartenstapel)  # Mischt den Kartenstapel zufällig durch.
    gezogeneKarten = kartenstapel[:anzahl]  # Nimmt die gewünschte Anzahl (anzahl) an Karten vom Stapel.
    return gezogeneKarten  # Gibt die gezogenen Karten als Liste von Tupeln zurück.


# Vereinfachte Funktion, um Kartenwerte und -farben zu extrahieren
def wertefarben(hand):
    werte = [karte[1] for karte in hand]  # Erstellt eine Liste der Symbole (Werte) der Karten in der Hand.
    farben = [karte[0] for karte in hand]  # Erstellt eine Liste der Farben der Karten in der Hand.

    # Sortiere die Werte entsprechend der Reihenfolge in der Symbolliste
    sortierteWerte = [wert for wert in symbole if wert in werte]
    # Sortiert die gezogenen Werte so, dass sie in derselben Reihenfolge wie in der Symbol-Liste erscheinen.
    return sortierteWerte, farben  # Gibt die sortierten Werte und Farben zurück.


# Vereinfachte Funktion zur Erkennung einer Straße ohne Nutzung von index() oder sorted()
def strasse(werte):
    for i in range(len(symbole) - 4):  # Die Schleife geht nur so weit, wie Platz für eine Straße ist
        straßeGefunden = 0  # Setze den Zähler nur einmal pro möglicher Straßenkombination
        for j in range(5):  # Eine mögliche Straße besteht aus 5 Karten
            if symbole[i + j] in werte:  # Prüfe, ob der Wert in der Hand vorhanden ist
                straßeGefunden += 1
            else:
                break  # Wenn eine Karte fehlt, ist es keine Straße

        if straßeGefunden == 5:
            return True  # Wenn 5 Karten in Folge gefunden wurden, ist es eine Straße

    return False  # Wenn keine Straße gefunden wurde, gib False zurück



# Gleiche Werte zählen
def gleicheWerte(werte):
    a = {}  # Erstellt ein leeres Wörterbuch, um die Anzahl der Vorkommen jedes Wertes zu speichern.
    for wert in werte:  # Durchläuft jeden Wert in der Hand.
        if wert in a:
            a[wert] += 1  # Wenn der Wert bereits im Wörterbuch ist, wird sein Zähler um 1 erhöht.
        else:
            a[wert] = 1  # Wenn der Wert noch nicht im Wörterbuch ist, wird er mit dem Zähler 1 hinzugefügt.
    return a  # Gibt das Wörterbuch mit der Anzahl der Vorkommen jedes Wertes zurück.


# Flush überprüfen
def flush(farben):
    ersteFarbe = farben[0]  # Nimmt die erste Farbe aus der Liste der Farben.
    for farbe in farben:
        if farbe != ersteFarbe:  # Wenn eine Farbe von der ersten abweicht, ist es kein Flush.
            return False
    return True  # Wenn alle Farben gleich sind, ist es ein Flush.


# Kombination erkennen
def kombinationErkennen(hand):
    werte, farben = wertefarben(hand)  # Extrahiert die sortierten Werte und Farben aus der Hand.
    gleiche = gleicheWerte(werte)  # Zählt die Anzahl der gleichen Werte.

    # Überprüft, ob es ein Royal Flush ist (Flush + Straße mit Ass)
    if flush(farben) and strasse(werte) and 'Ass' in werte:
        return "Royal Flush"

    # Überprüft, ob es ein Straight Flush ist (Flush + Straße)
    if flush(farben) and strasse(werte):
        return "Straight Flush"

    # Überprüft, ob es einen Vierling (4 gleiche Karten) gibt
    if max(gleiche.values()) == 4:
        return "Vierling"

    # Überprüft, ob es ein Full House gibt (eine Dreiergruppe und ein Paar)
    if 2 in gleiche.values() and 3 in gleiche.values():
        return "Full House"

    # Überprüft, ob es einen Flush gibt (alle Karten haben dieselbe Farbe)
    if flush(farben):
        return "Flush"

    # Überprüft, ob es eine Straße gibt (aufeinanderfolgende Werte)
    if strasse(werte):
        return "Straße"

    # Überprüft, ob es einen Drilling (3 gleiche Karten) gibt
    if max(gleiche.values()) == 3:
        return "Drilling"

    # Überprüft, ob es zwei Paare gibt
    if list(gleiche.values()).count(2) == 2:
        return "Zwei Paare"

    # Überprüft, ob es ein Paar gibt (2 gleiche Karten)
    if 2 in gleiche.values():
        return "Ein Paar"

    # Wenn keine der oben genannten Kombinationen gefunden wird, gibt es nur die höchste Karte.
    return "High Card"

def simulation(anzahl):
    ergebnisse = {  # Dictionary zur Speicherung der Ergebnisse
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Vierling": 0,
        "Full House": 0,
        "Flush": 0,
        "Straße": 0,
        "Drilling": 0,
        "Zwei Paare": 0,
        "Ein Paar": 0,
        "High Card": 0
    }

    for _ in range(1000000):  # Simuliere eine Million Runden
        hand = kartenZiehen(anzahl)
        kombination = kombinationErkennen(hand)  # Erkenne die Kombination
        ergebnisse[kombination] += 1  # Erhöhe den Zähler für die gefundene Kombination

    # Ausgabe der Ergebnisse in Prozent ohne Verwendung von items()
    for kombi in ergebnisse:
        anzahl = ergebnisse[kombi]  # Zugriff auf den Wert über den Schlüssel
        prozent = (anzahl / 1000000) * 100  # Prozentsatz berechnen
        print(f"{kombi}: {prozent:.4f}%")


# Hauptfunktion
def main():
    anzahl = 5
    hand = kartenZiehen(anzahl)  # Ziehe 5 Karten aus dem Kartenstapel.
    for karte in hand:
        print(f"{karte[1]} von {karte[0]}")  # Gibt jede gezogene Karte aus, z. B. "König von Herz".
    print("Kombination:", kombinationErkennen(hand))  # Gibt die erkannte Kombination (z. B. "Flush") aus.
    simulation(anzahl)


# Wenn dieses Skript direkt ausgeführt wird (nicht importiert), startet es das Spiel.
if __name__ == '__main__':
    main()  # Ruft die Hauptfunktion auf, die den Ablauf des Spiels startet.
