import matplotlib.pyplot as plt
import numpy as np

def update():
    global globo1
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    globo1[x][y][z] = False
    ax.voxels(globo1, edgecolor='k')
    plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
    plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real


def init():
    global globo1
    ax.voxels(globo1, edgecolor='k')

plt.style.use('_mpl-gallery')

# Prepare some coordinates
x, y, z = np.indices((15, 15, 10))
print(y)

# Draw cuboids in the top left and bottom right corners
globo1 = (x > 3) & (x < 7) & (y < 3) & (z < 3)


# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_zlabel("z label")


plt.ion()


# Inicializar el gráfico
plt.show()

init()
while True:
    update()







