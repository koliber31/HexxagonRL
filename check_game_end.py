from draw_board import board, player_tiles
from move_tile2_choice import move_tile2_choice
from Move import Move

def check_game_end(przeciwnik):
    sprawdz_koniec = False
    player_tiles[0] = 0
    player_tiles[1] = 0

    for i in range(0, len(board)):
        if board[i].player > 0:
            player_tiles[board[i].player - 1] += 1

    criteria1 = player_tiles[0] == 0 or player_tiles[1] == 0
    criteria2 = (player_tiles[0] + player_tiles[1]) == len(board)
    criteria3 = True

    for i in range(len(board)):
        if board[i].player == przeciwnik:
            ruch_wybor = move_tile2_choice(i)

            for j in range(0,18):
                if type(ruch_wybor[j]) == Move: 
                    if ruch_wybor[j].player == 0:
                        criteria3 = False
    
    # print(criteria1, criteria2, criteria3)
    sprawdz_koniec = criteria1 or criteria2 or criteria3
    
    return sprawdz_koniec