import random
import sys

class Card:
    def __init__(self, value, color, suit):
        self.value = value
        self.color = color
        self.suit = suit

    # Plays the card from the current deck
    def play(self, start_hand, end_hand):
        try:
            end_hand.append(self)
            start_hand.remove(self)
        except:
            pass

def init_deck():

    sorted_deck = [Card(value, 'black', 'spades') for value in range(1,14)]
    sorted_deck.extend([Card(value, 'black', 'clubs') for value in range(1,14)])
    sorted_deck.extend([Card(value, 'red', 'hearts') for value in range(1,14)])
    sorted_deck.extend([Card(value, 'red', 'diamonds') for value in range(1,14)])
    
    return sorted_deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def is_sorted(deck):
    sorted = init_deck()
    for x in range(len(deck)):
        if deck[x].value == sorted[x].value and deck[x].color == sorted[x].color and deck[x].suit == sorted[x].suit:
            continue
        else:
            return False

    return True

    
def deal_cards(players, deck, amount):
    if players * amount > len(deck):
        sys.exit("Error: Not enough cards.")
        
    hands = [[] for n in range(players)] # stores each player's hand

    shuffle(deck) # shuffle the deck
    for hand in hands:
        hand.extend(deck[0:amount])
        del deck[0:amount]

def sort_deck(deck):
    while is_sorted(deck) != True:
        for x in range(len(deck)): # for each card in deck
            for y in range(len(deck)):
                # if current card color is red and next card color is black
                if deck[x].color > deck[x+1].color:
                    # Swap the cards
                    deck[x], deck[x+1] = deck[x+1], deck[x] 

def print_deck(deck):
    for card in deck:
        print(f"{card.color} {card.value} of {card.suit}")
        
print_deck(shuffle(init_deck()))