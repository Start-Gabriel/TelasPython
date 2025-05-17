from basico.window import Window
from basico.rect import Rect
import basico.tools as tools
from typing import List
import pygame

class WindowVenda:
    def __init__(self):
        self.size = [800,600]
        self.color = tools.get_color("gray")
        self.background = None
        self.window = Window(size= self.size,
                             color= self.color,
                             background= self.background).pack()
        #-----------PRINCIPAL VALUES---------------------------
        self.SPACE = 10
        self.PIXEL = 1
        #---------RECTS BORDER VALUES -------------------------
        self.PRODUCTS_SIZE_Y = 60
        #---------PERCENT PRODUTOS VENDIDOS 
        self.PERCENT = 50
        self.PERCENT = self.PERCENT/100
        #----------START FUNCTIONS ----------------------------
    def draw(self):
        return self.generate_rects()
    def generate_rects(self):
        self.rects = []

        self.border = Rect(size=[self.size[0]-self.SPACE*2,
                     self.size[1]-self.SPACE*2],
                   pos=[self.SPACE, self.SPACE],
                   color="black",
                   border=self.PIXEL)
        self.rects.append(self.border)

        self.products = Rect(size=[self.border.get_size()[0]-self.SPACE*2,
                       self.PRODUCTS_SIZE_Y],
                     pos=[self.border.get_pos()[0]+self.SPACE, self.border.get_pos()[1]+self.SPACE],
                     color="black",
                     border=self.PIXEL)
        self.rects.append(self.products)

        self.pesquisa = Rect(size=[self.products.get_size()[0]/2-self.SPACE/2,
                       self.PRODUCTS_SIZE_Y],
                     pos=[self.border.get_pos()[0]+self.SPACE, self.products.get_pos()[1]+self.PRODUCTS_SIZE_Y+self.SPACE],
                     color="black",
                     border=self.PIXEL)
        self.rects.append(self.pesquisa)

        self.pesquisa_cod = Rect(size=[self.products.get_size()[0]/2-self.SPACE/2,
                           self.PRODUCTS_SIZE_Y],
                     pos=[self.border.get_pos()[0]+self.SPACE*2+self.pesquisa.get_size()[0], self.products.get_pos()[1]+self.PRODUCTS_SIZE_Y+self.SPACE],
                     color="black",
                     border=self.PIXEL)
        self.rects.append(self.pesquisa_cod)

        self.produtos_vendidos = Rect(size=[self.products.get_size()[0], self.border.get_size()[1]*self.PERCENT],
                          pos=[self.pesquisa.get_pos()[0], self.pesquisa_cod.get_pos()[1]+self.SPACE+self.PRODUCTS_SIZE_Y],
                          color="black",
                          border=self.PIXEL)
        self.rects.append(self.produtos_vendidos)

        self.valor = Rect(size=[self.produtos_vendidos.get_size()[0]/2-self.SPACE/2, self.PRODUCTS_SIZE_Y*2],
                  pos=[self.produtos_vendidos.get_pos()[0], self.produtos_vendidos.get_pos()[1]+self.produtos_vendidos.get_size()[1]+self.SPACE],
                  color="black",
                  border=self.PIXEL)
        self.rects.append(self.valor)

        for rect in self.rects:
            rect.draw(self.window)
        return self.window
    def set_size(self, new_size:List[int]):
        self.size = new_size
    def set_color(self, new_color:List[int]):
        self.color = new_color
    def set_background(self, new_background:str):
        self.background = new_background
    def get_size(self):
        return self.size
    def get_color(self):
        return self.color
    def get_background_surface(self):
        return self.background
    def get_rects(self):
        return self.rects
