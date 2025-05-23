import pygame
from typing import Union,List,Tuple
import basico.tools as tools
from basico.image import Image
from abc import ABC

class Window:
    def __init__(self,
                 size:Union[List[int],Tuple[int,int,int]],
                 color:Union[str,Tuple[int,int,int]],
                 background:str = None):
        """Cria uma janela

        Args:
            size (Union[List[int],Tuple[int,int,int]]): Tamanho da janela [altura,largura]
            color (Union[str,Tuple[int,int,int]]): Cor da janela, nome ou valor RGB(255,255,255)
            background (str, optional): Caminho para imagem de fundo da janela. Defaults to None.
        """

        self.size = size
        self.color = tools.get_color(color)
        self.background = background
        self.START_COORDINATES = (0,0)
        self.window = pygame.display.set_mode((self.size))
        pygame.display.set_caption(title="PANIFICADORA DELLIS")
        #self.icon = Image("images/onda.jpg")
        #pygame.display.set_icon(self.icon.get_surface())
        
    def pack(self):
        """Chamada para iniciar a tela

        Returns:
            Surface: Objeto surface do pygame
        """
        self.window.fill(self.color)
        if self.background is not None:
            self.background = tools.get_image(self.background)
            self.background = pygame.transform.scale(self.background,self.size)
            self.window.blit(self.background,self.START_COORDINATES)
        return self.window

class DefauthWindow(ABC):
    def __init__(self):
        self.size = [1000,600]
        self.color = "black"
        self.background = "images/pantano.jpg"
