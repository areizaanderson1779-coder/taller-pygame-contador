"""Componente visual reutilizable: un boton rectangular con texto.

Pygame no trae botones ya hechos, asi que este componente se construye
con un Rect (area), una fuente (texto) y una funcion callback (accion).
"""

from typing import Callable

import pygame

COLOR_TEXTO = (255, 255, 255)


class Boton:
    """Boton que se dibuja a si mismo y ejecuta una accion al hacer clic."""

    def __init__(
        self,
        x: int,
        y: int,
        ancho: int,
        alto: int,
        texto: str,
        accion: Callable[[], None],
        color: tuple[int, int, int],
        color_hover: tuple[int, int, int],
    ):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self._accion = accion
        self._color = color
        self._color_hover = color_hover
        self._resaltado = False
        self._fuente = pygame.font.Font(None, 36)

    def manejar_evento(self, evento: pygame.event.Event) -> None:
        """Revisa si el evento le corresponde a este boton."""
        if evento.type == pygame.MOUSEMOTION:
            # Cambia de color cuando el mouse pasa por encima.
            self._resaltado = self.rect.collidepoint(evento.pos)
        elif (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1  # 1 = boton izquierdo
            and self.rect.collidepoint(evento.pos)
        ):
            self._accion()

    def dibujar(self, superficie: pygame.Surface) -> None:
        color = self._color_hover if self._resaltado else self._color
        pygame.draw.rect(superficie, color, self.rect, border_radius=12)
        imagen_texto = self._fuente.render(self.texto, True, COLOR_TEXTO)
        superficie.blit(imagen_texto, imagen_texto.get_rect(center=self.rect.center))
