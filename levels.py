import pygame, time
from includeFont import fontText
from levelWords import *

pygame.init()

class LevelTitle:
    @staticmethod
    def levelOneTitle(screen):
        levelOne = fontText("LEVEL 1", 190, 10, 50)
        return levelOne.drawFont(screen)
    
    def levelOne(screen, index):
        # WORDS
        level1_words = levelWords.levelOneWords(index)
        levelOneFont = fontText(f"Type [{level1_words}] than press ENTER", 50, 60, 40)

        return levelOneFont.drawFont(screen), index    

    def gamePlay():
        pass