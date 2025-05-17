from basico.button import Button
from basico.rect import Rect
from basico.input import Input
from basico.text import Text
from basico.table import Table
from basico.window import Window
from basico.popup import PopUp
import basico.button as button_tools
import basico.tools as tools
from windows.window_venda import WindowVenda

import pygame
pygame.init()


class TelaVenda:
    def __init__(self, window:pygame.Surface = None):
        
        if window is not None:
            self.window = window
        else:
            self.window = Window(size=[800,600], color="gray").pack()
        self.__defaut_size = [100,50]
        self.valor_total = []
        self.valor = ''
        self.nome = ''
        self.list_principal_products = []
        self.RECTS = WindowVenda()
        self.RECTS.generate_rects()
        self.SPACE = 5
    def draw(self):
        self.generate_button_produtos_principais()
    def generate_button_produtos_principais(self):
        from valores.pao import Pao
        from valores.quitandas import Quitandas
        from valores.diversos import Diversos
        self.pao = Pao(window=self.window,
                       pos=[self.RECTS.products.get_pos()[0]+self.SPACE,
                            self.RECTS.products.get_pos()[1]+self.SPACE])
        self.pao.set_size([(self.RECTS.products.get_size()[0]-self.SPACE*4)/3, self.__defaut_size[1]])
        self.pao.draw()
        self.list_principal_products.append(self.pao)
        self.quitandas = Quitandas(window=self.window,
                                   pos=[0,100])
        self.quitandas.set_pos([self.pao.get_pos()[0]+self.pao.get_size()[0]+self.SPACE, self.pao.get_pos()[1]])
        self.quitandas.set_size(self.pao.get_size())
        self.quitandas.draw()
        self.list_principal_products.append(self.quitandas)
        self.diversos = Diversos(window=self.window,
                                 pos=[self.quitandas.get_pos()[0]+self.quitandas.get_size()[0]+self.SPACE, self.quitandas.get_pos()[1]])
        self.diversos.set_size(self.pao.get_size())
        self.diversos.draw()
        self.list_principal_products.append(self.diversos)
    def run(self,pos):
        for but in self.list_principal_products:
            but.run(pos)
            if but.get_press():
                print(f"oque diabos isso printa{but.get_venda()}")
                
    def set_window(self, window:pygame.Surface):
        self.window = window.copy()
    