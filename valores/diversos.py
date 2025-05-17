from basico.button import Button
from basico.input import Input
from basico.rect import Rect
from basico.text import Text
from basico.table import Table
from basico.window import Window
from windows.window_venda import WindowVenda
from basico.popup import PopUp
from typing import List

import pygame
pygame.init()

class Diversos:
    def __init__(self,
                 window:pygame.Surface,
                 pos:List[int]):
        self.window = window
        self.pos = pos
        
        self.__defaut_size = [100,50]
        self.button_diversos = Button(window=self.window,
                                      title=Text(text="DIVERSOS"),
                                      RectValues=Rect(size=self.__defaut_size, pos=self.pos),
                                      command=self.generate_diversos)
        self.nr_itens = 5
        self.size_table = [300,50]
        self.pos_table = [self.window.get_size()[0]/2-self.size_table[0]/2, self.window.get_size()[1]/2 - (self.size_table[1]*self.nr_itens)/2]
        self.color_table = ("white", "gray")
        self.color_popup = "lightgray"
        
        self.CLOCK = pygame.time.Clock()
    def generate_diversos(self):
        self.products = self.set_table_products()
        self.table_products = Table(window=self.window,
                                    size= self.size_table,
                                    pos=self.pos_table,
                                    nr_itens=self.nr_itens,
                                    colors=self.color_table)
        self.pop_up = PopUp(window= self.window,
                            text=Text(""),
                            rectValues=Rect(size=[self.size_table[0],
                                                  self.size_table[1]*self.table_products.nr_itens+self.size_table[1]*2], 
                                            color=self.color_popup))
        self.pop_up.set_pos([self.table_products.get_pos()[0], self.table_products.get_pos()[1]-self.__defaut_size[1]])

        self.pop_up.draw()
        self.table_products.draw(self.products[0])
        

        self.loop = True
        while self.loop:
            self.verify_produto = [None, None]
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.verify_produto = self.table_products.run(pygame.mouse.get_pos())
                    if self.verify_produto is not None:
                        print(self.verify_produto)
                    
                    self.pop_up.close.run(pos=pos)
                    if self.pop_up.loop == False:
                        self.loop = False
                        
                if events.type == pygame.K_ESCAPE:
                    self.loop = False
                
            pygame.display.flip()
            self.CLOCK.tick(60)
                    
    
    def set_table_products(self):
        from bd_produtos import produtos
        self.cnn = produtos.conectar_banco("bd_produtos/produtos.db")
        self.all_products = produtos.listar_produtos_ordenados(conn=self.cnn)
        self.all_products_name = []
        self.all_products_value = []
        for produto in self.all_products:
            self.all_products_name.append(Button(window=self.window,
                                                 title=Text(f"{produto[1]}"),
                                                 RectValues=Rect(self.__defaut_size), 
                                                 command=self.vender),)
            self.all_products_value.append(Button(window=self.window,
                                                 title=Text(f"{produto[2]}"),
                                                 RectValues=Rect(self.__defaut_size)))
        return [self.all_products_name, self.all_products_value]
    def draw(self):
        self.button_diversos.draw()
    def vender(self):
        print("vendeu")
    def run(self, pos):
        self.button_diversos.run(pos=pos)
    def set_size(self, size:List[int]):
        self.button_diversos.set_size(size=size)
    def set_pos(self, pos:List[int]):
        self.button_diversos.set_pos(pos=pos)
    def set_pos_table(self, pos:List[int]):
        self.table_products.set_pos_table(pos=pos)
    
    def set_size_table(self, size:List[int]):
        self.table_products.set_size_table(size=size)
    
    def get_size(self):
        return self.button_diversos.get_size()
    
    def get_press(self):
        pass