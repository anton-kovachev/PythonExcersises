import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        self.cards = []
        for i in range(0, 4):
            for j in range(0, 13):
                self.cards.append(Card(i,j + 1))

    def shuffle(self):
        shuffleTimes = random.randint(2, 10)
        for i in range(0, shuffleTimes):
            index = random.randint(0, len(self.cards) - 1)
            self.cards.append(self.cards.pop(index))

    def deal(self, num_cards):
        deal_cards = self.cards[0:num_cards]
        self.cards = self.cards[num_cards:]
        return deal_cards
