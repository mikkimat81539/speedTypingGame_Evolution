import pygame
from fontSetup import setupFont
from textboxSetup import TextBox

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Speed Typing Game")

# TextBox
textbox = TextBox(209, 117, 70, 33, "black", 2, "ENTER")

# Fonts
headerFont = setupFont("Speed Typing Game", 50, 100, 70)

paragraphFont = setupFont(f"Press {textbox.text} to begin", 30, 155, 120)

def mainMenu(screen):
# GAME LOOP
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
        
        screen.fill("white")

        # RENDER CODE HERE
        headerFont.displayFont(screen)
        paragraphFont.displayFont(screen)
        textbox.drawBox(screen)

        pygame.display.flip()

mainMenu(screen)
