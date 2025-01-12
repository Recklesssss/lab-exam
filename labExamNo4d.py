import pygame
from pygame.locals import *

def draw_purple_point(screen):
    purple = (128, 0, 128)
    pygame.draw.circle(screen, purple, (150, 150), 3)  # Radius of 3
    pygame.display.flip()
