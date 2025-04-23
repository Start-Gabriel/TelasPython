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
        self.window = Window(size=[800,600], color= "gray").pack()
        self.buttonABC = Button(window=self.window, title=Text(text="ABC"),RectValues=Rect(size=[200,50]))
        self.cadastrar = self.buttonABC
        self.excluir = self.buttonABC
        self.consultar = self.buttonABC
        self.todos = self.buttonABC
        self.alterar = self.buttonABC
        self.generate_buttons()
    def generate_buttons(self):
        self.cadastrar.set_title("CADASTRAR")
        self.excluir.set_title("EXCLUIR")
        self.consultar.set_title("CONSULTAR")
        self.alterar.set_title("ALTERAR")
        self.todos.set_title("TODOS")
        self.buttons = [self.cadastrar,self.excluir,self.consultar,self.alterar,self.todos]
        tools_button.alight_buttons([0,0],"y",10, self.buttons)
        for but in self.buttons:
            but.draw()

a = Menu_tela()

while True:
    pygame.display.flip()