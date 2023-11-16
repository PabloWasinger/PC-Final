import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the dimensions of the space
x_dim = 15
y_dim = 15
z_dim = 10

# Generate random data
num_points = 100
x = np.random.rand(num_points) * x_dim
y = np.random.rand(num_points) * y_dim
z = np.random.rand(num_points) * z_dim

# Calculate the volume of each cube (1x1x1)
cube_volume = 1000

# Set the size of each cube using the calculated volume
s = cube_volume * np.ones(num_points)

# Create scatter plot with cubic points


# Set labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Set the limits of the plot
ax.set_xlim(0, x_dim)
ax.set_ylim(0, y_dim)
ax.set_zlim(0, z_dim)

plt.ion()
matriz = np.zeros((15, 15, 10))
matriz[0:3, 0:3, 0:3] = True
ax.voxels(matriz, edgecolor='k')
# Show the plot
plt.show()


adasd = input("puto")

matriz[0:3, 0:3, 0:3] = False
ax.voxels(matriz, edgecolor='k')

asasd = input()
