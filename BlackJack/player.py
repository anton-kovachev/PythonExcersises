from hand import Hand

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def get_str_hand(self):
        return str(self.hand)
    
    def add_to_hand(self, cards):
        for card in cards:
            self.hand.add_to_hand(card)
    
    def get_hand_value(self):
        return self.hand.get_value()
