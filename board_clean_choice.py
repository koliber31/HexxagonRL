from draw_board import board
from move_array import tile_color

# Wyczyszczenie możliwych ruchów
def board_clean_choice():
    for i in range(0,len(board)):
        board[i].color = tile_color[board[i].player]