import bd_produtos.produtos as produtos
from basico.button import Button
from basico.input import Input
from basico.rect import Rect
from basico.text import Text
from basico.window import Window
from basico.popup import PopUp
import basico.button as tools_button
from typing import List
import pygame
class Pao:
    def __init__(self, window:pygame.Surface,
                 pos:List[int]):
        """Objeto pão

        Args:
            window (Window): Janela onde sera desenhado a opção pao
            pos (List[int]): Posição do botão principal pão
        """
        self.window = window
        self.window_backup = self.window.copy()
        self.pos = pos
        
        self.__defaut_size = [100,50]
        self.cnn = produtos.conectar_banco("bd_produtos/produtos.db")
        self.preco_grande = produtos.buscar_produto(conn=self.cnn, cod=5)[0][2]
        self.preco_pequeno = produtos.buscar_produto(conn=self.cnn, cod=4)[0][2]
        self.PERCENT_BUTTONS = 0.333
        self.PERCENT_POPUP = 0.5
        self.SIZE_Y = 200
        self.PIXEL = 3
        self.CLOCK = pygame.time.Clock()
        self.qtd_paes = [0,0]
        
        self.button_pao = Button(window=self.window,
                                 title="PAO",
                                 RectValues=Rect(size=self.__defaut_size),
                                 command=self.vender_pao)
        self.button_pao.set_pos(self.pos)
    def draw(self):
        self.button_pao.draw()
    
    def vender_pao(self):
        self.run_popup()
    def run_popup(self):
        self.loop_popup = True
        self.pao_tamanho = PopUp(window=self.window,
                                 text="TAMANHO DO PÃO",
                                 rectValues= Rect(size=[self.window.get_size()[0]*self.PERCENT_POPUP, self.SIZE_Y]))
        self.tamanho_pao()
        self.pao_tamanho.draw()
        self.pao_tamanho.custon_buttons(buttons=self.buttons_pao)
        while self.loop_popup:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.pao_tamanho.run(pos=pos)
                    if self.pao_tamanho.loop == False:
                        self.loop_popup = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.K_ESCAPE:
                    self.clear()
            self.CLOCK.tick(60)
            pygame.display.flip()
        
    def tamanho_pao(self):
        self.pao_pequeno = Button(window=self.window,
                                  title=Text(text="PEQUENO",color="white"),
                                  RectValues=Rect(size=[self.pao_tamanho.get_size()[0]*self.PERCENT_BUTTONS, self.__defaut_size[1]],
                                                  color="black"),
                                  command=self.selecionar_op)
        self.pao_grande = Button(window=self.window,
                                  title=Text(text="GRANDE",color="white"),
                                  RectValues=Rect(size=[self.pao_tamanho.get_size()[0]*self.PERCENT_BUTTONS, self.__defaut_size[1]],
                                                  color="black"),
                                  command=self.selecionar_op)
        self.calcular_valor = Button(window=self.window,
                                  title=Text(text="VALOR",color="white"),
                                  RectValues=Rect(size=[self.pao_tamanho.get_size()[0]*self.PERCENT_BUTTONS, self.__defaut_size[1]],
                                                  color="black"),
                                  command=self.selecionar_op)
        self.start_pos = ([self.pao_tamanho.get_pos()[0],
                                  self.pao_tamanho.get_pos()[1]+self.pao_tamanho.get_size()[1]-self.pao_pequeno.get_size()[1]])
        self.buttons_pao =[self.pao_pequeno,self.calcular_valor, self.pao_grande]
        tools_button.alight_buttons(start_pos=self.start_pos, orientation="x", space= 1, buttons=self.buttons_pao)
    
    def selecionar_op(self):
        for but in self.buttons_pao:
            if but.get_clicked():
                self.nome = but.title.text
        self.get_quantidade()
            
    def get_button_pao(self):
        return self.button_pao
    def get_buttons(self):
        return self.buttons_pao
    def get_quantidade(self):
        self.generate_inputs()
        if self.nome != "VALOR":
            self.input_quantidade.draw()
        self.input_valor.draw()
        self.loop_quantidade = True
        while self.loop_quantidade:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.nome != "VALOR":
                        self.quantidade_str = self.input_quantidade.run(pygame.mouse.get_pos()).replace(',','.')
                        if self.quantidade_str != '':
                            if self.nome == "GRANDE":
                                self.qtd_paes[0] = float(self.quantidade_str)
                            if self.nome == "PEQUENO":
                                self.qtd_paes[1] = float(self.quantidade_str)
                            self.loop_quantidade = False
                    self.valor_str = self.input_valor.run(pygame.mouse.get_pos()).replace(',','.')
                    if self.input_quantidade.press == False and self.input_valor.press == False:
                        self.clear()
                    if self.valor_str != '':
                        self.loop_quantidade = False
                        valor = float(self.valor_str)
                        self.qtd_paes[0], self.qtd_paes[1] = self.calcular_quantidade_paes(valor)
                        
            pygame.display.flip()
            
    def generate_inputs(self):
        self.input_quantidade = Input(buttonValues=Button(window=self.window,
                                                    title=Text(text="QUANTIDADE"),
                                                    RectValues=Rect(size=[self.pao_tamanho.get_size()[0],
                                                                          self.__defaut_size[1]],
                                                                    pos=[self.pao_tamanho.get_pos()[0],
                                                                         self.pao_tamanho.get_pos()[1]+self.pao_tamanho.get_size()[1]+self.PIXEL])))
        self.input_valor = Input(buttonValues=Button(window=self.window,
                                                    title=Text(text="VALOR"),
                                                    RectValues=Rect(size=[self.pao_tamanho.get_size()[0],
                                                                          self.__defaut_size[1]],
                                                                    pos=[self.pao_tamanho.get_pos()[0],
                                                                         self.pao_tamanho.get_pos()[1]+self.pao_tamanho.get_size()[1]+self.PIXEL])))
        self.input_valor.set_pos(pos=[self.input_quantidade.get_pos()[0], self.input_quantidade.get_pos()[1]+self.input_valor.get_size()[1]+self.PIXEL])
            
    def calcular_quantidade_paes(self, valor_disponivel: float):
        self.qtd_grande = 0
        self.qtd_pequeno = 0
        if self.nome == "VALOR":
            # Prioriza pão grande
            self.qtd_grande = int(valor_disponivel // self.preco_grande)
            self.resto = round(valor_disponivel - (self.qtd_grande * self.preco_grande), 2)
            
            if self.resto >= self.preco_pequeno:
                self.qtd_pequeno = int(self.resto // self.preco_pequeno)
        elif self.nome == "PEQUENO":
            self.qtd_pequeno = int(valor_disponivel // self.preco_pequeno)
        elif self.nome == "GRANDE":
            self.qtd_grande = int(valor_disponivel // self.preco_grande)
        
        return self.qtd_grande, self.qtd_pequeno

        


    def clear(self):
        self.window.blit(self.window_backup, (0,0))
        self.loop_quantidade = False
    def run(self, pos:List[int]):
        self.valor_total = 0
        self.qtd_paes = [0,0]
        self.button_pao.run(pos)
    
    def get_venda(self):
        for index,qtd in enumerate(self.qtd_paes):
            if qtd == None:
                self.qtd_paes[index] = 0
        self.valor_total = (self.qtd_paes[0]*self.preco_grande+self.qtd_paes[1]*self.preco_pequeno)
        return(self.valor_total)
    
    def get_press(self):
        return self.button_pao.get_clicked()
    @property
    def press(self):
        return self.button_pao.press

    def set_pos(self, pos):
        self.button_pao.set_pos(pos=pos)
    def set_size(self, size):
        self.button_pao.set_size(size=size)
    def get_pos(self):
        return self.button_pao.get_pos()
    def get_size(self):
        return self.button_pao.get_size()