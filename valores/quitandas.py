from basico.button import Button
from basico.input import Input
from basico.rect import Rect
from basico.text import Text
from basico.window import Window
from basico.popup import PopUp
import basico.button as tools_button
from typing import List
import pygame
pygame.init()
class Quitandas:
    def __init__(self,
                 window:pygame.Surface,
                 pos:List[int]):
        self.window = window
        self.window_backup = window.copy()
        self.pos = pos
        
        self.DEFAUT_SIZE = [100,50]
        self.PIXEL = 3
        self.PERCENT_POPUP = 0.3
        self.CLOCK = pygame.time.Clock()
        self.button_quitanda = Button(window=self.window,
                                      title=Text("QUITANDA"),
                                      RectValues=Rect(size=self.DEFAUT_SIZE, pos=self.pos), 
                                      command=self.vender_quitanda)
    
    def draw(self):
        self.button_quitanda.draw()
    def generate_input(self):
        self.run_input()
    def run_input(self):
        self.loop_input = True
        self.valor = Input(Button(window=self.window,
                                  title=Text("VALOR"),
                                  RectValues=Rect(self.DEFAUT_SIZE)))
        self.pop_up = PopUp(window=self.window,
                            text=Text("INFORME O VALOR"),
                            rectValues=Rect(size=[self.window.get_size()[0]*self.PERCENT_POPUP,
                                                  self.window.get_size()[1]*self.PERCENT_POPUP]))
        self.pop_up.custon_buttons([self.valor])
        self.pop_up.alight_custon_buttons()
        self.pop_up.draw()
        while self.loop_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.pop_up.run(pos=pos)
                    if self.pop_up.loop == False:
                        self.loop_input = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.K_ESCAPE:
                    pass
            self.CLOCK.tick(60)
            pygame.display.flip()
    def vender_quitanda(self):
        self.generate_input()
    def run(self, pos:List[int]):
        self.button_quitanda.run(pos=pos)
    
    def get_press(self):
        pass
    def get_pos(self):
        return self.button_quitanda.get_pos()
    def get_size(self):
        return self.button_quitanda.get_size()
    def set_pos(self, pos:List[int]):
        self.button_quitanda.set_pos(pos)
    def set_size(self, size:List[int]):
        self.button_quitanda.set_size(size)