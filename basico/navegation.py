from basico.button import Button
from basico.input import Input
from typing import List
import pygame
pygame.init()
class Navagation:
    def __init__(self, buttons:List[Button]):
        self.buttons = buttons
        self.index = -1
    def start(self, event:pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.down()
            if event.key == pygame.K_UP:
                self.up()
            if event.key == pygame.K_RETURN:
                self.enter()
            if type(self.buttons[self.index]) == Button:
                pass
            else:
                self.enter()
    def enter(self):
        self.buttons[self.index].run()
            
    def down(self):
        self.index += 1
        self.index = self.index_validation(self.index)
        self.buttons[self.index].set_temp_color("green")
        self.buttons[self.index].draw()
        self.reestore_color()
        self.buttons[self.index-1].draw()
    def up(self):
        self.index = self.index - 1

        self.index = self.index_validation(self.index)
        self.buttons[self.index].set_temp_color("green")
        self.buttons[self.index].draw()
        
        self.reestore_color()
        self.index_color = self.index_validation(self.index+1)
        self.buttons[self.index_color].draw()
    def reestore_color(self):
        if type(self.buttons[self.index])==Button:
            self.buttons[self.index].rect.color = self.buttons[self.index].color
        if type(self.buttons[self.index])==Input:
            self.buttons[self.index].input_button.rect.color = self.buttons[self.index].input_button.color
    def index_validation(self, index):
        if index >= 0 and index <= len(self.buttons) - 1:
            return index  # <-- aqui deveria ser o parâmetro index, não self.index
        if index < 0:
            index = len(self.buttons) - 1
            return index
        if index > len(self.buttons) - 1:
            index = 0
            return index
