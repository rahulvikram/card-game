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

    # reveals the card
    def show(self):
        # card can only be shown if it's not already being shown
        if not self.faceup:
            print(f"{self.value} of {self.suit}") # e.g. (4 of spades)
            self.faceup = True;


# TODO: define Deck class
class Deck:
    def __init__(self) -> None:
        pass
    
    # initializes a deck of cards
    def init_deck(self):
        sorted_deck = [Card(value, 'black', 'spades', False) for value in range(1,14)] # initialize all spade cards

        # append all other suit cards to the deck
        sorted_deck.extend([Card(value, 'black', 'clubs', False) for value in range(1,14)]) 
        sorted_deck.extend([Card(value, 'red', 'hearts', False) for value in range(1,14)])
        sorted_deck.extend([Card(value, 'red', 'diamonds', False) for value in range(1,14)])
        
        return sorted_deck
    
    # reveals all cards in the deck
    def show_deck(self):
        pass;


# TODO: define Pile class
class Pile:
    def __init__(self, test):
        pass

    # draw a card from the pile
    def draw(self):
        pass