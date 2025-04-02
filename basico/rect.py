import pygame
from basico.tools import get_color
from basico.window import Window
from typing import List,Tuple

class Rect:
    def __init__(self,
                 size:List[int]|Tuple[int,int]=[100,50],
                 pos:List[int]|Tuple[int,int]=[0,0],
                 color:str|List[int]|Tuple[int,int,int]="white",
                 border:int = 0):
        self.size = size
        self.pos = pos
        self.color = get_color(color)
        self.rect = pygame.Rect(pos[0],pos[1],size[0], size[1])
        self.border= border

    def draw(self,
             window:pygame.Surface|Window,
             pos:List[int]|Tuple[int,int]=None):
        if pos:
            self.pos = pos
        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]
        pygame.draw.rect(surface=window,
                         color=self.color,
                         rect=self.rect,
                         width=self.border)
    def clickpoint(self, pos):
        return self.rect.collidepoint(pos)
    
    def get_rect(self):
        return self.rect
    def get_size(self):
        return self.size
    def get_color(self):
        return self.color
    def get_pos(self):
        return self.pos