from draw_board import board
from move_tile2_choice import move_tile2_choice
from Move import Move
import numpy as np
import gymnasium as gym

def get_action_mask(env: gym.Env) -> np.ndarray:
    mask = np.zeros((666,), dtype=np.int32)
    for i in range(len(board)):
        if board[i].player != 1:
            for j in range(0,18):
                mask[i*18 + j] = 0
        
        else:
            move_choice = move_tile2_choice(i)
            for j in range(0,18):
                if type(move_choice[j]) == Move:
                    if move_choice[j].player == 0:
                        mask[i*18 + j] = 1
                    else:
                        mask[i*18 + j] = 0
    
    return mask