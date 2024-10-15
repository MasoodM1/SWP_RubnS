import random
from collections import Counter

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} von {self.suit}'

class Deck:
    suits = ['Herz', 'Karo', 'Kreuz', 'Pik']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return [self.cards.pop() for _ in range(5)]

class PokerSimulator:
    def __init__(self):
        self.deck = Deck()

    def deal_hand(self):
        return self.deck.draw()

    def is_royal_flush(self, hand):
        return self.is_straight_flush(hand) and 'A' in [card.rank for card in hand]

    def is_straight_flush(self, hand):
        return self.is_flush(hand) and self.is_straight(hand)

    def is_four_of_a_kind(self, hand):
        ranks = [card.rank for card in hand]
        return 4 in Counter(ranks).values()

    def is_full_house(self, hand):
        ranks = [card.rank for card in hand]
        counter = Counter(ranks).values()
        return 3 in counter and 2 in counter

    def is_flush(self, hand):
        suits = [card.suit for card in hand]
        return len(set(suits)) == 1

    def is_straight(self, hand):
        ranks = [card.rank for card in hand]
        rank_values = sorted([Deck.ranks.index(rank) for rank in ranks])
        return rank_values == list(range(rank_values[0], rank_values[0] + 5))

    def is_three_of_a_kind(self, hand):
        ranks = [card.rank for card in hand]
        return 3 in Counter(ranks).values()

    def is_two_pair(self, hand):
        ranks = [card.rank for card in hand]
        return list(Counter(ranks).values()).count(2) == 2

    def is_one_pair(self, hand):
        ranks = [card.rank for card in hand]
        return 2 in Counter(ranks).values()

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
        results = Counter()
        high_card_count = 0
        for _ in range(num_draws):
            self.deck = Deck()  # Reset the deck for each draw
            hand = self.deal_hand()
            hand_evaluation = self.evaluate_hand(hand)
            if hand_evaluation == "High Card":
                high_card_count += 1
            else:
                results[hand_evaluation] += 1
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