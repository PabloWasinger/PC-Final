import matplotlib.pyplot as plt
import numpy as np

def update():
    global globo1
    ax.voxels(globo1, edgecolor='k', facecolor='k', alpha=0.1)
    plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
    plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real


def init():
    global globo1
    global globo2
    ax.voxels(globo1, edgecolor='k', alpha=1)
    ax.voxels(globo2, edgecolor='k', alpha=0.6)

plt.style.use('_mpl-gallery')

# Prepare some coordinates
x, y, z = np.indices((15, 15, 10))
print(y)

# Draw cuboids in the top left and bottom right corners
globo1 = (x > 3) & (x < 7) & (y < 3) & (z < 3)
globo2 = (x > 7) & (x < 11) & (y < 3) & (z < 3)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_zlabel("z label")


plt.ion()


# Inicializar el gráfico
plt.show()

init()
dads = input("check: ")
if dads == True:
    update()
wesa = input("checasdaskd: ")






