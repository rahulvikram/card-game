class Card:
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

    def print_card(self):
        symbols = {"spades": "♠", "clubs": "♣", "hearts": "♥", "diamonds": "♦"} # list of symbols for the card
        print(f"{self.value}{symbols[self.suit]}") # e.g. (4♣)

    # reveals the card
    def show(self):
        # card can only be shown if it's not already being shown
        if not self.faceup:
            self.faceup = True