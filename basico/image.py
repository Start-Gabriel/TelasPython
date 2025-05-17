import pygame
from typing import List,Tuple
from basico.tools import furp
pygame.init()


class Image:
    def __init__(self,
                 path:str,
                 size:List[int]|Tuple[int,int]=None):
        self.path = furp(path)
        self.size = size
        self.image_surface = pygame.image.load(self.path)
    def draw(self,
             window:pygame.Surface,
             pos:List[int]|Tuple[int,int],
             size:List[int]|Tuple[int,int]=None):
        from basico.window import Window
        try:
            if self.size:
                self.image_scale = pygame.transform.scale(self.image_surface, self.size)
                window.blit(self.image_scale, pos)
                print(f"1")
            if size:
                self.size = size
                self.image_scale = pygame.transform.scale(self.image_surface, self.size)
                print(f"2{self.size}")
                window.blit(self.image_scale, pos)
        except:
            print(f"erro ao inserir imagem {self.path}")
    def get_path(self):
        return self.path
    def get_size(self):
        return self.size
    def get_surface(self):
        return self.image_surface