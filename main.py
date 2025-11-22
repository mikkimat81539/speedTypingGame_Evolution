import pygame, sys, time
from fontSetup import setupFont
from textboxSetup import TextBox
from game_play import gameplayWords

from random_word import RandomWords

pygame.init()

# SCREEN
screen = pygame.display.set_mode((600, 250))
pygame.display.set_caption("Speed Typing Game")


def gameOver():
    game_over = setupFont("Game Over", 50, 205, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill("white")

        game_over.displayFont(screen)

        pygame.display.flip()

def gamePlay():
    wordList_index = 0
    words = gameplayWords.game_words()

    gameplayTextBox = TextBox(100, 100, 320, 40, "black", 5, "")

    # Time
    timeLimit = 60
    startTime = time.time()
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                gameplayTextBox.textboxHandling(event)
            
                if event.key == pygame.K_RETURN:
                    if gameplayTextBox.text !=  words[wordList_index]:
                        timeLimit -= 5
                        print(gameplayTextBox.text)
                    else:
                        timeLimit += 5
                    
                    gameplayTextBox.text = "" # clear textbox
                    
                    wordList_index += 1
                    if wordList_index >= len(words):
                        randomW = RandomWords().get_random_word()
                        words.append(randomW)
        
        screen.fill("white")

        # RENDER CODE HERE
        gameplayHeader = setupFont(f"Type {words[wordList_index]} than press ENTER", 40, 40, 40)
        gameplayHeader.displayFont(screen)
        gameplayTextBox.drawBox(screen)
        gameplayTextBox.textboxFont(screen)

        endTime = time.time()
        elapsedTime = round((endTime - startTime), 2)
        
        timer = timeLimit - int(elapsedTime)

        if elapsedTime > timeLimit:
            gameOver()
        else:
            setupFont(timer, 70, 450, 150).displayFont(screen)

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
