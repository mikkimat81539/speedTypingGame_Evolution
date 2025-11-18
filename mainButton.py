import pygame

pygame.init()

class enterButton:
    def __init__(self, x_pos, y_pos, width, height, color, border):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = str(color)
        self.border = border
        self.get_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def drawButton(self, screen):
        return pygame.draw.rect(screen, self.color, self.get_rect, self.border, 7)
    
    def buttonChange(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.color = "gray"
            self.border = 0
        
        else:
            self.color = "black"
            self.border = 2
                

