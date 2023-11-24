
import random

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
    x, y, z = (random.randint(0,15), random.randint(0,15), random.randint(0,10))

    while hit_board [x][y][z] != "?":
        x, y, z = (random.randint(0,15), random.randint(0,15), random.randint(0,10))
    return (x,y,z)





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
    



def rand_coords(clase=None):
    """Pide y devuelve coordenadas de modo (x y z) o (x y) si es un elevador"""

    while True:
        x,y,z = random.randint(0,15),random.randint(0,15),random.randint(0,10)
        coords = x,y,z 
        splitcoords = coords.split()
        if clase == "elevador":
            x, y = (map(int, splitcoords))
            z = 0
        else:
            x, y, z = (map(int, splitcoords))
            
    return x, y, z
