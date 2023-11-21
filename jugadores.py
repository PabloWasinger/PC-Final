import matplotlib.pyplot as plt
import numpy as np
import funciones
import tableros


class Jugador():
    def __init__(self,):
        self.tipo = ""
        self.cant_vehiculos = 11


class Computadora(Jugador):
    def __init__(self):
        super().__init__()
        self.tipo = "Computer"


class Player(Jugador):
    def __init__(self):
        super().__init__()
        self.tipo = "Player"

