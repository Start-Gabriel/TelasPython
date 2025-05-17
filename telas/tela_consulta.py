import bd_produtos.produtos as produtos
from basico.input import Input
from basico.button import Button
from basico.text import Text
from basico.rect import Rect
from basico.window import Window
import basico.tools as tools
import basico.button as tools_button
from bd_produtos import produtos
from basico.navegation import Navagation
import pygame
import sys
pygame.init()

class TelaConsulta:
    def __init__(self):
        self.window = Window(size=[800,600], color= "gray").pack()
        self.consulta_input = Input(Button(window=self.window, title=Text("Pesquisar"),RectValues=Rect([600,50])))
        self.consulta_input.input_button.rect.set_pos([0,100])
        self.consulta_input.input_button.rect.center_x(self.window)
        self.navegation = Navagation([self.consulta_input])
        self.draw()
    def draw(self):
        self.consulta_input.draw()
    def run(self,pos):
        print("run")
    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.navegation.start(event=event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.run(pos)
            pygame.display.flip()