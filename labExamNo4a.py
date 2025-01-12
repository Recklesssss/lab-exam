import pygame
from pygame.locals import *

def draw_red_line(screen):
    red = (255, 0, 0)
    pygame.draw.line(screen, red, (50, 50), (250, 50), 3)

def draw_nested_triangles(screen):
    blue = (0, 0, 255)

    outer_triangle = [(250, 50), (100, 400), (400, 400)]
    flipped_inner_triangle = [(250, 350), (175, 150), (325, 150)]

    pygame.draw.polygon(screen, blue, outer_triangle)
    pygame.draw.polygon(screen, (255, 255, 255), flipped_inner_triangle)

def draw_purple_point(screen):
    purple = (128, 0, 128)
    pygame.draw.circle(screen, purple, (250, 250), 5)  

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("My Canvas")
    screen.fill((255, 255, 255))  # White background

    draw_red_line(screen)
    draw_nested_triangles(screen)
    draw_purple_point(screen)

    pygame.display.flip()  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_F1:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
