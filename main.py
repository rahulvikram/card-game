from PIL import Image

from src.deck import Deck
from src.player import Player
from src.card import Card

# init deck
deck = Deck()

deck.shuffle()

players = deck.deal(3, 8)

# opens images based on players' hands
for player in players:
    for card in player.hand:
        image = Image.open(fr"img\{card.value}{Card.symbols[card.suit]['img_tag']}.png")
        image.show()
