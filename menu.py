from basico.button import Button
from basico.input import Input
from basico.text import Text
from basico.rect import Rect
from basico.window import Window
import basico.button as tools_button

import pygame
pygame.init()


class Menu_tela:
    def __init__(self):
        self.window = Window(size=[800,600], color="gray").pack()

        self.cadastrar = Button(self.window, Text("CADASTRAR"), Rect([200,50]), self.__cadastrar)
        self.excluir   = Button(self.window, Text("EXCLUIR"),   Rect([200,50]),self.__excluir)
        self.consultar = Button(self.window, Text("CONSULTAR"), Rect([200,50]),self.__consultar)
        self.alterar   = Button(self.window, Text("ALTERAR"),   Rect([200,50]), self.__alterar)
        self.todos     = Button(self.window, Text("TODOS"),     Rect([200,50]), self.__todos)
        self.buttons = [self.cadastrar, self.excluir, self.consultar, self.alterar, self.todos]

        self.draw()

    def draw(self):
        center = tools_button.get_center_button([800,600],self.alterar)
        tools_button.alight_buttons([center[0], 50], "y", 10, self.buttons)
        for but in self.buttons:
            but.draw()
    def run(self,pos):
        for but in self.buttons:
            but.run(pos=pos)
    def __cadastrar(self):
        from telas.tela_cadastro import Cadastro
        produto = Cadastro()
        produto.run()
    def __excluir(self):
        print("b")
    def __consultar(self):
        pass
    def __alterar(self):
        pass
    def __todos(self):
        pass


a = Menu_tela()

while True:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            a.run(pos)
    pygame.display.flip()