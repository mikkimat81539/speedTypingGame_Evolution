import pygame
from includeFont import fontText

pygame.init()

class TextBox:
    def __init__(self, x_pos,  y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = str(color)
        self.get_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
    
    def drawBox(self, screen):
        return pygame.draw.rect(screen, self.color, self.get_rect, 5)
    
    def textboxFont(self, event):
        if event.key == pygame.K_RETURN:
            self.text = ""
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += event.unicode