# required modules
import random

# import helper functions
from helpers.values import val_dict
from helpers.sort_help import value_func, suit_func

# import classes
from card import Card 
from player import Player

# TODO: finish class deck
class Deck:
    # initializes a deck of cards
    def __init__(self):
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.cards = [Card(value, suit, False) for suit in self.suits for value in self.values]
    
    # reveals all cards in the deck
    def show_deck(self):
        for card in self.cards:
            card.faceup == True;

    # prints every card in the deck
    def print_deck(self):
        for card in self.cards:
            card.print_card()


    # deals cards to players
    def deal(self, player_count):
        players = []
        for i in range(player_count):
            pass
        
        return players
        

    def shuffle(self):
        random.shuffle(self.cards)                                                                                                                                                                                                                                                                             

    def draw(self):
        pass

    def sort_deck(self):
        pass

    def is_sorted(self):
        pass

deck = Deck()


