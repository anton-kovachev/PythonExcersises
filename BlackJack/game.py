from deck import Deck
from hand import Hand
import random


class Game:
    MINIMUM_BET = 1
    CURRENT_PLAYER = "Player"
    CURRENT_DEALER = "Dealer"
    NEXT_MOVE_HIT = "HIT"
    NEXT_MOVE_STAY = "STAY"

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        play_hand = ""
        
        while self.player.balance > 0:
            while(play_hand.upper() != "yes".upper()):
                play_hand = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ")
                if play_hand != "yes":
                    print("Invalid answer")
            bet = 0
            
            while bet < self.MINIMUM_BET:
                try:
                    bet = int(input("Place your bet: "))
                    if bet < self.MINIMUM_BET:
                        print(f"The minimum bet is ${Game.MINIMUM_BET}.")
                except:
                    bet = 0
            
            self.deck.create_deck()
            self.deck.shuffle()
            
            self.player_next_hit(2)
            self.dealer_next_hit(2)
            
            current = Game.CURRENT_PLAYER
            
            while not self.dealer.has_hit or (self.player.get_hand_value() <= 21 and self.dealer.get_hand_value() <= 21 and self.player.get_hand_value() < self.dealer.get_hand_value()):
                if current == Game.CURRENT_PLAYER:
                    next_move = ""
                    while next_move != Game.NEXT_MOVE_HIT and next_move != Game.NEXT_MOVE_STAY:
                        next_move = input("Would you like to hit or stay? ")
                        if next_move.upper() != Game.NEXT_MOVE_HIT.upper() and next_move.upper() != Game.NEXT_MOVE_STAY.upper():
                            print("This is not a valid option")

                    if next_move.upper() == Game.NEXT_MOVE_HIT:
                        self.player_next_hit(1) 
                        self.print_side_has(Game.CURRENT_PLAYER, self.player.hand)
                    else:
                        current = Game.CURRENT_DEALER
                else:
                    self.print_side_has(Game.CURRENT_DEALER, self.dealer.hand)
                    self.dealer.has_hit = True
                    while self.dealer.get_hand_value() <= 16:
                        self.dealer_next_hit(1)
                    else:
                        current = Game.CURRENT_PLAYER
                        print("The dealer stays")
            
            if self.player.get_hand_value() > 21:
                self.player.balance -= bet
                print(f"Your hand value is over 21 and you lose ${bet} :(")  
            elif self.dealer.get_hand_value() > 21:
                self.player.balance += bet
                print(f"The dealer busts, you win ${bet} :)")  
            elif self.player.get_hand_value() == self.dealer.get_hand_value():
                print("You tie. Your bet has been returned.") 
            elif self.player.get_hand_value() > self.dealer.get_hand_value():
                self.player.balance += bet
                print(f"You win ${bet}")
            else:
                print(f"The dealer wins, you lose ${bet} :(")
            
    def player_next_hit(self, number_of_cards):
        cards = self.deck.deal(number_of_cards)
        self.player.add_to_hand(cards)
        self.print_player_dealt(cards)
    
    def dealer_next_hit(self, number_of_cards):
        cards = self.deck.deal(number_of_cards)
        self.dealer.add_to_hand(cards)
        self.print_dealer_dealt(cards, hide = number_of_cards > 1 and not self.dealer.has_hit)
    
    def print_player_dealt(self, cards):
        print(f"You are dealt: {' '.join([str(card) for card in cards])}")
    
    def print_dealer_dealt(self, cards, hide = False):
        print(f"{"The dealer is dealt" if len(cards) == 2 else "The dealer hit and is dealt"}: {' '.join([str(card) if not hide or i == 0 else 'Unknown' for i, card in enumerate(cards)])}")

    def print_side_has(self, side, hand):
        print(f"{"You now have" if side == Game.CURRENT_PLAYER else "The dealer has"}: {str(hand)}")
        
        
        