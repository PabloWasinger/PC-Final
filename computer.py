import numpy as np
import vehiculos

np.set_printoptions(threshold=np.inf)

def next_turn(hit_board:tuple, computer) -> tuple:
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
    # x, y, z = (random.randint(0,14), random.randint(0,14), random.randint(0,9))

    # while hit_board [x][y][z] != "?":
    #     x, y, z = (random.randint(0,14), random.randint(0,14), random.randint(0,9))
    # return (x, y, z)


    probability_map = computer.gen_prob_map(hit_board)
    max_indices = np.where(probability_map == np.amax(probability_map))
    return max_indices


    





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
    pos_vehiculos = [("BALLOON_0",(0,0,0),(0, 3, 0, 3, 0, 3)),("BALLOON_1",(0,0,7),(0, 3, 0, 3, 0, 3)),("BALLOON_2",(12,0,12),(0, 3, 0, 3, 0, 3)),("BALLOON_3",(0,12,0),(0, 3, 0, 3, 0, 3)),("BALLOON_4",(0,12,7),(0, 3, 0, 3, 0, 3)),
                     ("ZEPPELIN_0",(),(0, 5, 0, 2, 0, 2)),("ZEPPELIN_1",(),(0, 5, 0, 2, 0, 2)),("ELEVATOR",(14,14,0),(0, 1, 0, 1, 0, 10))
                     ("PLANE_0",()),("PLANE_1",()),("PLANE_2",())]
    
    for vehiculo, coordenadas, molde in pos_vehiculos:
        x,y,z= coordenadas
        board[(molde[0] + x): (molde[1] + x), (molde[2] + y):(molde[3] + y), (molde[4] + z):(molde[5] + z)] = vehiculo 
        if vehiculo == "PLANE_0" or vehiculo == "PLANE_1" or vehiculo == "PLANE_2":
            body_0,wing_0,tail_0 = (0, 4, 1, 2, 0, 1),(2, 3, 0, 3, 0, 1),(0, 1, 1, 2, 0, 2)
            board[(body_0[0] + x):(body_0[1] + x), (body_0[2] + y):(body_0[3] + y), (body_0[4] + z):(body_0[5] + z)] = vehiculo
            board[(wing_0[0] + x):(wing_0[1] + x), (wing_0[2] + y):(wing_0[3] + y), (wing_0[4] + z):(wing_0[5] + z)] = vehiculo
            board[(tail_0[0] + x):(tail_0[1] + x), (tail_0[2] + y):(tail_0[3] + y), (tail_0[4] + z):(tail_0[5] + z)] = vehiculo
            

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





        

        


        
