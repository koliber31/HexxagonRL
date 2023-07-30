# import pygame
from Move import Move
from draw_board import board
from move_jump import move_jump
from move_action import move_action
from check_game_end import check_game_end
from move_array import moveArr
from get_action_mask import get_action_mask
import hexenv

envv = hexenv
def phase1(action):
    fromWhere = action // 18
    toWhere = action % 18
    if getattr(phase1, 'first_run', True):
        phase1.step = 1
    
    phase1.first_run = False
    phase1.run = True

    # Choice of pawn with which player want to move
    if phase1.step == 1:
        tile2 = -100
        if board[fromWhere].player != 1:
            phase1.step = 101
            print("Illegal Move")
            print(get_action_mask(envv))
            for k in range(len(board)):
                print(board[k].player, end='')
            print(action)
            print(fromWhere, toWhere)
        else:
            tile2Number = board[fromWhere].number + moveArr[toWhere].wektor
            for i in range(0,len(board)):
                if board[i].number == tile2Number:
                    if board[i].player != 0:
                        phase1.step = 101
                        print("Illegal Move")
                        print(get_action_mask(envv))
                        for k in range(len(board)):
                            print(board[k].player, end='')
                        print(action)
                        print(fromWhere, toWhere)
                    else:
                        tile2 = i
            if tile2 == -100:
                phase1.step = 101
                print("Illegal Move")
                print(get_action_mask(envv))
                for k in range(len(board)):
                    print(board[k].player, end='')
                print(action)
                print(fromWhere, toWhere)
            else:
                # print(tile2)
                if tile2 <= 60:
                    if(toWhere >= 6 and toWhere <= 17):
                        move_jump(fromWhere, tile2, 2, 1)
                    else:
                        move_jump(fromWhere, tile2, 1, 1)
                    phase1.step = 5

    
    # Capture enemies pawns 
    if phase1.step == 5:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         phase1.run = False
        #         break
        captured = 0
        for i in range(0,6):
            tile2 = board[fromWhere].number + moveArr[toWhere].wektor
            captured += move_action(tile2 + moveArr[i].wektor, 1, 2)
        phase1.step = 100
    
    if phase1.step == 100:
        phase = 2
        phase1.step = 0
        phase1.first_run = True
        illegalMove = False
        if check_game_end(2):
            phase = 3
        
        return phase, phase1.run, illegalMove, captured
    
    if phase1.step == 101:
        phase = 4
        phase1.step = 0
        phase1.first_run = True
        illegalMove = True
        if check_game_end(2):
            phase = 3
        return phase, phase1.run, illegalMove, 0
        
    
    # return 1, phase1.run