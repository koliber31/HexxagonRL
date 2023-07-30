from draw_board import board
from move_check import move_check
from move_array import moveArr

# Zwraca listę dostępnych pól
def move_tile2_choice(tile1):
    move_arr = []
    tile_number = board[tile1].number
    for i in range(0,18):
        move_arr.append(move_check(moveArr[i], tile_number))

    return move_arr