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
    
    def textboxFont(self, screen):
        createFont = pygame.font.Font("m5x7.ttf", 40)
        renderFont = createFont.render(self.text, False, "black")
        screen.blit(renderFont, (self.x_pos + 10, self.y_pos + 3))

    
    def textboxHandling(self, event):
        if event.key == pygame.K_RETURN:
            self.text = ""
            
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            if len(self.text) < 27:
                self.text += event.unicode
                
