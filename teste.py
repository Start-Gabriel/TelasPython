from submenus.menu_venda import MenuVenda
from telas.tela_vendav2 import TelaVenda
from windows.window_venda import WindowVenda
import pygame
clock = pygame.time.Clock()
window = WindowVenda()
app = TelaVenda(window=window.draw())
app.draw()

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            app.run(pos=pos)
        
    pygame.display.flip()
    clock.tick(60)