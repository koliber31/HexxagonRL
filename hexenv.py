import gymnasium as gym
import pygame
from gymnasium import spaces
import numpy as np
from draw_board import board #, win
from Phase1 import phase1
from Phase2 import phase2
from move_array import moveArr
import time
import random

# pygame.init()
# pygame.display.set_caption("Hexxagon") 
# FPS = 240

# def draw(board):
#     win.fill("black")

#     for pawn in board:
#         pawn.draw_pawn() # draw all pawns on board
    
#     pygame.display.update()

npObs = np.ndarray((37,), dtype=np.int32)
class HexEnv(gym.Env):
    def __init__(self):
        super(HexEnv, self).__init__()
        

        self.action_space = spaces.Discrete(666)
        self.observation_space = spaces.MultiDiscrete(3 * np.ones(37))
        self.game_history = []
        self.action_history = []

    def step(self, action):
        reward = 0
        done = False
        # self.clock.tick(FPS)
        if self.phase == 1:
            board_prev = []
            board_next = []
            for i in range(len(board)):
                board_prev.append(board[i].player)
            self.action_history.append([action // 18, action % 18 ])
            phase, run, illegalMove, captured = phase1(action)

            for i in range(len(board)):
                board_next.append(board[i].player)
            if board_prev == board_next:
                for i in range(len(board)):
                    print(board[i].player, end='')
                print("\n")
                for i in range(len(board)):
                    print(board_prev[i], end='')
                print("\n")

            if illegalMove == True:
                reward = -1
                done = False

        # draw(board)
        # time.sleep(0.75)
        self.game_history.append([pawn.player for pawn in board])

        
        if phase == 2:
            
            phase, tile1, tile2 = phase2()
            self.action_history.append([tile1, tile2])
            

        # draw(board)
        # time.sleep(0.75)

        self.game_history.append([pawn.player for pawn in board])

        if phase == 3:
            player1_points = 0
            player2_points = 0
            # print(self.game_history)
            for i in range(0,len(board)):
                if board[i].player == 1:
                    player1_points += 1
                elif board[i].player == 2:
                    player2_points += 1
            
            if player1_points > player2_points:
                print("Player 1 won")
                reward = 1
                done = True
            elif player1_points < player2_points:
                print("Player 2 won")
                reward = -1
                done = True
            else:
                print("Remis")
                reward = 0.25
                done = True

        if phase == 4:
            done = True
            points = 0
            for i in range(len(board)):
                npObs[i] = board[i].player

            info = {}
            print("Illegal Move")
            return npObs, reward, done, False, info
            
        
        points = 0
        for i in range(len(board)):
            npObs[i] = board[i].player


        info = {}
        return npObs, reward, done, False, info


    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.turnNumber = 0
        run = True
        # self.clock = pygame.time.Clock()
        self.phase = 1
        self.done = False
        for pawn in board:
            pawn.player = 0
            pawn.color = 'white'

        pawnNum = 0
        for pawn in board: # Ustawienie początkowych pionków na planszy
            pawn.move_tile_set(11,1) # Ustawianie pionków gracza 1
            pawn.move_tile_set(47,1)
            pawn.move_tile_set(74,1)
        
            pawn.move_tile_set(14,2)  # Ustawianie pionków gracza 2
            pawn.move_tile_set(41,2)
            pawn.move_tile_set(77,2)
            # pawnNum += 1


        for i in range(len(board)):
            npObs[i] = board[i].player

        info = {}
        return npObs, info