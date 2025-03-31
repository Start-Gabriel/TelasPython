import basico.button as buton
from basico.window import Window
from basico.text import Text
import pygame
pygame.init()
janela = Window([600,600], "red").pack()
but = buton.Button(janela,Text(),[100,50],"blue").pack()

while True:
    pygame.display.flip()