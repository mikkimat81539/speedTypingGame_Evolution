import pygame, sys, time
from mainButton import enterButton
from includeFont import fontText
from levels import LevelTitle
from textbox import TextBox

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Speed Typing Game")


def playLevelOne(): # Levels of the game
    text_box = TextBox(100, 110, 300, 40, "black")
    index = 0  # start at the first word

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    index += 1
                    if index >= 6:
                        index = 5  # stop the level

        screen.fill("white")

        # RENDER YOUR GAME HERE
        LevelTitle.levelOneTitle(screen)
        LevelTitle.levelOne(screen, index)
        
        # START TIME
        startTime = time.perf_counter()
        
        # CODE HERE
        text_box.drawBox(screen)
        
        # END TIME
        endTime = time.perf_counter()

        # ELAPSED TIME
        elapsedTime = round((endTime - startTime), 2)
        elapsedTimeFont = fontText(f"{elapsedTime}", 300, 200, 20)
        elapsedTimeFont.drawFont(screen)

        pygame.display.flip()

        pygame.display.update()

def mainMenu():  # Main Menu Screen
    # HEADER TEXT
    headerText = fontText("Speed Typing Game", 100, 50, 50)

    # BUTTON
    button = enterButton(191, 110, 65, 30, "black", 2)

    # PARAGRAPH TEXT
    paragraphText = fontText(f"Press ENTER key to start", 135, 110, 30)

    # Screen Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    playLevelOne()

        screen.fill("white")

        # RENDER YOUR GAME HERE
        button.buttonChange()

        button.drawButton(screen)
        headerText.drawFont(screen)
        paragraphText.drawFont(screen)

        pygame.display.flip()

mainMenu()
