import numpy as np

# Tamaño del tablero
tamaño_tablero = (15, 15, 10)

# Inicialización de la matriz de probabilidades
matriz_probabilidades = np.ones(tamaño_tablero) / np.prod(tamaño_tablero)

def actualizar_probabilidades(matriz_probabilidades, coordenadas_impacto, impacto):
    # Coordenadas del impacto
    x, y, z = coordenadas_impacto

    # Ajustar las probabilidades según el resultado del impacto
    if impacto == "MISS":
        # Reducir las probabilidades en el área cercana al impacto (por ejemplo)
        radio_miss = 2
        matriz_probabilidades[x - radio_miss:x + radio_miss + 1,
                               y - radio_miss:y + radio_miss + 1,
                               z - radio_miss:z + radio_miss + 1] *= 0.8
    elif impacto == "HIT" or impacto == "SUNK":
        # Establecer la probabilidad en el área del impacto a cero
        matriz_probabilidades[x, y, z] = 0.0

    # Normalizar las probabilidades
    matriz_probabilidades /= np.sum(matriz_probabilidades)

# Ejemplo de uso:
# Después de un disparo, actualiza las probabilidades
impacto = "MISS"  # Cambia esto según el resultado real del disparo
coordenadas_impacto = (5, 7, 3)  # Cambia esto según las coordenadas reales del impacto
actualizar_probabilidades(matriz_probabilidades, coordenadas_impacto, impacto)
