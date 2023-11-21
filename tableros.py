from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import funciones


class Tableros():
    def __init__(self, jugador):
        self.jugador = jugador
        self.tablero = np.zeros((15, 15, 10))
        self.plotboard = None
        self.titulo = None
        self.posicion = None
        self.colors = np.empty(self.tablero.shape, dtype=object)
    def dibujar_tablero(self, figura):
        self.plotboard = figura.add_subplot(self.posicion[0], self.posicion[1], self.posicion[2], projection="3d")
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
        self.titulo = "Player 1 Hitboard"
        self.posicion = (1, 2, 2)
    
    def shoot_board(self, coords, vehiculo):
        """Actualiza el hitboard en base si se hundio el vehiculo, hubo o no hubo hit. 
        En caso de que el tablero sea del jugador, pinta los cambios en pantalla"""
        if vehiculo: # Si hubo hit
            if vehiculo.issunken(): # Si se hundió el vehiculo
                mask = vehiculo.posicion != 0 # Posicion del vehiculo
                self.tablero[mask] = vehiculo[mask] # Asigna todos las posiciones del vehiculo
            
        self.plotboard[coords[0]][coords[1]][coords[2]] = True # Asigna true al lugar del hit

        if vehiculo.jugador == "Player":
            if vehiculo.issunken(): # Se hundio el vehiculo
                #Pintar vehiculo (gris)
                for index in zip(*vehiculo.indices):
                    self.colors[index] = (0, 0, 0, 0.2)
            elif vehiculo: #Hubo hit
                self.color[coords[0]][coords[1][coords[2]]] = (0, 1, 0, 0.5) # Pintar verde
            else: # No hubo hit
                self.color[coords[0]][coords[1][coords[2]]] = (1, 0, 0, 0.2) # Pintar rojo
            funciones.actualizar_pantalla()




class PlayerBoard(Tableros):
    def __init__(self, jugador):
        super().__init__(jugador)
        self.titulo = "Player 1 Board"
        self.posicion = (1, 2, 1)

fig = plt.figure()
hitboard = HitBoard()
playerboard = PlayerBoard()
hitboard.dibujar_tablero(fig)
playerboard.dibujar_tablero(fig)

plt.show()