# creating the text, textbox and mechanics behind the texts
import pygame

pygame.init()

class createText:
    def __init__(self, x_pos, y_pos, color, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = "Type [hello] than press ENTER"
        self.color = str(color)
        self.size = size
        

    def setText(self, screen):
        # First: create a font
        sysFont = pygame.font.Font('m5x7.ttf', self.size)

        # Second: Render the font
        renderText = sysFont.render(self.text, False, self.color, None)

        # Third: Set position
        setText = screen.blit(renderText, (self.x_pos, self.y_pos))
        return setText

class textBox:
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = str(color)
        self.get_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
    
    def drawBox(self, screen):
        return pygame.draw.rect(screen, self.color, self.get_rect, 5)

class userInput_Text:
    def __init__(self, textbox):
        self.text = ""
        self.textbox = textbox
        self.max_length = 25

    def handle_Textevent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.text = ""

            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # Delete last character
            else:
                if len(self.text) < self.max_length:
                    self.text += event.unicode

    def draw_textInput(self, screen):
        sysFont = pygame.font.Font('m5x7.ttf', 40)

        # updateText = self.text.replace("\r", "")
        
        textbox_x = self.textbox.x_pos + 10
        textbox_y = self.textbox.y_pos + (self.textbox.height // 8)
        
        renderText = sysFont.render(self.text, False, "black", None)
        setText = screen.blit(renderText, (textbox_x, textbox_y))
        return setText
