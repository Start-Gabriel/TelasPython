from basico.input import Input
from basico.button import Button
from basico.text import Text
from basico.rect import Rect
from basico.window import Window
import basico.tools as tools
import basico.button as tools_button
from bd_produtos import produtos
import pygame

class Cadastro:
    def __init__(self):
        '''self.cnn = produtos.conectar_banco
        produtos.criar_tabela()'''
        self.window = Window([800,600], "gray").pack()
        self.title = Text("CADASTRO",color="white",background_color="black", size=40)
        self.title.draw(self.window, [tools.get_obj_center([800,600],self.title.get_size_tuple())[0],0])
        self.nome = Input(Button(self.window, Text("NOME"), RectValues=Rect([500,50])))
        self.preco = Input(Button(self.window, Text("PREÇO"), RectValues=Rect([500,50])))
        self.cod = Input(Button(self.window, Text("CODIGO"), RectValues=Rect([500,50])))
        self.quantidade = Input(Button(self.window, Text("QUANTIDADE"), RectValues=Rect([500,50])))
        self.buttons = [self.nome.get_button(), self.preco.get_button(), self.cod.get_button(), self.quantidade.get_button()]
        self.inputs = [self.nome, self.preco, self.cod, self.quantidade]
        self.loop = True
        self.draw()
    def draw(self):
        self.center = tools_button.get_center_button([800,600], self.nome.get_button())
        tools_button.alight_buttons([self.center[0],150],"y",10, self.buttons)
        for but in self.buttons:
            but.draw()
    def run(self):
        while self.loop:
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.cod.run(self.pos)
                    self.preco.run(self.pos)
                    self.nome.run(self.pos)
            pygame.display.flip()