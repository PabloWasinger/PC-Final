import numpy as np
import random
import vehiculos

def next_turn(hit_board: tuple) -> tuple:
    """Returns the coordinates to shoot next.

    Args:
        hit_board (tuple): A 3D iterable of strings representing the hit board.
        Each cell can be accessed by hit_board[x][y][z].

        Each cell has 4 possible values:
        - '?': No shot has been done there.
        - 'HIT': An airship has been hit there before.
        - 'MISS': A shot has been done there but did not hit any airship.
        - 'SUNK': An airship was there but has already been shot down entirely.

    Returns:
        tuple: (x,y,z) to shoot at.
    """

    




def get_starting_board():
    """
    Gives the board with the airships placed on it. The board is a 3D iterable of 
    strings. 

    Each cell has 12 possible values: 'EMPTY', 'BALLOON_0', 'BALLOON_1',
    'BALLOON_2', 'BALLOON_3' 'BALLOON_4', 'ZEPPELIN_0', 'ZEPPELIN_1', 'PLANE_0',
    'PLANE_1', 'PLANE_2', 'ELEVATOR'.

    Returns:
        tuple: A tuple of tuples of tuples of strings representing the board.
        Each cell can be accessed by board[x][y][z].
    """


def get_vehicles():
    """Crea un diccionario con todos los vehiculos como objetos"""
    veihculos = {}
    for i in range(5):
        vehiculos[f"BALLOON_{i}"] = vehiculos.Globo()

    for i in range(2):
        vehiculos[f"ZEPPELIN_{i}"] = vehiculos.Zeppelin()

    for i in range(3):
        vehiculos[f"PLANE_{i}"] = vehiculos.Avion()

    vehiculos[f"ELEVATOR"] = vehiculos.Elevador()

    return vehiculos