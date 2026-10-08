import numpy as np

from plants.simulation.pendulum_plant import PendulumPlant
from rewards.stabilization_reward import StabilizationReward
from renderers.pygame_renderer import PygameRenderer
from environments.environment_adapter import GymEnvironmentAdapter

from stable_baselines3 import PPO
from gymnasium.utils.env_checker import check_env

def main():
    plant = PendulumPlant()
    reward_function = StabilizationReward()
    renderer = PygameRenderer()

    env = GymEnvironmentAdapter(plant, reward_function, renderer)
    check_env(env)
    print("El entorno cumple con las especificaciones de Gymnasium.")

    model = PPO("MlpPolicy", env, verbose=1)
    model.load("ppo_pendulum_model")

    observation, info = env.reset()

    for _ in range(1000):
        action, _ = model.predict(observation, deterministic=True)
        observation, reward, terminated, truncated, info = env.step(action)

        print("Estado después de la acción:", observation, "Recompensa:", reward)

        if terminated or truncated:
            observation, info = env.reset()
            break

    

if __name__ == "__main__":
    main()