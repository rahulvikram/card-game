import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # prevents pygame welcome message
import pygame
import sys

# import src classes
from src.deck import Deck
from src.player import Player
from src.card import Card

# import game helpers
from helpers.constants import *
from helpers.game_help import *

# init deck
deck = Deck()

# take user input for amt of players and cards
# player_count = player_input()
# card_count = card_input()

# deal cards to players based on user input
players = deck.deal(player_input(), card_input())

# initialize pygame and its display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True # needed so window does not hang

# while window is running
while running:
    # check if the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            running = False
            sys.exit('Program closed.\n')

    # fill screen background
    screen.fill(BLACK)

    w_card, w_height = 0, 0
    # opens images based on players' hands
    for player in players:
        for card in player.hand:            
            # display image on screen
            if card.faceup == True:
                img = scale_image(pygame.image.load(card.filename), len(players))
                screen.blit(img, (w_card, w_height))
            else:
                img = scale_image(pygame.image.load(Card.backfile), len(players))
                screen.blit(img, (w_card, w_height))
            w_card += 60 # print next card with gap from previous
        w_height += img.get_height() # print next player's hand below
        w_card = 0 # reset position of next player's hand for reprint


    # update display to show work
    pygame.display.flip()
