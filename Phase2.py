# import pygame
import random
from Move import Move
from draw_board import board
from move_tile2_choice import move_tile2_choice
from action_count_points import action_count_points
from move_jump import move_jump
from move_action import move_action
from board_clean_choice import board_clean_choice
from move_array import moveArr
from check_game_end import check_game_end

def phase2():
    if getattr(phase2, 'first_run', True):
        phase2.step = 0
    
    phase2.first_run = False
    

    if phase2.step == 0:
        phase2.points_max = -1
        tile1 = 0
        phase2.step = 1  

    if phase2.step == 1:
        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             run = False
        #             break
        
        for i in range(0, len(board)):
            if board[i].player == 2:
                move_choice = move_tile2_choice(i)

                for j in range(0,18):
                    points = 0
                    if type(move_choice[j]) == Move:
                        if move_choice[j].player == 0:
                            points = action_count_points(move_choice[j].jump, move_choice[j].tile_number, 1)
                            phase2.wage_max = random.randrange(0,10)
                        
                        if points > phase2.points_max or (points == phase2.points_max and phase2.wage_max > move_wage) :                                    
                            phase2.points_max = points
                            tile1 = i
                            # pole2 = move_choice[j].tile
                            tile2_move = move_choice[j]
                            move_wage = phase2.wage_max
        phase2.step = 2

    if phase2.step == 2:
        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             run = False
        #             break

        if tile1 >= 0:
            move_jump(tile1, tile2_move.tile, tile2_move.jump, 2)
            # print(tile1,tile2_move.pole, tile2_move.skok, 2)
        
        phase2.step = 3 
            
    if phase2.step == 3:
        for i in range(0,6):
            move_action(tile2_move.tile_number + moveArr[i].wektor, 2, 1)
        phase2.step = 100

    if phase2.step == 100:
        board_clean_choice()
        phase2.step = 0
        if check_game_end(1):
            faza = 3
            return 3, tile1, tile2_move.tile
        else:
            return 1, tile1, tile2_move.tile
    
    return 2 