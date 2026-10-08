from abc import ABC, abstractmethod
import numpy as np

class Plant(ABC):
    """
    Clase abstracta que representa un sistema dinámico (planta) en el entorno de simulación.
    Esta clase define la interfaz que deben implementar todas las plantas específicas.
    Los métodos están enfocados al uso en gymnasium
    """
    @abstractmethod
    def reset(self, seed=None, options=None) -> None: 
        """
        Reinicia el estado de la planta a un estado inicial.
        """
        pass

    @abstractmethod
    def step(self, action: np.ndarray) -> None:
        """
        Aplica una acción al sistema y actualiza su estado.
        """
        pass

    @abstractmethod
    def get_state(self) -> np.ndarray:
        """
        Devuelve el estado actual del sistema.
        """
        pass

    @abstractmethod
    def get_action_bounds(self) -> np.ndarray:
        """
        Devuelve los límites de acción del sistema.
        """
        pass


    @abstractmethod
    def get_observation_bounds(self) -> np.ndarray:
        """
        Devuelve los límites de observación del sistema.
        """
        pass