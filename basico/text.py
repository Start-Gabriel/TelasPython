from typing import List,Tuple
from basico.tools import insert_text, get_color

import pygame
class Text:
    def __init__(self,
                 text:str = "text",
                 color:str|Tuple[int,int,int] = "black",
                 background_color:str|Tuple[int,int,int]|List[int] = None,
                 size:int = 20):
        self.text = text
        self.color = get_color(color)
        self.background_color = get_color(background_color)
        self.size = size
        self.font = pygame.font.Font(None,self.size)
        self.text_render = self.font.render(self.text,
                                            True,
                                            self.color,
                                            self.background_color)
    def draw(self, window:pygame.Surface,pos:List[int]|Tuple[int,int]):
        window.blit(self.text_render,pos)
    def get_surface(self):
        return self.text_render
    def get_text(self):
        return self.text
    def get_color(self):
        return self.color
    def get_background_color(self):
        return self.background_color
    def get_size(self):
        return self.size
    def get_size_tuple(self):
        return self.text_render.get_size()
            