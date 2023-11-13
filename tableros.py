import matplotlib.pyplot as plt
import numpy as np


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

    pboard.voxels(globo1)

    

crear_tableros()

x, y, z = np.indices((15, 15, 10))

# Draw cuboids in the top left and bottom right corners
globo1 = (x > 3) & (x < 7) & (y < 3) & (z < 3)




plt.show()