"""Aplicacion principal: crea la ventana, recibe los eventos y dibuja."""

import pygame

from boton import Boton
from contador import Contador

ANCHO, ALTO = 480, 360
FPS = 60
COLOR_FONDO = (30, 34, 48)
COLOR_TITULO = (200, 205, 220)
COLOR_NUMERO = (255, 214, 102)
COLOR_AYUDA = (140, 146, 165)


class Aplicacion:
    """Coordina la ventana, el contador y los botones."""

    def __init__(self):
        pygame.init()
        # 1. Ventana principal
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Contador interactivo - Pygame")
        self.reloj = pygame.time.Clock()
        self.ejecutando = True

        # 2. Modelo y componentes graficos
        self.contador = Contador()
        self.fuente_titulo = pygame.font.Font(None, 40)
        self.fuente_numero = pygame.font.Font(None, 120)
        self.fuente_ayuda = pygame.font.Font(None, 24)
        self.botones = [
            Boton(60, 240, 170, 60, "Sumar +1", self.contador.incrementar,
                  color=(46, 134, 222), color_hover=(84, 160, 255)),
            Boton(250, 240, 170, 60, "Reiniciar", self.contador.reiniciar,
                  color=(214, 69, 65), color_hover=(240, 100, 95)),
        ]

    def ejecutar(self) -> None:
        """Bucle principal: eventos -> dibujo -> espera, hasta cerrar."""
        while self.ejecutando:
            self.ejecutar_cuadro()
            self.reloj.tick(FPS)
        pygame.quit()

    def ejecutar_cuadro(self) -> None:
        """Procesa los eventos pendientes y redibuja la ventana una vez."""
        self.procesar_eventos()
        self.dibujar()

    def procesar_eventos(self) -> None:
        # 3. Deteccion de eventos: se leen de la cola de eventos de Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                self.al_presionar_tecla(evento.key)
            for boton in self.botones:
                boton.manejar_evento(evento)

    def al_presionar_tecla(self, tecla: int) -> None:
        """4. Respuesta a eventos de teclado."""
        if tecla == pygame.K_SPACE:
            self.contador.incrementar()
        elif tecla == pygame.K_r:
            self.contador.reiniciar()
        elif tecla == pygame.K_ESCAPE:
            self.ejecutando = False

    def dibujar(self) -> None:
        """5. Se vuelve a dibujar todo con el valor actualizado del contador."""
        self.pantalla.fill(COLOR_FONDO)

        titulo = self.fuente_titulo.render("Contador de clics", True, COLOR_TITULO)
        self.pantalla.blit(titulo, titulo.get_rect(center=(ANCHO // 2, 50)))

        numero = self.fuente_numero.render(str(self.contador.valor), True, COLOR_NUMERO)
        self.pantalla.blit(numero, numero.get_rect(center=(ANCHO // 2, 150)))

        for boton in self.botones:
            boton.dibujar(self.pantalla)

        ayuda = self.fuente_ayuda.render(
            "Espacio: sumar   R: reiniciar   Esc: salir", True, COLOR_AYUDA
        )
        self.pantalla.blit(ayuda, ayuda.get_rect(center=(ANCHO // 2, 330)))

        pygame.display.flip()
