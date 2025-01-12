import pygame

def draw_nested_triangles():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Flipped Inner Triangle")
    screen.fill((255, 255, 255))  # White background

    # Blue color
    blue = (0, 0, 255)
    
    # Outer triangle
    outer_triangle = [(250, 50), (100, 400), (400, 400)]

    # Flipped inner triangle vertices adjusted to touch the outer triangle
    inner_triangle = [
        (250, 400),  # Bottom vertex touches the base of the outer triangle
        (175, 225),  # Left vertex touches the left edge of the outer triangle
        (325, 225)   # Right vertex touches the right edge of the outer triangle
    ]

    # Draw the triangles
    pygame.draw.polygon(screen, blue, outer_triangle)  # Outer triangle
    pygame.draw.polygon(screen, (255, 255, 255), inner_triangle)  # Inner triangle

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

draw_nested_triangles()
