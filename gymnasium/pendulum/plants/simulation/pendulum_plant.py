import numpy as np
from domain.plant import Plant

class PendulumPlant(Plant):
    """
    Un péndulo simple
    el estado se define por el ángulo y la velocidad angular
    la acción es un torque aplicado al péndulo
    """

    def __init__(
        self, 
        mass: float = 1.0,
        length: float = 1.0,
        gravity: float = 9.81,
        damping: float = 0.05,
        dt: float = 0.02,
    ): 
        self.mass = mass
        self.length = length
        self.gravity = gravity
        self.damping = damping
        self.dt = dt

        self.theta = 0  # Ángulo inicial (en radianes)
        self.theta_dot = 0.0  # Velocidad angular inicial (en radianes por segundo)

    def reset(self, seed=None, options=None) -> None:
        self.theta = 0  # Reinicia el ángulo a la posición inicial
        self.theta_dot = 0.0  # Reinicia la velocidad angular a cero

    def step(self, action: np.ndarray) -> None:
        torque = float(action[0])  # Convertir la acción a un valor flotante

        theta_ddot = (torque - self.damping * self.theta_dot + self.mass * self.gravity * self.length * np.sin(self.theta)) / (self.mass * self.length ** 2)

        self.theta_dot += theta_ddot * self.dt # Integración de la aceleración angular para obtener la velocidad angular
        self.theta += self.theta_dot * self.dt  # Integración de la velocidad angular para obtener el ángulo
        self.theta = self._normalize_angle(self.theta)

    def get_state(self) -> np.ndarray:
        return np.array([self.theta, self.theta_dot], dtype=np.float32)

    def get_action_bounds(self) -> np.ndarray:
        return (
            np.array([-10.0], dtype=np.float32),
            np.array([10.0], dtype=np.float32)
        )

    def get_observation_bounds(self) -> np.ndarray:
        return (
            np.array([-np.pi, -np.inf], dtype=np.float32),
            np.array([np.pi, np.inf], dtype=np.float32)
        )


    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """
        Normaliza el ángulo para que esté en el rango [-pi, pi].
        """
        return (angle + np.pi) % (2 * np.pi) - np.pi

