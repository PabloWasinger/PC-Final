import numpy as np
import random
import funciones
import vehiculos

np.set_printoptions(threshold=np.inf)

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
    x, y, z = (random.randint(0,14), random.randint(0,14), random.randint(0,9))

    while hit_board [x][y][z] != "?":
        x, y, z = (random.randint(0,14), random.randint(0,14), random.randint(0,9))
    return (x, y, z)





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
    board = np.full((15, 15, 10), 'EMPTY', dtype='object')
        
    molde_b0 = (0, 3, 0, 3, 0, 3)
    x,y,z=5,5,5
    board[(molde_b0[0] + x): (molde_b0[1] + x), (molde_b0[2] + y):(molde_b0[3] + y), (molde_b0[4] + z):(molde_b0[5] + z)] = "BALLOON_0" 

    # molde_b1 = (0, 3, 0, 3, 0, 3)
    # x,y,z=0,0,7
    # board[(molde_b1[0] + x): (molde_b1[1] + x), (molde_b1[2] + y):(molde_b1[3] + y), (molde_b1[4] + z):(molde_b1[5] + z)] = "BALLOON_1" 
    
    # molde_b2 = (0, 3, 0, 3, 0, 3)
    # x,y,z=12,0,12
    # board[(molde_b2[0] + x): (molde_b2[1] + x), (molde_b2[2] + y):(molde_b2[3] + y), (molde_b2[4] + z):(molde_b2[5] + z)] = "BALLOON_2" 
    
    # molde_b3 = (0, 3, 0, 3, 0, 3)
    # x,y,z=0,12,0
    # board[(molde_b3[0] + x): (molde_b3[1] + x), (molde_b3[2] + y):(molde_b3[3] + y), (molde_b3[4] + z):(molde_b3[5] + z)] = "BALLOON_3" 
    
    # molde_b4 = (0, 3, 0, 3, 0, 3)
    # x,y,z=0,12,7
    # board[(molde_b4[0] + x): (molde_b4[1] + x), (molde_b4[2] + y):(molde_b4[3] + y), (molde_b4[4] + z):(molde_b4[5] + z)] = "BALLOON_4" 
    
    molde_z0 = (0, 5, 0, 2, 0, 2)
    x,y,z=5,5,0
    board[(molde_z0[0] + x): (molde_z0[1] + x), (molde_z0[2] + y):(molde_z0[3] + y), (molde_z0[4] + z):(molde_z0[5] + z)] = "ZEPPELIN_0"
        
    # molde_z1 = (0, 2, 0, 5, 0, 2)
    # x,y,z=13,0,8
    # board[(molde_z1[0] + x): (molde_z1[1] + x), (molde_z1[2] + y):(molde_z1[3] + y), (molde_z1[4] + z):(molde_z1[5] + z)] = "ZEPPELIN_1"
        
    molde3 = (0, 1, 0, 1, 0, 10)
    x,y,z=14,14,0
    board[(molde3[0] + x): (molde3[1] + x), (molde3[2] + y):(molde3[3] + y), (molde3[4] + z):(molde3[5] + z)] = "ELEVATOR"

    body_0 = (0, 4, 1, 2, 0, 1) 
    wing_0 = (2, 3, 0, 3, 0, 1)
    tail_0 = (0, 1, 1, 2, 0, 2)
    x,y,z=0,0,0
    board[(body_0[0] + x):(body_0[1] + x), (body_0[2] + y):(body_0[3] + y), (body_0[4] + z):(body_0[5] + z)] = "PLANE_0"
    board[(wing_0[0] + x):(wing_0[1] + x), (wing_0[2] + y):(wing_0[3] + y), (wing_0[4] + z):(wing_0[5] + z)] = "PLANE_0"
    board[(tail_0[0] + x):(tail_0[1] + x), (tail_0[2] + y):(tail_0[3] + y), (tail_0[4] + z):(tail_0[5] + z)] = "PLANE_0"
    
    # body_1 = (0, 4, 1, 2, 0, 1) 
    # wing_1 = (2, 3, 0, 3, 0, 1)
    # tail_1 = (0, 1, 1, 2, 0, 2)
    # x,y,z=0,0,0
    # board[(body_1[0] + x):(body_1[1] + x), (body_1[2] + y):(body_1[3] + y), (body_1[4] + z):(body_1[5] + z)] = "PLANE_1"
    # board[(wing_1[0] + x):(wing_1[1] + x), (wing_1[2] + y):(wing_1[3] + y), (wing_1[4] + z):(wing_1[5] + z)] = "PLANE_1"
    # board[(tail_1[0] + x):(tail_1[1] + x), (tail_1[2] + y):(tail_1[3] + y), (tail_1[4] + z):(tail_1[5] + z)] = "PLANE_1"
    
    # body_2 = (0, 4, 1, 2, 0, 1) 
    # wing_2 = (2, 3, 0, 3, 0, 1)
    # tail_2 = (0, 1, 1, 2, 0, 2)
    # x,y,z=0,0,0
    # board[(body_2[0] + x):(body_2[1] + x), (body_2[2] + y):(body_2[3] + y), (body_2[4] + z):(body_2[5] + z)] = "PLANE_2"
    # board[(wing_2[0] + x):(wing_2[1] + x), (wing_2[2] + y):(wing_2[3] + y), (wing_2[4] + z):(wing_2[5] + z)] = "PLANE_2"
    # board[(tail_2[0] + x):(tail_2[1] + x), (tail_2[2] + y):(tail_2[3] + y), (tail_2[4] + z):(tail_2[5] + z)] = "PLANE_2"
    
    return board



    

    



def get_vehicles(tablero):
    """Crea un diccionario con todos los vehiculos como objetos"""
    vehiculos_computadora = {}
    for i in range(1):
        v = f"BALLOON_{i}"
        vehiculos_computadora[v] = vehiculos.Globo("globo")
        mask = tablero == v
        vehiculos_computadora[v].posicion[mask] = True
        vehiculos_computadora[v].indices = np.where(vehiculos_computadora[v].posicion)

    for i in range(1):
        v = f"ZEPPELIN_{i}"
        vehiculos_computadora[v] = vehiculos.Zeppelin("zeppelin")
        mask = tablero == v
        vehiculos_computadora[v].posicion[mask] = True
        vehiculos_computadora[v].indices = np.where(vehiculos_computadora[v].posicion)

    for i in range(1):
        v = f"PLANE_{i}"
        vehiculos_computadora[v] = vehiculos.Avion("avion")
        mask = tablero == v
        vehiculos_computadora[v].posicion[mask] = True
        vehiculos_computadora[v].indices = np.where(vehiculos_computadora[v].posicion)

    v = f"ELEVATOR"
    vehiculos_computadora[v]= vehiculos.Elevador("elevador")
    mask = tablero == v
    vehiculos_computadora[v].posicion[mask] = True
    vehiculos_computadora[v].indices = np.where(vehiculos_computadora[v].posicion)

    return vehiculos_computadora