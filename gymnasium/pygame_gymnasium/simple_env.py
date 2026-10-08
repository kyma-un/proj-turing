import gymnasium as gym
from gymnasium import spaces
import numpy as np

class SimpleEnv(gym.Env):
    def __init__(self):
        super().__init__()

        # Acciones:
        # 0 = izquierda
        # 1 = derecha

        self.action_space = spaces.Discrete(2)

        # Observación:
        # posición del agente en el espacio [0, 10]
        self.observation_space = spaces.Box(
            low=np.array([0]), 
            high=np.array([10]),
            dtype=np.float32
        )

        self.position = 0


    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.position = 0

        observation = np.array(
            [self.position],
            dtype=np.float32
        )

        info = {}

        return observation, info

    def step(self, action):

        if action == 0:  # izquierda
            self.position -= 1
        elif action == 1:  # derecha
            self.position += 1

        # Limitar posición
        self.position = np.clip(self.position, 0, 10) 

        # Recompensa
        if self.position == 10:
            reward = 10
        else:
            reward = -1

        terminated = self.position == 10
        truncated = False

        observation = np.array(
            [self.position],
            dtype=np.float32
        )
        info = {}

        return (
            observation, 
            reward, 
            terminated, 
            truncated, 
            info
        )