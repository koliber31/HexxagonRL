from draw_board import board

tile_color = ['white', 'green', 'red']

# Moving the pawn
def move_jump(tile1, tile2, jump, player):
    board[tile2].player = player
    board[tile2].color = tile_color[player]

    if jump == 2:
        board[tile1].player = 0
        board[tile1].color = tile_color[0]
    else:
        board[tile1].player = player
        board[tile1].color = tile_color[player]