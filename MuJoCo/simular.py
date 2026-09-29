import time
import numpy as np
import mujoco
import mujoco.viewer

XML_PATH = "pendulo_rueda_inercial.xml"

def controlador(t: float, theta: float, theta_dot: float, wheel_dot: float) -> float:
    torque_max = 1.0
    frecuencia_hz = 1.0
    return torque_max * np.sin(2 * np.pi * frecuencia_hz * t)


def main():
    #Inicialización
    model = mujoco.MjModel.from_xml_path(XML_PATH)
    data = mujoco.MjData(model)

    # indices art
    pend_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "pendulo_joint")
    rueda_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "rueda_joint")
    pend_qpos = model.jnt_qposadr[pend_id]
    pend_qvel = model.jnt_dofadr[pend_id]
    rueda_qvel = model.jnt_dofadr[rueda_id]

    #Perturbación desequilibradora
    data.qpos[pend_qpos] = 0.05
    mujoco.mj_forward(model, data)

    #Visor Nativo de Mujoco
    print("Visor")
    with mujoco.viewer.launch_passive(model, data) as viewer:
        t0 = time.time()
        i_print = 0.0

        while viewer.is_running():
            t = data.time

            theta = data.qpos[pend_qpos]
            theta_dot = data.qvel[pend_qvel]
            wheel_dot = data.qvel[rueda_qvel]

            data.ctrl[0] = controlador(t, theta, theta_dot, wheel_dot)

            mujoco.mj_step(model, data)
            viewer.sync()

            #Imprimir estado
            if t - i_print > 0.5:
                print(
                    f"t={t:6.2f}s  theta={theta:+6.3f} rad  "
                    f"theta_dot={theta_dot:+7.3f} rad/s  "
                    f"wheel_dot={wheel_dot:+8.3f} rad/s"
                )
                i_print = t

            # Sincroniza con el reloj real para que se vea a velocidad
            # natural (MuJoCo por si solo simula mas rapido que tiempo real)
            elapsed_wall = time.time() - t0
            sleep_time = t - elapsed_wall
            if sleep_time > 0:
                time.sleep(sleep_time)


if __name__ == "__main__":
    main()
