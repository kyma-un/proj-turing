from simple_env import SimpleEnv

env = SimpleEnv()
observation, info = env.reset()

print("Observación inicial:", observation)

for i in range(50):
    action = env.action_space.sample()  # Tomar una acción aleatoria
    observation, reward, terminated, truncated, info = env.step(action)

    print(f"Paso {i + 1}: Acción: {action}, Observación: {observation}, Recompensa: {reward}")

    if terminated or truncated:
        print("El episodio ha terminado.")
        break