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
but = Button(janela,Text("butao","pink"),Rect([100,50],color="black"),test)
but1= Button(janela,Text("butao1","pink"),Rect([100,50],color="black"),test)
but2 = Button(janela,Text("butao2","pink"),Rect([100,50],color="black"),test)
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
    
            
    pygame.display.flip()