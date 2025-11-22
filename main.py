import pygame, sys
from fontSetup import setupFont
from textboxSetup import TextBox
from game_play import gameplayWords

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Speed Typing Game")

def gamePlay():
    wordList_index = 0

    gameplayHeader = setupFont(f"Type [{gameplayWords.game_words(wordList_index)}] than press ENTER", 40, 60, 40)

    gameplayTextBox = TextBox(90, 100, 320, 40, "black", 5, "")
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                gameplayTextBox.textboxHandling(event)
            
                if event.key == pygame.K_RETURN:
                    wordList_index += 1

                    if wordList_index >= 4:
                        wordList_index = 3
        
        screen.fill("white")

        # RENDER CODE HERE
        gameplayHeader.displayFont(screen)
        gameplayTextBox.drawBox(screen)
        gameplayTextBox.textboxFont(screen)

        pygame.display.flip()

def mainMenu(screen):
    # TextBox
    textbox = TextBox(209, 117, 70, 33, "black", 2, None)

    # Fonts
    headerFont = setupFont("Speed Typing Game", 50, 100, 70)

    paragraphFont = setupFont(f"Press ENTER to begin", 30, 155, 120)

# GAME LOOP
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textbox.color = "gray"
                    textbox.border = 0
                    gamePlay()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    textbox.color = "black"
                    textbox.border = 2

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
        
        screen.fill("white")

        # RENDER CODE HERE
        textbox.drawBox(screen)
        headerFont.displayFont(screen)
        paragraphFont.displayFont(screen)

        pygame.display.flip()

mainMenu(screen)
