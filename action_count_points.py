from Move import Move
from move_array import moveArr
from move_check import move_check

def action_count_points(move, tile_number, przeciwnik):
    points = 0
    tile_number = tile_number
    move_action = []
    if move == 1:
        points += 1

    for k in range(0,6): 
        move_action.append(move_check(moveArr[k], tile_number))
        
        if type(move_action[k]) == Move:
            if move_action[k].player == przeciwnik:
                points += 1
    return points