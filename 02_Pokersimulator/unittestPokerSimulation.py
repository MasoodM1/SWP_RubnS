import unittest
from main import kartenZiehen, kombinationErkennen, flush, gleicheWerte, strasse

class TestPokerFunctions(unittest.TestCase):
    def test_kartenZiehen(self):
        kartenstapel = [('Herz', '2'), ('Karo', '3'), ('Pik', '4'), ('Kreuz', '5')]
        hand = kartenZiehen(2, kartenstapel)
        self.assertEqual(len(hand), 2)  # Testet ob die Hand 2 Karten enthält (x == y)
        for karte in hand:
            self.assertIn(karte, kartenstapel)  # Testet ob karte die gleiche Objekt ist wie im kartenstapel (x is y)

    def test_kombinationErkennen(self):
        symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
        royal_flush = [('Herz', '10'), ('Herz', 'Bube'), ('Herz', 'Dame'), ('Herz', 'König'), ('Herz', 'Ass')]
        straight_flush = [('Karo', '6'), ('Karo', '7'), ('Karo', '8'), ('Karo', '9'), ('Karo', '10')]
        self.assertEqual(kombinationErkennen(royal_flush, symbole), "Royal Flush")
        self.assertEqual(kombinationErkennen(straight_flush, symbole), "Straight Flush")

    def test_flush(self):
        farben = ['Herz', 'Herz', 'Herz', 'Herz', 'Herz']
        self.assertTrue(flush(farben))  # bool(x) is True => also ob flush zutrifft
        farben = ['Herz', 'Karo', 'Herz', 'Herz', 'Herz']
        self.assertFalse(flush(farben))

    def test_gleicheWerte(self):
        werte = ['10', '10', 'Ass', 'Ass', '10']
        ergebnis = gleicheWerte(werte)
        self.assertEqual(ergebnis, {'10': 3, 'Ass': 2})

    def test_strasse(self):
        werte = ['6', '7', '8', '9', '10']
        symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
        self.assertTrue(strasse(werte, symbole))
        werte = ['5', '7', '8', '9', '10']
        self.assertFalse(strasse(werte, symbole))

if __name__ == '__main__':
    unittest.main()
