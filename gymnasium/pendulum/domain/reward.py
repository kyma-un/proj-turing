from abc import ABC, abstractmethod
import numpy as np

class RewardFunction(ABC):

    @abstractmethod
    def calculate(
        self, 
        state: np.ndarray,
        action: np.ndarray,
    ) -> float:
        """
        Calcula la recompensa basada en el estado actual y la acción tomada.
        """
        pass

    