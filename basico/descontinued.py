from basico.button import Button, alight_buttons
from basico.text import Text
from basico.rect import Rect
from basico.image import Image
from typing import List, Tuple
from basico.window import Window
import pygame

class Menu:
    def __init__(self,
                 window:pygame.Surface|Window,
                 title:Text=Text(text="MENU"),
                 rect:Rect=Rect([100,50]),
                 background:Image = None,
                 buttons:List[Button]=None,
                 expand:str="y"):
        self.window = window
        self.title = title
        self.rect = rect
        self.background = background
        self.buttons = buttons
        self.expand = expand
        self.button_menu = Button(window=window,
                                  title=title,
                                  RectValues=rect,
                                  command=self.open,
                                  background=background)
        self.__openValidation = False #open and close menu validation
        self.backup = self.window.copy()
        '''try:
            self.buttons.insert(0,self.button_menu)
        except:
            print("erro ao inserir menu")'''
    def draw(self):
        self.button_menu.draw()
        alight_buttons(start_pos=[self.button_menu.rect.pos[0]+self.button_menu.rect.size[0],self.button_menu.rect.pos[1]+self.button_menu.rect.size[1]],orientation=self.expand,space=1,buttons=self.buttons)
    def run(self,pos:List[int]|Tuple[int,int]):
        self.button_menu.run(pos=pos)
    def open(self):
        self.__openValidation = not self.__openValidation
        try:
            if self.__openValidation:
                for but in self.buttons.copy():
                    but.draw()
                self.__runMenu()
            else:
                self.window.blit(self.backup,(0,0))
                self.draw()
        except:
            print("erro ao executar menu")
    def __runMenu(self):
        while self.__openValidation:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.run(pygame.mouse.get_pos())
            pygame.display.flip()