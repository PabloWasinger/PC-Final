import matplotlib.pyplot as plt
import numpy as np

def create_airplane_mask(x_offset, y_offset, z_offset):
    x, y, z = np.indices((15, 15, 10))
    # Definir condiciones para el avión
    body_condition = ((x >= 0 + x_offset) & (x < 4 + x_offset) & 
                     (y >= 1 + y_offset) & (y < 2 + y_offset) & 
                     (z >= 0 + z_offset) & (z < 1 + z_offset))
    wing_condition = ((x >= 2 + x_offset) & (x < 3 + x_offset) & 
                     (y >= 0 + y_offset) & (y < 3 + y_offset) & 
                     (z >= 0 + z_offset) & (z < 1 + z_offset))
    tail_condition = ((x >= 0 + x_offset) & (x < 1 + x_offset) & 
                     (y >= 1 + y_offset) & (y < 2 + y_offset) & 
                     (z >= 0 + z_offset) & (z < 2 + z_offset))

    # Combinar condiciones para obtener la forma completa del avión
    airplane_mask = wing_condition | body_condition | tail_condition

    return airplane_mask

def update():
    global airplane_mask
    x_offset = int(input("x_offset: "))
    y_offset = int(input("y_offset: "))
    z_offset = int(input("z_offset: "))
    airplane_mask = create_airplane_mask(x_offset, y_offset, z_offset)
    ax.clear()
    ax.voxels(airplane_mask, edgecolor='k')
    plt.gcf().canvas.draw_idle()
    plt.pause(0.1)

def init():
    global airplane_mask
    ax.voxels(airplane_mask, edgecolor='k')

plt.style.use('_mpl-gallery')

# Tamaño de la cuadrícula tridimensional
# Posición inicial del avión
initial_x_offset = 0
initial_y_offset = 0
initial_z_offset = 0

# Crear máscara para el avión
airplane_mask = create_airplane_mask(initial_x_offset, initial_y_offset, initial_z_offset)

# Crear figura y eje tridimensional
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_zlabel("z label")







# Modo interactivo
plt.ion()

np.set_printoptions(threshold=np.inf)
# Inicializar el gráfico
plt.show()
init()

# Actualizar el gráfico de manera interactiva
while True:
    update()
