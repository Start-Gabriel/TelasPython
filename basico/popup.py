from basico.rect import Rect
from basico.window import Window
from basico.button import Button
from basico.text import Text
from basico.tools import get_obj_center, get_mid
from typing import List, Tuple
import sys
import pygame
pygame.init()

class PopUp:
    def __init__(self, window:pygame.Surface,
                 text:Text,
                 rectValues:Rect):
        self.window = window
        self.window_size = self.window.get_size()
        self.backup_window = window.copy()
        self.text = text
        self.rectValues = rectValues
        self.PIXEL = 3
        self.space = 2
        self.buttons = []
        self.loop = True
        self.border_size = [rectValues.size[0]+self.space,rectValues.size[1]+self.space]
        self.center = [self.window_size[0]/2 - self.rectValues.size[0]/2, self.window_size[1]/2 - self.rectValues.size[1]/2]
        self.center_border = [self.window_size[0]/2 - self.border_size[0]/2, self.window_size[1]/2 - self.border_size[1]/2]
        self.pop_up = Button(self.window, title=self.text, RectValues=Rect(size=self.rectValues.size, pos= self.center, color=self.rectValues.get_color()))
        self.border = Rect(size=[rectValues.size[0]+self.space,rectValues.size[1]+self.space],pos=self.center_border,color="black")
        self.close = Button(window=self.window, title=Text(text="X"), RectValues=Rect(size=[rectValues.size[0]*7/100, rectValues.size[0]*7/100], pos= [self.center[0]+self.pop_up.rect.size[0]-self.rectValues.size[0]*7/100, self.center[1]], color="red"),command=self.close_pop)
    def draw(self):
        self.border.draw(self.window)
        self.pop_up.draw()
        self.close.draw()
        if self.buttons != []:
            self.custon_buttons(self.buttons)
    def custon_buttons(self, buttons:List[Button]=[]):
        self.buttons = buttons
        if self.buttons[0].get_pos() == [0,0]:
            self.alight_custon_buttons()
        if self.buttons != []:
            for but in buttons:
                but.draw()
    def alight_custon_buttons(self, buttons:List[Button] = None):
        import basico.button as tools_buttons
        self.buttons = buttons if buttons else self.buttons
        self.new_size = self.rectValues.get_size()[0]
        for but in self.buttons:
            but.set_size([self.new_size, but.get_size()[1]])
        self.start_pos = [self.get_pos()[0], self.get_pos()[1]+self.get_size()[1]+self.PIXEL]
        tools_buttons.alight_buttons(start_pos=self.start_pos,
                                     orientation="y",
                                     space=3,
                                     buttons=self.buttons)
    def run(self, pos:List[int]):
        self.draw()
        self.close.run(pos=pos)
        if self.buttons != []:
            for but in self.buttons:
                but.run(pos=pos)
                if but.press is True:
                    self.close_pop()
                    
            pygame.display.flip()
    def close_pop(self):
        self.loop = False
        self.window.blit(self.backup_window, (0,0))
    def set_pos(self, pos:List[int]):
        self.pop_up.set_pos(pos)
        self.close.set_pos(pos=[pos[0]+self.pop_up.get_size()[0]-self.pop_up.get_size()[0]*7/100, pos[1]])
        self.border.set_pos(pos=[pos[0]-self.space/2, pos[1]-self.space/2])
    def set_size(self, size:List[int]):
        self.pop_up.set_size(size=size)
    def get_size(self):
        return self.rectValues.get_size()
    def get_pos(self):
        return self.pop_up.rect.get_pos()
    