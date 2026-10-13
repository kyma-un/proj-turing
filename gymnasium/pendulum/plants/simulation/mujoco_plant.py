from pathlib import Path

import mujoco
import numpy as np

from domain.plant import Plant

# proj-turing/MuJoCo/pendulo_rueda_inercial.xml, sin importar desde dónde se ejecute
XML_DEFAULT = Path(__file__).resolve().parents[4] / "MuJoCo" / "pendulo_rueda_inercial.xml"


class MujocoPlant(Plant):
    """
    Péndulo con rueda inercial simulado en MuJoCo.
    La física (masas, longitudes, fricción) vive en el XML, no aquí.
    Estado: [theta, theta_dot, wheel_dot]. Acción: torque sobre la rueda.
    """

    def __init__(self, xml_path: str | Path = XML_DEFAULT, dt: float = 0.02, init_noise: float = 0.05):
        self.model = mujoco.MjModel.from_xml_path(str(xml_path))
        self.data = mujoco.MjData(self.model)

        # Cuántos pasos internos de MuJoCo (2 ms) caben en un paso del agente
        self.frame_skip = max(1, round(dt / self.model.opt.timestep))
        self.dt = self.frame_skip * self.model.opt.timestep

        self.init_noise = init_noise
        self.rng = np.random.default_rng()

    def reset(self, seed=None, options=None) -> None:
        if seed is not None:
            self.rng = np.random.default_rng(seed)

        mujoco.mj_resetData(self.model, self.data)
        self.data.qpos[0] = self.rng.uniform(-self.init_noise, self.init_noise)  # Pequeño empujón en theta
        mujoco.mj_forward(self.model, self.data)  # Recalcula posiciones y sensores sin avanzar el tiempo

    def step(self, action: np.ndarray) -> None:
        self.data.ctrl[0] = float(action[0])  # MuJoCo recorta al ctrlrange del XML
        mujoco.mj_step(self.model, self.data, nstep=self.frame_skip)

    def get_state(self) -> np.ndarray:
        theta, theta_dot, wheel_dot = self.data.sensordata  # Orden de <sensor> en el XML
        return np.array([self._normalize_angle(theta), theta_dot, wheel_dot], dtype=np.float32)

    def get_action_bounds(self) -> np.ndarray:
        low, high = self.model.actuator_ctrlrange[0]
        return (
            np.array([low], dtype=np.float32),
            np.array([high], dtype=np.float32)
        )

    def get_observation_bounds(self) -> np.ndarray:
        return (
            np.array([-np.pi, -np.inf, -np.inf], dtype=np.float32),
            np.array([np.pi, np.inf, np.inf], dtype=np.float32)
        )

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """
        Normaliza el ángulo para que esté en el rango [-pi, pi].
        """
        return (angle + np.pi) % (2 * np.pi) - np.pi