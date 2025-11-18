import pygame

pygame.init()

class fontText:
    def __init__(self, text, x_pos, y_pos, size):
        self.text = str(text)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
    
    def drawFont(self, screen):
        createFont = pygame.font.Font("m5x7.ttf", self.size)

        updateFont = self.text.replace("\r", "")

        # textbox_x = text_box.x_pos
        # textbox_y = text_box.x_pos

        renderFont = createFont.render(updateFont, False, "black")
        screen.blit(renderFont, (self.x_pos, self.y_pos))
