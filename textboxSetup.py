import pygame

pygame.init()

class TextBox:
    def __init__(self, x_pos, y_pos, width, height, color, border, text):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = str(color)
        self.border = border
        self.text = text
        self.get_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def drawBox(self, screen):
        return pygame.draw.rect(screen, self.color, self.get_rect, self.border)