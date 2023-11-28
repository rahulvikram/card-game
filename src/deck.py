# required modules
import random
import sys

# import helper functions
sys.path.append('/Users/rahul/OneDrive - Oregon State University/Documents/Coding/projects/card-game/helpers/')
from sort_help import value_func, suit_func
from values import val_dict # decksort alg: converts AJQK into respective num values

# import classes
from card import Card 
from player import Player

# TODO: finish class deck
class Deck:

    # initializes a deck of cards; these vars are instance variables, belonging to each instance of a deck
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

    # shuffle deck of cards
    def shuffle(self):
        random.shuffle(self.cards)                                                                                                                                                                                                                                                                             

    # deals cards to players
    def deal(self, player_count, card_count):
        players = []

        # makes sure the cards to deal isn't more than the total cards in the deck
        if player_count*card_count > len(self.cards):
            print("Error: Not enough cards in deck.\n")
            sys.exit()
        else: # if enough cards are in deck
            self.shuffle() # shuffle the deck

            # create new players, add them to player list, and give them cards from shuffled deck
            for i in range(player_count):
                new_player = Player() # create new player
                new_player.hand.extend(self.cards[0:card_count]) # add the specified amt of cards to the player's hand
                self.cards[0:card_count] = [] # remove these cards from the original deck, completing the deal
                players.append(new_player) # add new player to the players deck                  

        return players
        

    def draw(self):
        pass

    def sort_deck(self):
        pass

    def is_sorted(self):
        pass