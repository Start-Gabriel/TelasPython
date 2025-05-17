from basico.input import Input
from basico.button import Button
from basico.text import Text
from basico.rect import Rect
from basico.window import Window
import basico.tools as tools
import basico.button as tools_button
from bd_produtos import produtos
from basico.navegation import Navagation
import pygame
import sys
pygame.init()

class Cadastro:
    def __init__(self):
        '''self.cnn = produtos.conectar_banco
        produtos.criar_tabela()'''
        self.window = Window([800,600], "gray").pack()
        self.title = Text("CADASTRO",color="white",background_color="black", size=40)
        self.title.draw(self.window, [tools.get_obj_center([800,600],self.title.get_size_tuple())[0],0])
        self.nome = Input(Button(self.window, Text("NOME"), RectValues=Rect([500,50])))
        self.preco = Input(Button(self.window, Text("PREÇO"), RectValues=Rect([500,50])))
        self.cod = Input(Button(self.window, Text("CODIGO"), RectValues=Rect([500,50])))
        self.quantidade = Input(Button(self.window, Text("QUANTIDADE"), RectValues=Rect([500,50])))
        self.confirmar = Button(window=self.window, title=Text(text="CONFIRMAR", color="white"), RectValues=Rect([90,50],color="green"), command= self.validar)
        self.cancelar = Button(window=self.window, title=Text(text="CANCELAR", color="white"), RectValues=Rect([90,50],color="red"), command= self.limpar)
        self.retornar = Button(window=self.window, title=Text(text="VOLTAR", color="white"), RectValues=Rect([90,50],color="yellow"), command= self.voltar)
        self.buttons = [self.nome.get_button(), self.preco.get_button(), self.cod.get_button(), self.quantidade.get_button()]
        self.inputs = [self.nome, self.preco, self.cod, self.quantidade]
        self.navegation = Navagation(self.inputs)
        self.loop = True
        self.draw()
    def draw(self):
        self.center = tools_button.get_center_button([800,600], self.nome.get_button())
        tools_button.alight_buttons([self.center[0],150],"y",10, self.buttons)
        tools_button.alight_buttons([self.quantidade.get_button().rect.get_pos()[0],self.quantidade.get_button().rect.get_pos()[1]+60],"x", 10, [self.confirmar, self.cancelar, self.retornar])
        for but in self.buttons:
            but.draw()
        self.confirmar.draw()
        self.cancelar.draw()
        self.retornar.draw()
    def run(self, pos):
        self.pos = pos
        self._cod = self.cod.run(self.pos)
        self._preco = self.preco.run(self.pos)
        self._nome = self.nome.run(self.pos)
        self._quantidade = self.quantidade.run(self.pos)
        self.confirmar.run(self.pos)
        self.cancelar.run(self.pos)
        self.retornar.run(self.pos)
        pygame.display.flip()
    def validar(self):
        self.full = all([
            self._cod not in (None, "", []),
            self._preco not in (None, "", []),
            self._nome not in (None, "", []),
            self._quantidade not in (None, "", [])
        ])
        if self.full:
            self.insert()
    def insert(self):
        import bd_produtos.produtos as produto
        from basico.popup import PopUp
        self.__cnn = produto.conectar_banco("bd_produtos/produtos.db")
        produto.criar_tabela(self.__cnn)
        self.mensage = produto.cadastrar_produto(conn=self.__cnn, nome=self._nome, preco=self._preco, cod= self._cod, quantidade= self._quantidade)
        if self.mensage[0] == "codigo duplicado":
            self.limpar()
            self.pop_up = PopUp(self.window,Text(f"{self.mensage}"), Rect([600,100], color="white"))
        else:
            self.pop_up = PopUp(self.window,Text(f"{self.mensage}"), Rect([300,100], color="white"))
        self.pop_up.run()
    def limpar(self):
        for inp in self.inputs:
            inp.clear()
    def voltar(self):
        from submenus.menu_produto import MenuProduto
        app = MenuProduto()
        app.start()
    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.navegation.start(event=event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.run(pos)
            pygame.display.flip()
