import random
import sys

# TODO: define Deck class
class Deck:
    def __init__(self) -> None:
        pass

# TODO: define Pile class
class Pile:
    def __init__(self, test):
        pass

class Card:
    def __init__(self, value, color, suit, faceup):
        self.value = value
        self.color = color
        self.suit = suit
        self.faceup = faceup

    # Plays the card from the current deck
    def play(self, start_hand, end, faceup):
        try:
            end.append(self) # adds the card to the pile (end destination)
            start_hand.remove(self) # removes the card from the hand of the player who played
            faceup = True; # card has been played, so the card is now face up
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