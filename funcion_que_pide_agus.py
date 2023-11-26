import numpy as np
import random
import funciones


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
    board = np.full((15, 15, 10), 'EMPTY', dtype='str')
        
    molde1 = (0, 3, 0, 3, 0, 3)
    x,y,z=5,5,5
    board[(molde1[0] + x): (molde1[1] + x), (molde1[2] + y):(molde1[3] + y), (molde1[4] + z):(molde1[5] + z)] = "GLOBO" 

    molde2 = (0, 5, 0, 2, 0, 2)
    x,y,z=5,5,0
    board[(molde2[0] + x): (molde2[1] + x), (molde2[2] + y):(molde2[3] + y), (molde2[4] + z):(molde2[5] + z)] = "ZEPPELIN"
        
    molde3 = (0, 1, 0, 1, 0, 10)
    x,y,z=14,14,0
    board[(molde3[0] + x): (molde3[1] + x), (molde3[2] + y):(molde3[3] + y), (molde3[4] + z):(molde3[5] + z)] = "ELEVATOR"

    body = (0, 4, 1, 2, 0, 1) 
    wing = (2, 3, 0, 3, 0, 1)
    tail = (0, 1, 1, 2, 0, 2)
    x,y,z=0,0,0
    board[(body[0] + x):(body[1] + x), (body[2] + y):(body[3] + y), (body[4] + z):(body[5] + z)] = "PLANE"
    board[(wing[0] + x):(wing[1] + x), (wing[2] + y):(wing[3] + y), (wing[4] + z):(wing[5] + z)] = "PLANE"
    board[(tail[0] + x):(tail[1] + x), (tail[2] + y):(tail[3] + y), (tail[4] + z):(tail[5] + z)] = "PLANE"



    



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
