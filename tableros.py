from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import funciones

def main():
    pass


class Tableros():
    def __init__(self, jugador):
        self.jugador = jugador # Es jugador o computadora?
        self.binario = np.zeros((15, 15, 10), dtype=bool) # Tablero con 1s y 0s donde hay o no valores ocupados correspondientemente
        self.strings = None # Tablero con strings, (nombre de vehiculo o hits)
        self.plotboard = None # Plot para dibujar usando matplotlib
        self.titulo = None # Titulo del tablero
        self.posicion = None # Posicion del tablero en la figura
        self.colors = np.empty(self.binario.shape, dtype=object) # Tablero con los colores de cada cuadrado


    def dibujar_tablero(self):
        """Dibujar el tablero en la figura usando matplotlib"""
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
        self.strings = np.full((15, 15, 10), '?', dtype='str')
        self.titulo = "Player 1 Hitboard"
        self.posicion = (1, 2, 2)
    
    def shoot_board(self, coords, vehiculo):
        """Actualiza el hitboard en base si se hundio el vehiculo, hubo o no hubo hit. 
        En caso de que el tablero sea del jugador, pinta los cambios en pantalla"""

        x, y, z = coords

        if vehiculo: # Si hubo hit

            if vehiculo.issunken(): # Si se hundió el vehiculo
                mask = vehiculo.binario != 0 # Posicion del vehiculo
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
            if vehiculo.issunken(): # Se hundio el vehiculo
                #Pintar vehiculo (gris)
                for index in zip(*vehiculo.indices):
                    self.colors[index] = (0, 0, 0, 0.2)
            elif vehiculo: #Hubo hit
                self.color[x][y][z] = (0, 1, 0, 0.5) # Pintar verde
            else: # No hubo hit
                self.color[x][y][z] = (1, 0, 0, 0.2) # Pintar rojo
            funciones.dibujar_hitboard(self)



class PlayerBoard(Tableros):
    def __init__(self, jugador):
        super().__init__(jugador)
        self.titulo = "Player 1 Board"
        self.posicion = (1, 2, 1)
        self.strings = np.full((15, 15, 10), "EMPTY", dtype='str')
        self.vida = 11
    
    


    def draw_vehicle(self, vehiculo):
        """Dibuja el vehiculo en pantalla con su respectivo color"""
        mask = vehiculo.posicion != 0
        self.binario[mask] = True
        self.strings[vehiculo.indices] = vehiculo.objeto
        for index in zip(*vehiculo.indices):
                self.colors[index] = vehiculo.color
        funciones.dibujar_playerboard(self)



    def recibir_tiro(self, coords, vehiculos, hit):
        """Pinta el vehiculo de gris si se hundio, sino pinta la zona del hit de verde."""
        vehiculo = vehiculos[hit]

        if vehiculo.health == 0: # Si se hundio el vehiculo oscurecerlo
            for index in zip(*vehiculo.indices):
                self.colors[index] = (0.2, 0.2, 0.2, 0.2)
        else: # Si no se hundió el vehicul, pintar el lugar del hit como verde
            x, y, z = coords
            self.colors[x][y][z] = (0, 1, 0, 0.8)
        
        funciones.dibujar_playerboard(self)

            

        
        
        

if __name__ == "__main__":
    main()