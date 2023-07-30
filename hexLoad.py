from sb3_contrib import MaskablePPO
import os
from hexenv import HexEnv
import time
from get_action_mask import get_action_mask


# models_dir = f"models/{int(time.time())}/"
# logdir = f"logs/{int(time.time())}/"

# if not os.path.exists(models_dir):
# 	os.makedirs(models_dir)

# if not os.path.exists(logdir):
# 	os.makedirs(logdir)

env = HexEnv()
env.reset()

# model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

model_path = "models/1690622103/40000.zip"
model = MaskablePPO.load(model_path, env=env)

episodes = 10
for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    while not done:
        # print(ep)
        action_masks = get_action_mask(env)
        action, _states = model.predict(obs, action_masks=action_masks)
        # print("START")
        # print(get_action_mask())
        # print("KONIEC")
        obs, reward, done, trunctated, info = env.step(action)
        
        # print(reward)
        # print(obs)
env.close()