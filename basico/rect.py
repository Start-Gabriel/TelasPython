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
        self.border= border
        self.generate_Surface(pos=self.pos, size=self.size)
    def generate_Surface(self,pos:List[int]=None,size:List[int]=None):
        generate_pos = pos if pos else self.pos
        generate_size = size if size else self.size
        self.rect = pygame.Rect(generate_pos[0],generate_pos[1],generate_size[0], generate_size[1])
    def draw(self,
         window: pygame.Surface | Window,
         pos: List[int] | Tuple[int, int] = None):
    
        draw_pos = pos if pos else self.pos

        self.rect.left = draw_pos[0]
        self.rect.top = draw_pos[1]

        pygame.draw.rect(surface=window,
                        color=self.color,
                        rect=self.rect,
                        width=self.border)

    def clickpoint(self, pos = None):
        if pos is not None:
            return self.rect.collidepoint(pos)
    
    def get_rect(self):
        return self.rect
    def get_size(self):
        return self.size
    def get_color(self):
        return self.color
    def get_pos(self):
        return self.pos
    def set_pos(self,pos):
        self.pos = pos
        self.generate_Surface(pos=pos)
    def set_size(self, size:List[int]):
        self.size = size
        self.generate_Surface(size=size)
    def center_x(self, window:pygame.Surface):
        self.pos = [window.get_size()[0]/2 - self.size[0]/2, self.pos[1]]