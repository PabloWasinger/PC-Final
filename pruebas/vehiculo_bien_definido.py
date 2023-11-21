import matplotlib.pyplot as plt
import numpy as np
import funciones

class Vehiculos():
    
    def __init__(self):
         self.issunken = False

    def position(indices,size, axes):
        x, y, z = indices

        # Pedimos las coordenadas y asignamos la posicion del vehiculo
        x_offset, y_offset, z_offset = funciones.get_coords()
        posicion  = (x >= size[0] + x_offset) & (x < size[1] + x_offset) & (y >= size[2] + y_offset) (y < size[3] + y_offset) & (z >= size[4] + z_offset) (z < size[5] + z_offset)
        
        # Chequear si colisiona con otros objetos o se va fuera del espacio
        colision = funciones.check_collision(posicion)
        while colision:

            # Si colisiona pedir datos devuelta y volver a posicionar el vehiculo
            if colision == 1:
                print("El globo no puede colisionarse con otro vehiculo!\nEscriba las coordenadas devuelta: ")
            elif colision == 2:
                print("EL globo debe estar dentro del espacio!\nEscriba las coordenadas devuelta: ")

            x_offset, y_offset, z_offset = funciones.get_coords()
            posicion  = (x >= size[0] + x_offset) & (x < size[1] + x_offset) & (y >= size[2] + y_offset) (y < size[3] + y_offset) & (z >= size[4] + z_offset) (z < size[5] + z_offset)
            colision = funciones.check_collision(posicion)
ytrcuy = 1      