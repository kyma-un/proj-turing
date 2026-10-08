from abc import ABC, abstractmethod
import numpy as np

class Renderer(ABC):
    """
    Clase abstracta que representa un renderizador para visualizar el estado de un sistema dinámico (planta).
    Esta clase define la interfaz que deben implementar todos los renderizadores específicos.
    """

    @abstractmethod
    def render(self, state: np.ndarray) -> None:
        """
        Renderiza el estado actual del sistema.
        """
        pass


    @abstractmethod
    def close(self) -> None:
        """
        Cierra el renderizador y libera los recursos asociados.
        """
        pass
    