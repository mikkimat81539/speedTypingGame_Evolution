import pygame
from typingText import createText
from typingText import textBox
from typingText import userInput_Text

pygame.init()

# SCREEN
screen = pygame.display.set_mode((600, 350))
pygame.display.set_caption("Speed Typing Game")

# Text
texts = createText(60, 42,"black", 50)

# TextBox
text_box = textBox(100, 130, 400, 50, "black")

# User Text
input_text = userInput_Text(text_box)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            input_text.handle_Textevent(event)

        screen.fill("white")

        # Render Game Here
        texts.setText(screen)
        text_box.drawBox(screen)
        input_text.draw_textInput(screen) 

        pygame.display.flip()

pygame.quit()
