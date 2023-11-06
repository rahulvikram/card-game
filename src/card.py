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