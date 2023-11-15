import matplotlib.pyplot as plt
import numpy as np
import funciones

class Vehiculos():
    issunken = False
    def __init__(self):
        pass

class Globo(Vehiculos):
    health = 1
    def __init__(self):
        pass

    def position_globo(indices, axes):
        x, y, z = indices

        # Pedimos las coordenadas y asignamos la posicion del globo
        x_offset, y_offset, z_offset = funciones.get_coords()
        posicion  = (x >= 0 + x_offset) & (x < 3 + x_offset) & (y >= 0 + y_offset) (y < 3 + y_offset) & (z >= 0 + z_offset) (z < 3 + z_offset)
        
        # Chequear si colisiona con otros objetos o se va fuera del espacio
        colision = funciones.check_collision(posicion)
        while colision:

            # Si colisiona pedir datos devuelta y volver a posicionar el globo
            if colision == 1:
                print("El globo no puede colisionarse con otro vehiculo!\nEscriba las coordenadas devuelta: ")
            elif colision == 2:
                print("EL globo debe estar dentro del espacio!\nEscriba las coordenadas devuelta: ")

            x_offset, y_offset, z_offset = funciones.get_coords()
            posicion  = (x >= 0 + x_offset) & (x < 3 + x_offset) & (y >= 0 + y_offset) (y < 3 + y_offset) & (z >= 0 + z_offset) (z < 3 + z_offset)

            colision = funciones.check_collision(posicion)
        

class Zeppelin(Vehiculos):
    health = 3
    def __init__(self):
        pass

class Avion(Vehiculos):
    health = 2
    def __init__(self):
        pass

class Elevador(Vehiculos):
    health = 4
    def __init__(self):
        pass

