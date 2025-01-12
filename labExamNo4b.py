import pygame
from pygame.locals import *

def draw_red_line(screen):
    red = (255, 0, 0)
    pygame.draw.line(screen, red, (50, 50), (250, 50), 3)
    pygame.display.flip()
