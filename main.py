import pygame
import random
import time


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 40
        self.Pasha = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), [self.top + i * self.cell_size, self.left + j * self.cell_size, self.cell_size, self.cell_size], 1)


shapes = ['square', 'stick', 'steps', 'zigzag_r', 'zigzag_l', 'turn_r', 'turn_l']

pygame.init()
size = width, height = 800, 900
screen = pygame.display.set_mode(size)
board = Board(10, 20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = event.pos
            if coords[0] > board.width * board.cell_size or coords[1] > board.height * board.cell_size:
               print("None")
            else:
                coords_r = (coords[0] - 10) // board.cell_size
                coords_rr = (coords[1] - 10) // board.cell_size
                print((coords_r, coords_rr))
                for i in range(coords_r):

                    for j in range(coords_rr):
                        pass

    # screen.fill((40, 40, 40))
    board.render(screen)
    pygame.display.flip()