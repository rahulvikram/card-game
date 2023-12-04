class Card:

    symbols = {
        "spades":
        {
            "icon":"♠",
            "sort_index": 1
        },
        "clubs":
        {
            "icon":"♣",
            "sort_index": 2
        },
        "hearts":
        {
            "icon":"♥",
            "sort_index": 3
        },
        "diamonds":
        {
            "icon":"♦",
            "sort_index": 4
        }
    } # list of symbols for the card

    # init card with instance vars
    def __init__(self, value, suit, faceup):
        self.value = value
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
    
    # dunder method overriding print() for print_deck function
    def __repr__(self):
        return f"{self.value}{Card.symbols[self.suit]['icon']}" # e.g. (4♣)

    # reveals the card
    def reveal(self):
        # card can only be shown if it's not already being shown
        if not self.faceup:
            self.faceup = True