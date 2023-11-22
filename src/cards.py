import random
import sys

from construct import Card, Deck, Pile

def shuffle(deck):
    random.shuffle(deck)
    return deck

def is_sorted(deck):
    sorted = Deck.init_deck();
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

# helper functions in sort_deck() function: lets deck.sort() know what attr. to sort cards by 
def color_func(card):
    return card.color
def value_func(card):
    return card.value
def suit_func(card):
    return card.suit

def print_deck(deck):
    for card in deck:
        print(f"{card.color} {card.value} of {card.suit}")

def sort_deck(deck):
    
    # sorts the whole deck by value and color
    deck.sort(key=value_func)
    deck.sort(key=color_func)
    
    # auto-sort by suit has the suits out of order, so we need to manually reorder them
    # creates black and red lists for splitting by color
    blacks = []
    reds = []

    # splits the deck by color into lists above
    for i in deck:
        if i.color == 'black':
            blacks.append(i)
        else:
            reds.append(i)

    # individually sorts each list of black and red cards
    blacks.sort(key=suit_func, reverse=True)
    reds.sort(key=suit_func, reverse=True)

    # adds new sorted black and red card lists to the main deck
    deck.clear()
    deck = blacks
    deck.extend(reds)
    
    # # prints deck
    # for i in deck:
    #     print(f"{i.value} of {i.suit}")
    
    return deck