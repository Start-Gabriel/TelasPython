from basico.button import Button
import basico.button as buton
from basico.window import Window
from basico.text import Text
from basico.image import Image
from basico.rect import Rect
from basico.menu import Menu
import pygame
from basico.input import Input
import basico.image
pygame.init()
def test():
    print("teste")
janela = Window([600,600], "gray").pack()
inp = Input(buttonValues=Button(janela,Text("input"),Rect([100,50],[0,0])))
inp.draw()
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            inp.run(pos)
            
    pygame.display.flip()