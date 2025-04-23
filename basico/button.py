import pygame
from basico.window import Window
from typing import Union, List, Tuple
from basico.text import Text
import basico.tools as tools
from basico.image import Image
from basico.rect import Rect
from abc import ABC

class Button:
    def __init__(self,
                 window: pygame.Surface|Window,
                 title:Text,
                 RectValues:Rect,
                 command: callable = None,
                 background: str|Image = None,
                 tags:callable = None):
        self.window = window
        self.title = title
        self.rect = RectValues
        self.command = command
        self.background = background
        self.tags = tags
    def draw(self):
        self.__title_pos =  tools.get_mid(self.rect.get_pos(),self.rect.get_size(),self.title.get_size_tuple())
        self.rect.draw(window=self.window, pos= self.rect.get_pos())
        if self.background:
            self.background.draw(window=self.window,
                                 pos=self.pos,
                                 size=self.rect.get_size())
        self.title.draw(self.window,self.__title_pos)
        if self.tags:
            self.tags()
    def run(self, pos: pygame.mouse):      
        self.press = self.rect.clickpoint(pos=pos)
        if self.press:
            if self.command is not None:
                self.command()
    def get_pos(self):
        return self.rect.get_pos()
    def set_title(self, new_title:str):
        self.title.text = new_title
    
def alight_buttons(start_pos: Union[List[int], Tuple[int, int]],
                   orientation: str,
                   space: int,
                   buttons: List[Button]):
    """
    Alinha uma lista de botões horizontal ou verticalmente.

    Args:
        start_pos (List[int] | Tuple[int, int]): Posição inicial (x, y).
        orientation (str): Direção de alinhamento ('x' para horizontal, 'y' para vertical).
        space (int): Espaço entre os botões.
        buttons (List[Button]): Lista de instâncias da classe Button.
    """
    x, y = start_pos

    for button in buttons:
        button.rect.set_pos([x, y])  # usa método da classe Rect se disponível, senão set diretamente
        w, h = button.rect.get_size()

        if orientation == "x":
            x += w + space
        elif orientation == "y":
            y += h + space


def get_center_button(size_window: Union[List[int], Tuple[int, int]],
                      button: Button,
                      tags: str = "j"):
    """
    Obtém as coordenadas centrais para posicionar um botão no centro da janela.

    Args:
        size_window (Union[List[int], Tuple[int, int]]): O tamanho da janela onde o botão será centralizado.
        button (Button): O botão a ser centralizado.
        tags (str, optional): Define se a centralização será horizontal ('x'), vertical ('y') ou total ('j'). Defaults to "j".

    Returns:
        Tuple: As coordenadas centrais (x, y) para o botão.
    """
    if tags == "x":
        center = (int(size_window[0] / 2 - button.size[0] / 2), button.pos[1])
        return center
    if tags == "y":
        center = (button.pos[0], int(size_window[1] / 2 - button.size[1] / 2))
        return center
    if tags == "j":
        center = (int(size_window[0] / 2 - button.size[0] / 2), int(size_window[1] / 2 - button.size[1] / 2))
        return center

class DefauthButton(ABC):
    def __init__(self):
        self.size = [300,50]
        self.color = "white"
        self.color_title = "black"
        