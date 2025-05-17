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
                 title:Text|str,
                 RectValues:Rect,
                 command: callable = None,
                 background: str|Image = None,
                 tags:callable = None):
        self.window = window
        if type(title) == str:
            self.title = Text(title)
        else:
            self.title = title
        self.rect = RectValues
        self.command = command
        self.background = background
        self.tags = tags
        self.color = RectValues.color
        self.validation_temp = True
        self.verfy_press = False
        self.gambiarra_verify = False
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
    def run(self, pos: pygame.mouse = None):
        if pos is not None:      
            self.verfy_press = self.rect.clickpoint(pos=pos)
        else:
            self.verfy_press = True
        if self.verfy_press:
            if self.command is not None:
                self.gambiarra_verify = True
                self.command()
    def get_title(self):
        return self.title.text
    def get_pos(self):
        return self.rect.get_pos()
    def get_size(self):
        return self.rect.get_size()
    def set_title(self, new_title:str):
        self.title.text = new_title
    def set_temp_color(self,color:str):
        self.rect.color = color
    def set_size(self,size:List[int]):
        self.rect.set_size(size)
    def set_pos(self, pos):
        self.rect.set_pos(pos)
    def get_clicked(self):
        if self.verfy_press:
            return True
        else:
            return False
    @property
    def press(self):
        gambiarra = self.get_clicked()
        return gambiarra
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
        button.set_pos([x, y])  # usa método da classe Rect se disponível, senão set diretamente
        w, h = button.get_size()

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
        center = (int(size_window[0] / 2 - button.rect.size[0] / 2), button.rect.pos[1])
        return center
    if tags == "y":
        center = (button.rect.pos[0], int(size_window[1] / 2 - button.rect.size[1] / 2))
        return center
    if tags == "j":
        center = (int(size_window[0] / 2 - button.rect.size[0] / 2), int(size_window[1] / 2 - button.rect.size[1] / 2))
        return center

class DefauthButton(ABC):
    def __init__(self):
        self.size = [300,50]
        self.color = "white"
        self.color_title = "black"
        