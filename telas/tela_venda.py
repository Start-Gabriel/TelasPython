from basico.button import Button
from basico.input import Input
from basico.rect import Rect
from basico.text import Text
from basico.navegation import Navagation
from bd_produtos import produtos
from basico.window import Window
from basico.button import alight_buttons
from basico.navegation import Navagation
from basico.table import Table
import sys
import pygame
pygame.init()
class TelaVenda:
    def __init__(self):
        self.window = Window(size=[800,600],
                             color="gray").pack()
        self.window_backup = self.window.copy()
        self.title = Button(self.window,title=Text(text="VENDAS",color="white",size=30),RectValues=Rect(size=[800,70],pos=[0,0],color="blue"))
        self.title.draw()
        self.SPACE = 10
        self.PIXEL = 1
        self.PIXEL_SPACE = 4
        self.NR_ITENS = int((self.window.get_size()[1]-self.title.rect.get_size()[1])/30)
        self.nome_item = []
        self.valor_item = []
        self.total = []
        self.generate_buttons()
        self.draw()
        self.navegation = Navagation(self.buttons_vendas)
    def generate_buttons(self):
        self.button_ = Button(window=self.window,title=Text(text="n"),RectValues=Rect(size=[150,50]),command=None)
        self.button_pao = Button(window=self.window,title=Text(text="PÃO"),RectValues=Rect(size=[150,50]),command=self.vender_unidade)
        self.button_quitandas = Button(window=self.window,title=Text(text="QUITANDAS"),RectValues=Rect(size=[150,50]),command=self.vender_preco)
        self.button_diversos = Button(window=self.window,title=Text(text="DIVERSOS"),RectValues=Rect(size=[150,50]),command=self.gerar_diversos)
        self.buttons_vendas = [self.button_pao,self.button_quitandas,self.button_diversos]
        
        self.button_vender = Button(window=self.window,title=Text(text="VENDER"),RectValues=Rect(size=[100,50]),command=self.vender)
        self.button_cancelar = Button(window=self.window,title=Text(text="CANCELAR"),RectValues=Rect(size=[100,50]),command=self.cancelar)
        self.buttons_operacao = [self.button_vender,self.button_cancelar]
        
        self.button_finalizar = Button(window=self.window,title=Text(text="FINALIZAR"),RectValues=Rect(size=[100,100],color="green"))
        self.button_cancelar = Button(window=self.window,title=Text(text="CANCELAR"),RectValues=Rect(size=[100,100],color="red"))
        self.button_valor = Button(window=self.window,title=Text(text="VALOR"),RectValues=Rect(size=[250,100],color="white"))
        self.buttons_final = [self.button_valor,self.button_finalizar,self.button_cancelar]

        
    def draw(self):
        self.draw_buttons()
        self.draw_lines()
        self.title_inserir = Button(self.window,title=Text(text="ADICIONAR",color="white"),RectValues=Rect(size=[150,20],pos=[self.buttons_vendas[-1].rect.pos[0],self.buttons_vendas[-1].rect.pos[1]+self.buttons_vendas[-1].rect.size[1]+self.SPACE],color="blue"))
        self.title_inserir.draw()
        self.inserir_quantidade()
        self.inserir_valor()
        #self.gerar_diversos()
        
    def draw_buttons(self):
        alight_buttons(start_pos=[self.title.rect.pos[0],self.title.rect.pos[1]+self.title.rect.size[1]],orientation="y",space=10,buttons= self.buttons_vendas)
        for but in self.buttons_vendas:
            but.draw()
        self.size_buttons_final = 0
        for soma in self.buttons_final:
            self.size_buttons_final += soma.get_size()[0]
        alight_buttons(start_pos=[self.window.get_size()[0]-self.size_buttons_final-self.SPACE*len(self.buttons_final),self.window.get_size()[1]-self.button_finalizar.get_size()[1]-self.SPACE],orientation="x",space= self.SPACE,buttons=self.buttons_final)
        for but in self.buttons_final:
            but.draw()
        #self.button_valor.set_size([(self.buttons_vendas[0].rect.pos[0]+self.buttons_vendas[0].rect.size[0]*2+self.PIXEL*self.PIXEL_SPACE)-(self.button_finalizar.get_pos()[0]-self.SPACE),100])
        
        
    def draw_lines(self):
        self.line_title = pygame.draw.line(self.window,color="black",start_pos=[self.title.rect.pos[0],self.title.rect.pos[1]+self.title.rect.size[1]],end_pos=[self.title.rect.pos[0]+self.title.rect.size[0],self.title.rect.pos[1]+self.title.rect.size[1]])
        #line_itens = pygame.draw.line(self.window,color="black",start_pos=[self.buttons_vendas[-1].rect.pos[0],self.buttons_vendas[-1].rect.pos[1]+self.buttons_vendas[-1].rect.size[1]],end_pos=[self.buttons_vendas[-1].rect.pos[0]+self.buttons_vendas[-1].rect.size[0],self.buttons_vendas[-1].rect.pos[1]+self.buttons_vendas[-1].rect.size[1]])
        self.line_itens_begin = pygame.draw.line(self.window,color="black",start_pos=[self.buttons_vendas[0].rect.pos[0]+self.buttons_vendas[0].rect.size[0]+self.PIXEL*self.PIXEL_SPACE,self.buttons_vendas[0].rect.pos[1]],end_pos=[self.buttons_vendas[-1].rect.pos[0]+self.buttons_vendas[-1].rect.size[0]+self.PIXEL*self.PIXEL_SPACE,self.window.get_size()[1]])
        self.line_itens_end = pygame.draw.line(self.window,color="black",start_pos=[self.buttons_vendas[0].rect.pos[0]+self.buttons_vendas[0].rect.size[0]*2+self.PIXEL*self.PIXEL_SPACE,self.buttons_vendas[0].rect.pos[1]],end_pos=[self.buttons_vendas[-1].rect.pos[0]+self.buttons_vendas[-1].rect.size[0]*2+self.PIXEL*self.PIXEL_SPACE,self.window.get_size()[1]])
        pygame.display.flip()
    def vender_unidade(self):
        self.mostrar_nome()
    def vender_preco(self):
        pass
    def vender(self):
        pass
    def cancelar(self):
        pass
    
    def inserir_quantidade(self):
        self.title_inserir.rect.pos[0]
        self.quantidade_input = Input(Button(self.window,Text(text="QUANTIDADE",color="black",size=15),Rect([150,50])))
        self.quantidade_input.input_button.rect.set_pos([self.title_inserir.rect.pos[0],self.title_inserir.rect.pos[1]+self.title_inserir.rect.size[1]+self.SPACE])
        self.quantidade_input.draw()
        self.draw_lines()
        
    def inserir_valor(self):
        self.valor_input = Input(Button(self.window,Text(text="VALOR",color="black",size=15),Rect([150,50])))
        self.valor_input.input_button.rect.set_pos([self.quantidade_input.input_button.rect.pos[0],self.quantidade_input.input_button.rect.pos[1]+self.quantidade_input.input_button.rect.size[1]+self.SPACE])
        self.valor_input.draw()
        self.draw_lines()
    def gerar_diversos(self):
        from basico.table import Table
        from bd_produtos import produtos
        self.cnn = self.cnn = produtos.conectar_banco()
        self.__diversos = produtos.listar_produtos_ordenados(self.cnn)
        self.diversos_nome =[]
        self.diversos_valor = []
        for produto in self.__diversos:
            if produto[1] == "quitanda":
                pass
            else:
                self.diversos_valor.append(Button(self.window,title=Text(text=str(f"{produto[2]}").upper()),RectValues=Rect([150,50]),command=None))
                self.diversos_nome.append(Button(self.window,title=Text(text=str(f"{produto[1]}").upper()),RectValues=Rect([150,50]),command=None))
        self.nome_produtos_diversos = Table(window=self.window,size=[149,30],pos= [self.buttons_vendas[0].rect.pos[0]+self.buttons_vendas[0].rect.size[0]+self.PIXEL*self.PIXEL_SPACE+self.PIXEL,self.buttons_vendas[0].rect.pos[1]+self.PIXEL],nr_itens=int(((self.window.get_size()[1]-self.title.rect.get_size()[1])/30)-1),colors=["gray","blue"])
        self.nome_produtos_diversos.draw(self.diversos_nome)
        self.loop_diversos = True
        while self.loop_diversos:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for index,but in enumerate(self.diversos_nome):
                        but.run(pos)
                        if but.press == True:
                            print(but.get_title())
                            print("entrou aqui")
                            self.nome_itens = but.get_title()
                            self.valor_itens = self.diversos_valor[index].get_title()
                            self.vender_unidade()
                    """for but in self.diversos_valor:
                        but.run(pos)
                        if but.press == True:
                            print(but.get_title())
                            self.valor_itens = but.get_title()
                            self.vender_unidade()"""
                    self.nome_produtos_diversos.run(pos)
                    self.nome_produtos_diversos.button_validation.run(pos)
                    if self.nome_item != []:
                        self.tabela_nome.run(pos=pos)
                    if self.valor_item != []:
                        self.tabela_valor.run(pos=pos)
                    if self.nome_produtos_diversos.button_validation.press == False:
                        """self.nome_produtos_diversos.clear()
                        self.loop_diversos = False"""
                        pass
            pygame.display.flip()
    def mostrar_nome(self):
        from basico.table import Table
        try:
            if self.tabela_nome:
                self.tabela_nome.clear()
        except:
            pass
        self.total.append(self.valor_itens)
        self.nome_item.append(Button(window=self.window,title=Text(self.nome_itens),RectValues=Rect([100,100])))
        self.valor_item.append(Button(window=self.window,title=(Text(self.valor_itens)),RectValues=Rect([100,100])))
        self.tabela_nome = Table(window=self.window,size= [self.window.get_size()[0] - self.button_valor.get_pos()[0]-self.SPACE-50,30],pos=[self.button_valor.get_pos()[0],self.title.rect.get_size()[1]+self.SPACE],nr_itens=13,colors=["gray","white"])
        self.tabela_valor = Table(window=self.window,size= [50,30],pos=[self.tabela_nome.pos[0]+self.tabela_nome.size[0],self.tabela_nome.pos[1]],nr_itens=self.tabela_nome.nr_itens,colors=self.tabela_nome.colors)
        self.tabela_valor.draw(buttons=self.valor_item)
        self.tabela_nome.draw(buttons=self.nome_item)
        print(self.valor_itens)
        
        self.set_total = sum(self.total)
        self.valor_input.input_button.title.text = self.total  
        self.valor_input.draw()     
    def run(self,pos):
        for but in self.buttons_vendas:
            but.run(pos)
            
        for but in self.buttons_operacao:
            but.run(pos)
    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.navegation.start(event=event)
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.run(pos)
            pygame.display.flip()