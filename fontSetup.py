import pygame

pygame.init()

class setupFont:
    def __init__(self, text, size, x_pos, y_pos):
        self.text = text
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def displayFont(self, screen):
        createFont = pygame.font.Font("m5x7.ttf", self.size)
        renderFont = createFont.render(self.text, False, "black")
        screen.blit(renderFont, (self.x_pos, self.y_pos))