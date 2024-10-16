import random

# Kartenklasse mit Farbe und Rang
class Card:
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} von {self.color}'  # Lesbare Ausgabe: "A von Herz"

#
class Deck:
    colors = ['Herz', 'Karo', 'Kreuz', 'Pik']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(color, rank) for color in self.colors for rank in self.ranks]    # Erzeugt alle 52 Karten mit Farbe und Rang
        random.shuffle(self.cards) # Misch die Reihenfolge der Karten

    def draw(self):
        return [self.cards.pop() for _ in range(5)] # Zieht 5 Karten vom Deck und mit pop() bereits gezogene Karten entfernt

class PokerSimulator:
    def __init__(self):
        self.deck = Deck()

    def deal_hand(self):
        return self.deck.draw()

    def is_royal_flush(self, hand):
        return self.is_straight_flush(hand) and 'A' in [card.rank for card in hand] # Royal Flush ist ein Straight Flush mit Ass

    def is_straight_flush(self, hand):
        return self.is_flush(hand) and self.is_straight(hand) # Ob es gleiche Farbe und Reihenfolge hat

    def is_four_of_a_kind(self, hand):
        ranks = [card.rank for card in hand]
        return ranks.count(ranks[0]) == 4 or ranks.count(ranks[1]) == 4 # Zählt ob die erste oder zweite Karte 4 Mal vorkommt

    def is_full_house(self, hand):
        ranks = [card.rank for card in hand] # Liste der Ränge
        unique_ranks = set(ranks) # Die Anzahl der verschiedenen Ränge
        return len(unique_ranks) == 2 and (ranks.count(ranks[0]) == 3 or ranks.count(ranks[1]) == 3)

    def is_flush(self, hand):
        colors = [card.color for card in hand]
        return len(set(colors)) == 1

    def is_straight(self, hand):
        ranks = [card.rank for card in hand]
        rank_values = sorted([Deck.ranks.index(rank) for rank in ranks]) # jede Rang wird der Index gesucht und sortiert dies aufsteigend
        return rank_values == list(range(rank_values[0], rank_values[0] + 5))

    def is_three_of_a_kind(self, hand):
        ranks = [card.rank for card in hand]
        return any(ranks.count(rank) == 3 for rank in ranks) # Zählt ob ein Rang 3 Mal vorkommt

    def is_two_pair(self, hand):
        ranks = [card.rank for card in hand]
        return len([rank for rank in set(ranks) if ranks.count(rank) == 2]) == 2 # list comprehension an Zahlen die nur 2 Mal vorkommen und diese list soll es 2 Mal geben

    def is_one_pair(self, hand):
        ranks = [card.rank for card in hand]
        return any(ranks.count(rank) == 2 for rank in ranks)

    def evaluate_hand(self, hand):
        if self.is_royal_flush(hand):
            return "Royal Flush"
        elif self.is_straight_flush(hand):
            return "Straight Flush"
        elif self.is_four_of_a_kind(hand):
            return "Four of a Kind"
        elif self.is_full_house(hand):
            return "Full House"
        elif self.is_flush(hand):
            return "Flush"
        elif self.is_straight(hand):
            return "Straight"
        elif self.is_three_of_a_kind(hand):
            return "Three of a Kind"
        elif self.is_two_pair(hand):
            return "Two Pair"
        elif self.is_one_pair(hand):
            return "One Pair"
        else:
            return "High Card"

    def simulate_draws(self, num_draws):
        results = {}
        high_card_count = 0
        for _ in range(num_draws):
            self.deck = Deck()  # Reset the deck for each draw
            hand = self.deal_hand()
            hand_evaluation = self.evaluate_hand(hand)
            if hand_evaluation == "High Card":
                high_card_count += 1
            else:
                if hand_evaluation in results:
                    results[hand_evaluation] += 1
                else:
                    results[hand_evaluation] = 1
        results["High Card"] = high_card_count

        for hand_type, count in results.items():
            percentage = (count / num_draws) * 100
            print(f"{hand_type}: {count} ({percentage:.4f}%)")

if __name__ == '__main__':
    simulator = PokerSimulator()
    hand = simulator.deal_hand()
    print("Ihre Hand:", hand)
    print("Hand Bewertung:", simulator.evaluate_hand(hand))
    simulator.simulate_draws(1000000)