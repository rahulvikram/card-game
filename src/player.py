class Player:
    def __init__(self):
        self.hand = [] # new player's hand is initially empty, will be populated later on
        pass

    def print_hand(self):
        for card in self.hand:
            card.print_card()
        print('\n')