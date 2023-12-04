from src.deck import Deck
from src.player import Player


# init deck
deck = Deck()

deck.shuffle()

players = deck.deal(3, 8)
for player in players:
    
    player.print_hand()

