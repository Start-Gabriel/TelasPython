import pygame
from typing import Union, List, Tuple
import sys
from basico.button import Button
from basico.rect import Rect
from basico.text import Text

import basico.tools as tools
pygame.init()

class Input:
    def __init__(self, buttonValues: Button):
        buttonValues.command = self.input_text
        self.title = buttonValues.title.text
        self.input_button = buttonValues
        self.input_button.title = Text(self.title, buttonValues.title.color, buttonValues.title.background_color, self.input_button.title.size)
        self.backup = buttonValues.window.copy()
        self.texts = ""
        self.cursor_index = 0  # 👈 novo: índice do cursor
        self.clock = pygame.time.Clock()
        self.cursor_visible = True
        self.cursor_counter = 0
        
    def draw(self):
        self.input_button.draw()

    def run(self, pos: List[int] | Tuple[int, int]=None):
        self.loop = True
        self.input_button.run(pos=pos)
        return self.texts

    def input_text(self):
        self.input_button.rect.color = "green"
        self.input_button.draw()

        while self.loop:
            self.clock.tick(60)
            self.handle_events()
            self.blink_cursor()
            pygame.display.flip()

        self.input_button.rect.color = "white"
        self.input_button.draw()
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.input_button.rect.rect.collidepoint(pygame.mouse.get_pos()):
                    self.return_text()
                else:
                    self.set_cursor_position(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.return_text()
                elif event.key == pygame.K_BACKSPACE:
                    self.backspace()
                elif event.key == pygame.K_LEFT:
                    self.cursor_index = max(self.cursor_index - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.cursor_index = min(self.cursor_index + 1, len(self.texts))
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.return_text()
                elif event.key == pygame.K_ESCAPE:
                    self.return_text()
            elif event.type == pygame.TEXTINPUT:
                    self.insert_text(event.text)
            self.update()

    def blink_cursor(self):
        self.cursor_counter += 1
        if self.cursor_counter >= 30:
            self.cursor_counter = 0

    def backspace(self):
        if self.cursor_index > 0:
            self.texts = self.texts[:self.cursor_index - 1] + self.texts[self.cursor_index:]
            self.cursor_index -= 1

    def insert_text(self, char):
        self.texts = self.texts[:self.cursor_index] + char + self.texts[self.cursor_index:]
        self.cursor_index += 1

    def update(self):
        # Atualiza o texto + desenha o cursor
        display_text = f"{self.title}: {self.texts}"
        if self.cursor_visible:
            cursor = "|"
        else:
            cursor = ""

        text_with_cursor = (
            display_text[:len(self.title)+2+self.cursor_index] +
            cursor +
            display_text[len(self.title)+2+self.cursor_index:]
        )
        self.input_button.title = Text(text_with_cursor, self.input_button.title.color, self.input_button.title.background_color, size=self.input_button.title.size)
        self.input_button.draw()

    def set_cursor_position(self, mouse_pos):
        # Tentativa simples de ajustar a posição do cursor baseado no clique
        rel_x = mouse_pos[0] - self.input_button.rect.pos[0]
        font = pygame.font.SysFont(None, self.input_button.title.size)  # Mesma fonte do seu projeto, ajuste aqui
        width = 0
        self.cursor_index = 0
        for i, char in enumerate(self.texts):
            width += font.size(char)[0]
            if width > rel_x - 60:  # Ajuste baseado no tamanho do título
                break
            self.cursor_index = i + 1

    def return_text(self):
        self.loop = False
        self.cursor_visible = False
        return self.texts

    def get_button(self):
        return self.input_button

    def clear(self):
        self.texts = ""
        self.update()
    def set_temp_color(self,color:str):
            self.input_button.rect.color = color
    def set_pos(self,pos:List[int]):
        self.input_button.set_pos(pos)
    def set_size(self, size:List[int]):
        self.input_button.set_size(size=size)
    def get_pos(self):
        return self.input_button.get_pos()
    def get_size(self):
        return self.input_button.get_size()
    def get_press(self):
        return self.input_button.press
    @property
    def press(self):
        return self.input_button.press