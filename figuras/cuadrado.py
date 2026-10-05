def area_cuadrado(lado):
    """Devuelve el área de un cuadrado."""
    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero")
    return lado ** 2