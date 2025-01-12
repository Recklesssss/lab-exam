import pygame

def draw_nested_triangles():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Flipped Inner Triangle")
    screen.fill((255, 255, 255))  # White background

    # Blue color
    blue = (0, 0, 255)
    
    outer_triangle = [(250, 50), (100, 400), (400, 400)]
 
    flipped_inner_triangle = [(250, 350), (175, 150), (325, 150)]

    pygame.draw.polygon(screen, blue, outer_triangle)
    pygame.draw.polygon(screen, (255, 255, 255), flipped_inner_triangle)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

draw_nested_triangles()
