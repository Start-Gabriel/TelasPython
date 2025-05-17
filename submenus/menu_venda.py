from basico.button import Button
from basico.window import Window
from basico.input import Input
from basico.rect import Rect
from basico.text import Text

from windows.window_venda import WindowVenda

from typing import List

import basico.button as tools_button
import pygame

class MenuVenda:
    def __init__(self):
        self.window = WindowVenda()
        #--------------DEFAUT BUTTON VALUES--------
        self.window.draw()
        self.window = self.window.get_window()
        self.BUTTON_SIZE = [100,50]
        self.BUTTON_RECT = Rect(size=self.BUTTON_SIZE)
        self.CLOCK = pygame.time.Clock()
    #NOT OTIMIZED i alone!
    def run(self, pos:List[int]):
        from telas.tela_vendav2 import TelaVenda
        self.app = TelaVenda(self.window)
        self.app.set_window(self.window)
        self.app.draw()
        self.app.run(pos=pos)
        self.CLOCK.tick(60)
    def start(self):
        self.loop = True
        while self.loop:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.loop = False
                    pygame.quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.run(pos=pygame.mouse.get_pos())
            pygame.display.flip()
            
    