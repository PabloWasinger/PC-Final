from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import funciones
from typing import Tuple, Optional, Any

def main():
    pass


class Tableros():
    def __init__(self, jugador):
        self.jugador = jugador # Es jugador o computadora?
        self.binario = np.zeros((15, 15, 10), dtype=bool) # Tablero con 1s y 0s donde hay o no valores ocupados correspondientemente
        self.plotboard = None # Plot para dibujar usando matplotlib
        self.titulo = None # Titulo del tablero
        self.posicion = None # Posicion del tablero en la figura
        self.colors = np.empty(self.binario.shape, dtype=object) # Tablero con los colores de cada cuadrado


    def dibujar_tablero(self)->None:
        """
        Dibujar el tablero en la figura usando matplotlib
        Establece la visualización del tablero tridimensional
        """
        self.plotboard.set_xlabel('x')
        self.plotboard.set_ylabel('y')
        self.plotboard.set_zlabel('z')
        self.plotboard.set_title(self.titulo)
        self.plotboard.set_xlim(0, 15)
        self.plotboard.set_ylim(0, 15)
        self.plotboard.set_zlim(0, 10)
 


class HitBoard(Tableros):
    def __init__(self, jugador):
        super().__init__(jugador)
        self.strings = np.full((15, 15, 10), '?', dtype='object')
        self.titulo = "Player 1 Hitboard"
        self.posicion = (1, 2, 2)
    
    def shoot_board(self, coords: Tuple[int, int, int], vehiculo: Optional[Any])->None:
        """
        La función se encarga de realizar el disparo.
        Toma las coordenadas de un disparo y si hubo o no hit, actualiza el estado del tablero y realiza la 
        representacion gráfica.
        Recibe:
        - coords: Una tupla con las coordenadas del disparo en el tablero.
        - vehiculo: Un objeto que representa el vehículo.
        """

        x, y, z = coords

        if vehiculo: # Si hubo hit

            if vehiculo.health == 0: # Si se hundió el vehiculo
                mask = vehiculo.posicion != 0 # Posicion del vehiculo
                self.binario[mask] = True # Asigna todos las posiciones del vehiculo
                self.strings[mask] = "SUNK"

            else:
                self.binario[x][y][z] = True
                self.strings[x][y][z] = "HIT"
                
        else:
            self.binario[x][y][z] = True # Asigna true al lugar del hit
            self.strings[x][y][z] = "MISS"

        # Dibujar en el tablero el hit si es de un jugador
        if self.jugador == "Player":
            if vehiculo and vehiculo.health == 0: # Se hundio el vehiculo
                #Pintar vehiculo (gris)
                for index in zip(*vehiculo.indices):
                    self.colors[index] = (0, 0, 0, 0.2)
            elif vehiculo: #Hubo hit
                self.colors[x][y][z] = (0, 1, 0, 0.5) # Pintar verde
            else: # No hubo hit
                self.colors[x][y][z] = (1, 0, 0, 0.2) # Pintar rojo
            funciones.dibujar_hitboard(self)



class PlayerBoard(Tableros):
    def __init__(self, jugador):
        super().__init__(jugador)
        self.titulo = "Player 1 Board"
        self.posicion = (1, 2, 1)
        self.strings = np.full((15, 15, 10), "EMPTY", dtype='object')
        self.vida = 11
    
    


    def draw_vehicle(self, vehiculo:Any)->None:
        """
        La función dibuja el vehiculo en el tablero.
        Establece la visualización del vehiculo en el tablero.
        Recibe:
        - vehiculo: Un objeto que representa el vehículo.
        """
        mask = vehiculo.posicion != 0
        self.binario[mask] = True
        self.strings[vehiculo.indices] = vehiculo.objeto
        for index in zip(*vehiculo.indices):
                self.colors[index] = vehiculo.color
        funciones.dibujar_playerboard(self)



    def recibir_tiro(self, coords: Tuple[int, int, int], vehiculo)->None:
        """
        La función actualiza el tablero luego de recibir el disparo.
        Toma las coordenadas de un disparo y si hubo o no hit, actualiza el estado del tablero y realiza la 
        representacion gráfica.
        Recibe:
        - coords: Una tupla con las coordenadas del disparo en el tablero.
        - vehiculo: Un objeto que representa el vehículo.
        """

        if vehiculo.health == 0: # Si se hundio el vehiculo oscurecerlo
            for index in zip(*vehiculo.indices):
                self.colors[index] = (0.2, 0.2, 0.2, 0.2)
        else: # Si no se hundió el vehicul, pintar el lugar del hit como verde
            x, y, z = coords
            self.colors[x][y][z] = (0, 1, 0, 0.8)
        
        funciones.dibujar_playerboard(self)


    def map_computer_board(self)->None:
        """
        La función se encarga de mapear el tablero asignando "True" a las posiciones ocupadas.
        """
        mask = self.strings != "EMPTY"
        self.binario[mask] = True
            

        
        
        

if __name__ == "__main__":
    main()