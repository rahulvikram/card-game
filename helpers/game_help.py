import pygame
import math # needed for card width scaling
from constants import *

# helper functions for the game window

# scales the card images down based on player and card count
def scale_image(img, players):
    img = pygame.transform.scale(img, (WIDTH/players/math.e, HEIGHT/players))
    return img

# prompts user for number of players
def player_input():
    try:
        player_input = input("Number of players: ")
        player_count = int(player_input)
        return player_count
    except:
        print("Error. Enter a number.")
        return player_input()
 
# prompts user for amount of cards per player
def card_input():
    try:
        card_input = input("Cards per player: ")
        card_count = int(card_input)
        return card_count
    except:
        print("Error. Enter a number.")
        return card_input()
