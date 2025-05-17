import pygame
import sys
from basico.window import Window
from basico.text import Text
from basico.button import Button
from basico.rect import Rect
import basico.tools as tools
import basico.button as tools_button


class MenuCliente:
    def __init__(self):
        
        self.window = Window(size=[800,600], color="gray").pack()
        
        self.title = Text("CADASTRO CLIENTES", color="white", background_color="black", size=40)
        self.title.draw(self.window, [tools.get_obj_center([800,600], self.title.get_size_tuple())[0], 0])

        self.cadastrar = Button(self.window, Text("CADASTRAR"), Rect([200,50]), self.__cadastrar)
        self.excluir   = Button(self.window, Text("EXCLUIR"),   Rect([200,50]), self.__excluir)
        self.consultar = Button(self.window, Text("CONSULTAR"), Rect([200,50]), self.__consultar)
        self.alterar   = Button(self.window, Text("ALTERAR"),   Rect([200,50]), self.__alterar)
        self.todos     = Button(self.window, Text("TODOS"),     Rect([200,50]), self.__todos)
        self.voltar    = Button(self.window, Text("VOLTAR"),    Rect([200,50]), self.__voltar)

        self.buttons = [self.cadastrar, self.excluir, self.consultar, self.alterar, self.todos, self.voltar]

        self.draw()

    def draw(self):
        center = tools_button.get_center_button([800,600], self.alterar)
        tools_button.alight_buttons([center[0], 150], "y", 10, self.buttons)
        for but in self.buttons:
            but.draw()

    def run(self, pos):
        for but in self.buttons:
            but.run(pos=pos)

    def __cadastrar(self):
        pass

    def __excluir(self):
        print("Excluir cliente")

    def __consultar(self):
        print("Consultar cliente")

    def __alterar(self):
        print("Alterar cliente")

    def __todos(self):
        print("Listar todos clientes")

    def __voltar(self):
        from main_menu import MainMenu
        app = MainMenu()
        app.start()

    def start(self):
        self.running = True
        self.draw()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.run(pos)
            pygame.display.flip()
