import pygame

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Speed Typing Game")

# GAME LOOP
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    # RENDER CODE HERE

    pygame.display.flip()

pygame.quit()
