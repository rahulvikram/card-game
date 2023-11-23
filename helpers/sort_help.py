# helper functions in sort_deck() function: lets deck.sort() know what attr. to sort cards by 
def value_func(card):
    return card.value

def suit_func(card):
    return card.suit