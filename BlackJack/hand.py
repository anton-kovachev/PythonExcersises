class Hand:
    def __init__(self):
       self.cards = [] 

    def get_value(self):
        hand_value = 0
        for card in self.cards:
            card_value = card.get_value()
            has_ace = False
            if card_value is not None:
                hand_value += card_value
            else:
                has_ace = True
            if has_ace:
                if hand_value + 11 <= 21:
                    hand_value += 11
                else:
                    hand_value += 1
                    
        return hand_value
    
    def add_to_hand(self, card):
        self.cards.append(card)

    def __str__(self):
        return " ".join([str(card) for card in self.cards])
