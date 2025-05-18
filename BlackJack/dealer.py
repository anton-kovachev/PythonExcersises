from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()
        self.has_hit = False

    def get_str_hand(self):
        return str(self.hand)
    
    def add_to_hand(self, cards):
        for card in cards:
            self.hand.add_to_hand(card)

    def hit(self, card):
        self.hit = True

    def get_hand_value(self):
        return self.hand.get_value()
    
