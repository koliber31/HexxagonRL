from sb3_contrib.common.maskable.policies import MaskableActorCriticPolicy
from sb3_contrib import MaskablePPO
from sb3_contrib.common.wrappers import ActionMasker
from get_action_mask import get_action_mask
import os
from hexenv import HexEnv
import time

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env = HexEnv()
env = ActionMasker(env, get_action_mask)
env.reset()

model = MaskablePPO(MaskableActorCriticPolicy, env, verbose=1, tensorboard_log=logdir, ent_coef=0.01, batch_size=32)

TIMESTEPS = 20000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")