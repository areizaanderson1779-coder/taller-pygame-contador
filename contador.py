"""Modelo del contador: guarda el valor y las reglas para cambiarlo.

No sabe nada de Pygame; solo administra el estado.
"""


class Contador:
    """Lleva la cuenta de las interacciones del usuario."""

    def __init__(self, valor_inicial: int = 0):
        if not isinstance(valor_inicial, int) or valor_inicial < 0:
            raise ValueError("El valor inicial debe ser un entero mayor o igual a 0.")
        self._valor = valor_inicial

    @property
    def valor(self) -> int:
        """Valor actual (solo lectura)."""
        return self._valor

    def incrementar(self) -> None:
        self._valor += 1

    def reiniciar(self) -> None:
        self._valor = 0
