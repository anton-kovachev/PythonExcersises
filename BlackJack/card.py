class Card:
    SUIT_SYMBOLS = {
        0: u"\u2666",  # diamonds
        1: u"\u2665",  # hearts
        2: u"\u2663",  # clubs
        3: u"\u2660"  # spades
    }

    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }

    def __init__(self, deckNumber, cardNumber):
        self.deckNumber = deckNumber
        self.card_number = cardNumber

    def __str__(self):
        return f"{Card.VALUE_NAMES[self.card_number]}{Card.SUIT_SYMBOLS[self.deckNumber]}"
    
    def get_value(self):
        if self.card_number == 1:
            return None
        elif self.card_number in range(2, 10):
            return self.card_number
        else:
            return 10
