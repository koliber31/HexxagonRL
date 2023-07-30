from draw_board import board
from move_array import tile_color

# Capturing enemies pawns
def move_action(tile_number, player, enemy):
    captured = 0 
    for i in range(0,len(board)):
        if board[i].number == tile_number:
            if board[i].player == enemy:
                board[i].player = player
                board[i].color = tile_color[player]
                captured += 1 
    return captured 