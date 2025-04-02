import pygame
from typing import Union, List, Tuple
import sys
from basico.button import Button
from basico.rect import Rect
from basico.text import Text

import basico.tools as tools
pygame.init()

class Input:
    def __init__(self,
                 buttonValues:Button):
        
        buttonValues.command = self.input_text
        self.input_button = buttonValues
        self.input_button.title = Text("bcta",buttonValues.title.color,buttonValues.title.background_color)
        self.backup = buttonValues.window.copy()
        self.texts=""
    def draw(self):
        self.input_button.draw()
    def run(self,pos:List[int]|Tuple[int,int]):
        self.loop = True
        self.input_button.run(pos=pos)
    def input_text(self):
        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_button.rect.rect.collidepoint(pygame.mouse.get_pos()) == False:
                        self.loop = False
                    else:
                        pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pass
                    if event.key == pygame.K_BACKSPACE:
                        self.texts = self.texts[:-1]
                        self.update()
                    else:
                        self.texts += event.unicode
                        self.update()
                        print(self.texts)
            pygame.display.flip()
    def update(self):
        self.input_button.title = Text(self.texts,self.input_button.title.color,self.input_button.title.background_color)
        self.input_button.draw()