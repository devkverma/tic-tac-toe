import sys
import pygame
from constants import *

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

class Game:

    def __init__(self):
        pass

    def show_lines(self):
        pass

def main():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

main()
