import gymnasium as gym
from gymnasium import spaces
import numpy as np
from domain.plant import Plant
from domain.renderer import Renderer
from domain.reward import RewardFunction

class GymEnvironmentAdapter(gym.Env):

    metadata = {"render_modes": ["human"], "render_fps": 60}

    def __init__(
        self,
        plant: Plant,
        reward_function: RewardFunction,
        renderer: Renderer,
    ):
        super().__init__()

        self.plant = plant
        self.reward_function = reward_function
        self.renderer = renderer

        # Definir el espacio de observación y acción
        action_low, action_high = self.plant.get_action_bounds()

        observation_low, observation_high = self.plant.get_observation_bounds()

        self.observation_space = spaces.Box(
            low=observation_low,
            high=observation_high,
            dtype=np.float32,
        )

        self.action_space = spaces.Box(
            low=action_low,
            high=action_high,
            dtype=np.float32,
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.plant.reset(seed=seed, options=options)
        observation = self.plant.get_state()

        return observation, {} # Observation, info

    def step(self, action):
        self.plant.step(action)

        observation = self.plant.get_state()
        reward = self.reward_function.calculate(observation, action)

        terminated = False  # El episodio no termina en este entorno
        truncated = False  # No hay truncamiento en este entorno

        if self.renderer is not None:
            self.renderer.render(observation)

        return observation, reward, terminated, truncated, {}  # Observation, reward, terminated, truncated, info

    def close(self):
        if self.renderer is not None:
            self.renderer.close()