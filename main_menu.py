import pygame
from basico.window import Window
from basico.text import Text
from basico.button import Button
from basico.rect import Rect
import basico.tools as tools
import basico.button as tools_button
from basico.navegation import Navagation


class MainMenu:
    def __init__(self):
        
        self.window = Window([800, 600], "gray").pack()

        self.title = Text("PANIFICADORA DELLIS", color="white", background_color="black", size=40)
        self.title.draw(self.window, [tools.get_obj_center([800,600], self.title.get_size_tuple())[0], 0])

        self.produto_button = Button(self.window, Text("PRODUTOS"), Rect([200, 50]), self.__abrir_menu_produto)
        self.cliente_button = Button(self.window, Text("CLIENTES"), Rect([200, 50]), self.__abrir_menu_cliente)
        self.venda_button = Button(self.window, Text("VENDA"), Rect([200, 50]), self.__abrir_menu_venda)

        self.buttons = [self.produto_button, self.cliente_button, self.venda_button]

        center = tools_button.get_center_button([800,600], self.produto_button)
        tools_button.alight_buttons([center[0], 200], "y", 20, self.buttons)
        self.draw()
    def draw(self):
        for but in self.buttons:
            but.draw()

    def __abrir_menu_produto(self):
        from submenus.menu_produto import MenuProduto
        app = MenuProduto()
        app.start()
    

    def __abrir_menu_cliente(self):
        pass
    def __abrir_menu_venda(self):
        from telas.tela_venda import TelaVenda
        app = TelaVenda()
        app.start()

    def run(self, pos):
        for button in self.buttons:
            button.run(pos=pos)

    def start(self):
        navegation =Navagation(self.buttons)
        self.running = True
        while self.running:
            for event in pygame.event.get():
                navegation.start(event=event)
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.run(pos)
            pygame.display.flip()
