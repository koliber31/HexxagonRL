import pygame
import math
from Pawn import Pawn

WIDTH, HEIGHT = 800,800 # width and height of game window
# win = pygame.display.set_mode((WIDTH,HEIGHT))

player_tiles = [None] * 2 # Lista opisująca ile pól zajmuje dany gracz
player_tiles[0] = 3 # Ile pól zajmuje gracz
player_tiles[1] = 3 # Ile pól zajmuje przeciwnik

COLUMNS = 7 # Liczba kolumn planszy
board_radius = 4 # Liczba pól stanowiących promień planszy
size = 30 # Promien hexa
center_x = WIDTH/2 - 9 * size 
center_y = HEIGHT/2 + 9 * size
row_max = 3
board = [] # Lista wszystkich pól stanowiących planszę

for i in range(1,COLUMNS+1): # Liczenie i tworzenie wszystkich hexow
        center_x += 3/2 * size
        if i <= board_radius:
            row_min = 1
            row_max += 1
            center_y = HEIGHT/2 - i * math.sqrt(3) * size/2
        else:
            row_min = row_min + 1
            row_max = 7
            center_y = HEIGHT/2 + (i-8) * math.sqrt(3) * size/2
        
        for j in range(row_min, row_max+1):
            center_y += math.sqrt(3) * size
            pawn = Pawn(i*10+j, center_x, center_y, size, 0)
            # print(i*10+j)
            board.append(pawn)
            