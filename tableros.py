from typing import Any
import matplotlib.pyplot as plt
import numpy as np


class Tableros():
    def __init__(self):
        pass

    def crear_tablero(fig):
        pass
        


class HitBoard(Tableros):
    def __init__(self):
        super().__init__()

class Playerboard(Tableros):
    def __init__(self):
        super().__init__()



def crear_tableros():
    fig = plt.figure()

    pboard = fig.add_subplot(1, 2, 1, projection="3d")
    pboard.set_xlabel('x')
    pboard.set_ylabel('y')
    pboard.set_zlabel('z')
    pboard.set_title("Player 1 board")

    hboard = fig.add_subplot(1, 2, 2, projection="3d")
    hboard.set_xlabel('x')
    hboard.set_ylabel('y')
    hboard.set_zlabel('z')
    hboard.set_title("Player 1 Hitboard")

    return pboard, hboard



plt.show()