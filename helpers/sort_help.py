import sys
sys.path.append('/Users/rahul/OneDrive - Oregon State University/Documents/Coding/projects/card-game/src/')
from card import Card

# used for decksort algorithm
val_dict = {
    "A": 1,
    "J": 11,
    "Q": 12,
    "K": 13
}

# helper functions in sort_deck() function: lets deck.sort() know what attr. to sort cards by 
# value function: helps sort the deck by card value
def value_func(card):
    if isinstance(card.value, str): # if the value is any of AJQK 
        return val_dict[card.value]
    
    return card.value # if the value is a number

# after value sort, this sorts the deck by its suit
def suit_func(card):
    return Card.symbols[card.suit]['sort_index']