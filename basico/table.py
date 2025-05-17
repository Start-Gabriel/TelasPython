from basico.button import Button
from basico.rect import Rect
from basico.text import Text
from basico.button import alight_buttons
from basico.tools import get_nested_center, get_window_center, get_color
from typing import List,Tuple
import pygame
pygame.init()
class Table:
    def __init__(self, window:pygame.Surface,
                 size:List[int],
                 pos:List[int],
                 nr_itens:int = 5,
                 colors:Tuple[str,str]=["gray", "red"]):
        self.window = window
        self.window_backup = self.window.copy()
        self.size = size
        self.size_table = [size[0], size[1]*nr_itens]
        self.nr_itens = nr_itens
        self.colors = colors
        self.pos = pos
        self.next = Button(self.window, title=Text(">"),RectValues=Rect([30,30]),command=self.next_line)
        self.back = Button(self.window, title=Text("<"),RectValues=Rect([30,30]),command=self.back_line)
        self.pos_list = 0
        self.pos_list_validation = 1
        self.button_validation = Button(window=self.window, title=Text(""),RectValues=Rect(self.size_table, self.pos), command=self.validation_click_table)
        
    def draw(self, buttons:List[Button]|Button= None):
        self.buttons = buttons.copy()
        self.validation_size()
        self.set_size_button()
        self.update()
        self.next.draw()
        self.back.draw()
    def validation_size(self):
        pass
        
        """while self.nr_itens > len(self.buttons)-self.pos_list:
            self.buttons.append(Button(self.window,Text(""),Rect()))
            print(len(self.buttons))"""
            
    def set_color_button(self):
        if self.buttons:
            index_color = 0
            for but in self.buttons:
                index_color +=1
                if index_color == 2:
                   index_color = 0
                but.rect.color=self.colors[index_color]
    def set_size_button(self):
        for but in self.buttons:
            but.rect.set_size(self.size)
        
        alight_buttons(start_pos=self.pos, orientation="y", space=0, buttons=self.buttons)
        self.back.set_pos([self.pos[0],self.size_table[1]+self.pos[1]])
        self.next.set_pos([self.back.get_pos()[0]+self.back.get_size()[0], self.back.get_pos()[1]]) 
    def update(self):
        self.window.blit(source=self.window_backup,
                         dest=self.pos,
                         area=(self.pos[0],
                               self.pos[1],
                               self.size_table[0],
                               self.size_table[1]))
        start = self.pos_list
        end = min(start + self.nr_itens, len(self.buttons))
        index_color = 0

        for i in range(start, end):
            button = self.buttons[i]
            button.rect.color = self.colors[index_color]
            button.set_size(self.size)
            button.rect.set_pos([self.pos[0], self.pos[1] + (i - start) * self.size[1]])
            button.draw()

            index_color = (index_color + 1) % len(self.colors)
        self.back.draw()
        self.next.draw()
    def clear(self):
        self.window.blit(self.window_backup, (0,0))
    def validation_click(self, pos):
        returned = self.button_validation.run(pos=pos)
    def validation_click_table(self):
        return True

                
    def run(self, pos):
        self.atual_buttons = self.get_buttons()
        for but in self.atual_buttons:
            but.run(pos)
            if but.press:
                return but.title.text
        self.button_validation.run(pos)
        self.next.run(pos)
        self.back.run(pos)
    def get_buttons(self):
        return self.update_buttons()
    def next_line(self):
        if self.pos_list < len(self.buttons):
            self.pos_list += self.nr_itens
        self.validation_size()
        self.update_buttons()
        self.update()

    def back_line(self):
        if self.pos_list - self.nr_itens >= 0:
            self.pos_list -= self.nr_itens
        else:
            self.pos_list = 0
        self.update_buttons()
        self.update()
        
    def set_size_table(self, size:List[int]):
        self.size_table = [size[0], size[1]*self.nr_itens]

    def set_pos_table(self, pos:List[int]):
        self.pos = pos
    def get_pos(self):
        return self.pos
    
    def update_buttons(self):
        self.atual_buttons = []
        for index in range(self.nr_itens):
            if self.verify_nr_itens(index):
                self.atual_buttons.append(self.buttons[index+self.pos_list])
        return self.atual_buttons     
    def verify_nr_itens(self, index:int):
        if self.pos_list+index > len(self.buttons)-1:
            print("maior que a lista?")
            return False
        if self.pos_list < 0:
            print ("menor que a lista")
            return False
        else:
            return True
        