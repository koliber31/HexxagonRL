# import pygame
from draw_board import board

# Check which tile was pressed
def tile_press():
    # mouse_pos = pygame.mouse.get_pos()
    for i in range(0,len(board)): # Sprawdzenie który pionek został kliknięty
        # if plansza[i].click_pawn(mouse_pos) == True: # True zwraca klikniety pionek
            tile = i
    return tile