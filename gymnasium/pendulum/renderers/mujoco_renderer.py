import time

import mujoco
import mujoco.viewer
import numpy as np

from domain.renderer import Renderer


class MujocoRenderer(Renderer):
    """
    Muestra la simulación en el visor nativo de MuJoCo.
    No dibuja a partir de `state`: lee directamente el MjData de la planta.
    """

    def __init__(self, plant, realtime: bool = True):
        self.plant = plant          # Comparte model y data con la planta
        self.realtime = realtime
        self.viewer = None
        self._t0_wall = None
        self._t0_sim = None
        self._last_sim = None

    def _initialize(self) -> None:
        self.viewer = mujoco.viewer.launch_passive(self.plant.model, self.plant.data)
        self._t0_wall = time.time()
        self._t0_sim = self.plant.data.time                
        self._last_sim = self.plant.data.time

    def render(self, state: np.ndarray) -> None:
        if self.viewer is None:
            self._initialize()

        if not self.viewer.is_running():  # El usuario cerró la ventana
            return

        self.viewer.sync()

        if self.realtime:
            sim_t = self.plant.data.time
            # Si el tiempo simulado retrocedió, hubo un reset: reinicia los relojes
            if sim_t < self._last_sim:
                self._t0_wall, self._t0_sim = time.time(), sim_t
            self._last_sim = sim_t

            ahead = (sim_t - self._t0_sim) - (time.time() - self._t0_wall)
            if ahead > 0:
                time.sleep(ahead)

    def close(self) -> None:
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None