import math

import numpy as np
import pygame

from domain.renderer import Renderer

class PygameRenderer(Renderer):

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        fps: int = 60,
    ):
        self.width = width
        self.height = height
        self.fps = fps

        self.screen = None
        self.clock = None

    def _initialize(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Pendulum Simulation")

        self.clock = pygame.time.Clock()

    def render(self, state: np.ndarray) -> None:
        if self.screen is None or self.clock is None:
            self._initialize()

        theta = float(state[0])  # Ángulo del péndulo

        self._handle_events()
        self._draw_background()
        self._draw_pendulum(theta)

        pygame.display.flip()

        self.clock.tick(self.fps)

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()

    def _draw_background(self) -> None:
        self.screen.fill((255, 255, 255))  # Fondo blanco

    def _draw_pendulum(self, theta: float) -> None:

        origin_x = self.width // 2
        origin_y = 300

        length = 200  # Longitud del péndulo

        bob_x = (
            origin_x - length * math.sin(theta) # se pone menos porque el ángulo es medido desde la vertical hacia la izquierda
        )

        bob_y = (
            origin_y - length * math.cos(theta)  # se pone menos porque el ángulo es medido desde la vertical hacia la izquierda
        )

        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            (origin_x, origin_y),
            (bob_x, bob_y),
            5,
        )

        pygame.draw.circle(
            self.screen,
            (255, 0, 0),
            (int(bob_x), int(bob_y)),
            25,
        )

        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (origin_x, origin_y),
            8,
        )


    def close(self) -> None:
        if self.screen is not None:
            pygame.quit()
            self.screen = None
            self.clock = None