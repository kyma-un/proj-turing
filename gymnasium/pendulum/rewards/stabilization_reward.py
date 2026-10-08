import numpy as np
from domain.reward import RewardFunction

class StabilizationReward(RewardFunction):
    def __init__(
        self, 
        theta_weight: float = 1.0,
        velocity_weight: float = 0.0,
        torque_weight: float = 0.00,
    ):
        self.theta_weight = theta_weight
        self.velocity_weight = velocity_weight
        self.torque_weight = torque_weight

    def calculate(
        self, 
        state: np.ndarray,
        action: np.ndarray,
    ) -> float:
        theta, theta_dot = state
        torque = action[0]
        
        # Recompensa basada en la desviación del ángulo y la velocidad angular
        reward = -(
            self.theta_weight * (theta ** 2)  # Penaliza la desviación del ángulo
            + self.velocity_weight * (theta_dot ** 2)  # Penaliza la velocidad angular
            + self.torque_weight * (torque ** 2) # Penaliza el uso de torque excesivo
        )

        print("theta",theta**2, "reward", reward )
        
        return reward