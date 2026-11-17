"""Genera una captura de la aplicacion despues de simular tres clics.

Los clics se simulan publicando eventos MOUSEBUTTONDOWN reales en la cola
de Pygame (pygame.event.post), de modo que pasan por el mismo codigo que
un clic hecho con el mouse.

Uso:  python generar_captura.py
"""

from pathlib import Path

import pygame

from aplicacion import Aplicacion

app = Aplicacion()
app.ejecutar_cuadro()

boton_sumar = app.botones[0]
for _ in range(3):
    pygame.event.post(pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, pos=boton_sumar.rect.center, button=1
    ))
    app.ejecutar_cuadro()

# Deja el mouse "encima" del boton para que se vea el efecto hover.
pygame.event.post(pygame.event.Event(
    pygame.MOUSEMOTION, pos=boton_sumar.rect.center, rel=(0, 0), buttons=(0, 0, 0)
))
app.ejecutar_cuadro()

destino = Path(__file__).parent / "capturas" / "contador.png"
destino.parent.mkdir(exist_ok=True)
pygame.image.save(app.pantalla, str(destino))
print(f"Valor del contador: {app.contador.valor}")
print(f"Captura guardada en {destino}")
pygame.quit()
