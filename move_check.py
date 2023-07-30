import copy
from draw_board import board

# Check if tile is relevant for move
def move_check(move, tile_number):
    
    move_return = copy.copy(move)

    for i in range(0, len(board)):
        if board[i].number == tile_number + move_return.wektor:
            move_return.tile = i
            move_return.tile_number = board[i].number
            move_return.player = board[i].player
            return move_return
        else:
            move_return.player = -1