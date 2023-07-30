from get_action_mask import get_action_mask
import hexenv

env = hexenv.HexEnv()
mask = 0

def call_mask():
    mask = get_action_mask(env)
    # return mask
