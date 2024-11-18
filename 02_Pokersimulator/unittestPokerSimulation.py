import unittest
from main import kartenZiehen, wertefarben, strasse, gleicheWerte, flush, kombinationErkennen

class TestPokerSimulator(unittest.TestCase):

    def setUp(self):
        self.farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
        self.symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
        self.kartenstapel = [(farbe, symbol) for farbe in self.farben for symbol in self.symbole]

    def test_kartenZiehen(self):
        hand = kartenZiehen(5, self.kartenstapel)
        self.assertEqual(len(hand), 5)
        for karte in hand:
            self.assertIn(karte, self.kartenstapel)

    def test_wertefarben(self):
        hand = [('Herz', '2'), ('Karo', '3'), ('Pik', '4'), ('Kreuz', '5'), ('Herz', '6')]
        werte, farben = wertefarben(hand)
        self.assertEqual(werte, ['2', '3', '4', '5', '6'])
        self.assertEqual(farben, ['Herz', 'Karo', 'Pik', 'Kreuz', 'Herz'])

    def test_strasse(self):
        werte = ['2', '3', '4', '5', '6']
        self.assertTrue(strasse(werte, self.symbole))
        werte = ['2', '3', '4', '5', '7']
        self.assertFalse(strasse(werte, self.symbole))

    def test_gleicheWerte(self):
        werte = ['2', '2', '3', '3', '3']
        result = gleicheWerte(werte)
        self.assertEqual(result, {'2': 2, '3': 3})

    def test_flush(self):
        farben = ['Herz', 'Herz', 'Herz', 'Herz', 'Herz']
        self.assertTrue(flush(farben))
        farben = ['Herz', 'Karo', 'Pik', 'Kreuz', 'Herz']
        self.assertFalse(flush(farben))

    def test_kombinationErkennen(self):
        hand = [('Herz', '10'), ('Herz', 'Bube'), ('Herz', 'Dame'), ('Herz', 'König'), ('Herz', 'Ass')]
        self.assertEqual(kombinationErkennen(hand), "Royal Flush")
        hand = [('Herz', '9'), ('Herz', '10'), ('Herz', 'Bube'), ('Herz', 'Dame'), ('Herz', 'König')]
        self.assertEqual(kombinationErkennen(hand), "Straight Flush")
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '2'), ('Kreuz', '2'), ('Herz', '3')]
        self.assertEqual(kombinationErkennen(hand), "Vierling")
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '2'), ('Kreuz', '3'), ('Herz', '3')]
        self.assertEqual(kombinationErkennen(hand), "Full House")
        hand = [('Herz', '2'), ('Herz', '4'), ('Herz', '6'), ('Herz', '8'), ('Herz', '10')]
        self.assertEqual(kombinationErkennen(hand), "Flush")
        hand = [('Herz', '2'), ('Karo', '3'), ('Pik', '4'), ('Kreuz', '5'), ('Herz', '6')]
        self.assertEqual(kombinationErkennen(hand), "Straße")
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '2'), ('Kreuz', '4'), ('Herz', '5')]
        self.assertEqual(kombinationErkennen(hand), "Drilling")
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '3'), ('Kreuz', '3'), ('Herz', '4')]
        self.assertEqual(kombinationErkennen(hand), "Zwei Paare")
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '4'), ('Kreuz', '5'), ('Herz', '6')]
        self.assertEqual(kombinationErkennen(hand), "Ein Paar")
        hand = [('Herz', '2'), ('Karo', '3'), ('Pik', '4'), ('Kreuz', '5'), ('Herz', '7')]
        self.assertEqual(kombinationErkennen(hand), "High Card")

if __name__ == '__main__':
    unittest.main()