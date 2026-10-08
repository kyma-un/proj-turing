# import numpy as np
# from plants.simulation.pendulum_plant import PendulumPlant

# plant = PendulumPlant()
# plant.reset()
# print("Estado inicial:", plant.get_state())

# for _ in range(100):
#     action = np.array([0.1])  # Aplicar un torque constante
#     plant.step(action)
#     print("Estado después de la acción:", plant.get_state())

### --------------------------------------------------------------------

# import numpy as np
# from rewards.stabilization_reward import StabilizationReward

# reward_function = StabilizationReward()

# state = np.array([0.0, 0.0])  # Estado inicial del péndulo (ángulo, velocidad angular)
# action = np.array([0.0])  # Acción aplicada (torque)


# reward = reward_function.calculate(state, action)
# print("Recompensa calculada:", reward)

### --------------------------------------------------------------------
# import numpy as np

# from plants.simulation.pendulum_plant import PendulumPlant
# from renderers.pygame_renderer import PygameRenderer


# plant = PendulumPlant()
# renderer = PygameRenderer()

# plant.reset()

# for _ in range(1000):

#     action = np.array([0.01])

#     plant.step(action)

#     state = plant.get_state()

#     renderer.render(state)

# renderer.close()

### --------------------------------------------------------------------
import numpy as np

from plants.simulation.pendulum_plant import PendulumPlant
from rewards.stabilization_reward import StabilizationReward
from renderers.pygame_renderer import PygameRenderer
from environments.environment_adapter import GymEnvironmentAdapter

from gymnasium.utils.env_checker import check_env

def main():
    plant = PendulumPlant()
    reward_function = StabilizationReward()
    renderer = PygameRenderer()

    env = GymEnvironmentAdapter(plant, reward_function, renderer)

    check_env(env)
    print("El entorno cumple con las especificaciones de Gymnasium.")

    observation, info = env.reset()

    print("Estado inicial:", observation)

    for _ in range(1000):
        action =  np.array([0.1]) #env.action_space.sample()  # Muestra una acción aleatoria
        observation, reward, terminated, truncated, info = env.step(action)

        print("Estado después de la acción:", observation, "Recompensa:", reward)


        if terminated or truncated:
            observation, info = env.reset()
            break
    env.close()

if __name__ == "__main__":
    main()