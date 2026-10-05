from tabulate import tabulate
from figuras.cuadrado import area_cuadrado

resultados = [
    ["Cuadrado (lado 4)", area_cuadrado(4)],
]

print(tabulate(resultados, headers=["Figura", "Área"]))