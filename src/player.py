class Player:
    def __init__(self):
        self.hand = [] # new player's hand is initially empty, will be populated at runtime
        pass

    def print_hand(self):
        for card in self.hand:
            print(card)
        print('\n')

    def play_card(self, dest_deck, value, suit):
        if len(self.hand) == 0:
            print("Error: hand is empty.")
            return;
        
        # if there are cards in the hand
        for card in self.hand: # for each card in the hand
            # if card exists in the hand
            if card.value == value and card.suit == suit:
                dest_deck.cards.insert(0,card) # prepend card to destination deck (the pile)
                self.hand.remove(card) # removes card from player's hand

