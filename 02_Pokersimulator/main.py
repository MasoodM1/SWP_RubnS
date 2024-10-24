import random

farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
kartenstapel = [(farbe, symbol) for farbe in farben for symbol in symbole]

def kartenZiehen(anzahl):
    return random.sample(kartenstapel,anzahl)

def wertefarben(hand):
    werte = [karte[1] for karte in hand]
    farbe = [karte[0] for karte in hand]
    return werte, farbe

def strasse(werte):
    werte_index = sorted([symbole.index(wert) for wert in werte])   # mit index wird die Position in der symbole-list gefunden und mit sorted sortiert
    for i in range(len(werte_index) - 4):   # -4 damit wie oft 5 Karten Platz hätten
        if werte_index[i + 4] - werte_index[i] == 4:    # der Position des 5 Wert minus erste Wert 4 ergibt
            return True
    return False

def gleicheWerte(werte):
    a = {}
    for wert in werte:
        if wert in a:
            a[wert] += 1
        else:
            a[wert] = 1
    return a

def flush(farben):
    return len(set(farben)) == 1    # set ergibt eine Menge an eindeutigen Farben

def kombinationErkennen(hand):
    werte, farbe = wertefarben(hand)
    gleiche = gleicheWerte(werte)

    if flush(farbe) and strasse(werte) and 'Ass' in werte:
        return "Royal Flush"    # wenn gleiche Farbe, 5 Werte nacheinander und ein Ass enthalten

    if flush(farbe) and strasse(werte):
        return "Straight Flush"     # wenn gleiche Farbe und 5 Werte hintereinander

    if 4 in gleiche.values():   # values gibt eine Liste der Häufigkeiten der Werte zurück
        return "Vierling"

    if 3 in gleiche.values() and 2 in gleiche.values():
        return "Full House"

    if flush(farbe):
        return "Flush"

    if strasse(werte):
        return "Straße"

    if 3 in gleiche.values():
        return "Drilling"

    paare = list(gleiche.values()).count(2)     # count(2) zählt wie oft 2 in der Häufigkeitsliste vorkommt
    if paare == 2:
        return "Zwei Paare"

    if paare == 1:
        return "Ein Paar"

    return "High Card"

def simulation(anzahl):
    ergebnisse = {
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

    for _ in range(1000000):
        hand = kartenZiehen(anzahl)
        kombination = kombinationErkennen(hand)
        ergebnisse[kombination] += 1

    for kombi in ergebnisse:
        anzahl = ergebnisse[kombi]
        prozent = (anzahl / 1000000) * 100
        print(f"{kombi}: {prozent:.4f}%")

def main():
    anzahl = 5
    hand = kartenZiehen(anzahl)
    for karte in hand:
        print(f"{karte[1]} von {karte[0]}")
    print("Kombination:", kombinationErkennen(hand))
    simulation(anzahl)

if __name__ == '__main__':
    main()