import pygame
from typing import List,Tuple
from basico.tools import furp
pygame.init()


class Image:
    def __init__(self,
                 path:str,
                 size:List[int]|Tuple[int,int]):
        self.path = furp(path)
        print(self.path)

Image("button\image.py",[199,100])