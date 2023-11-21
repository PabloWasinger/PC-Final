import numpy as np

# Supongamos que tienes dos arrays 3D, arr1 y arr2, de unos y ceros
arr1 = np.array([[[1, 0, 1], [0, 1, 0], [1, 0, 1]],
                 [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
                 [[1, 0, 1], [0, 1, 0], [1, 0, 1]]])

arr2 = np.array([[[0, 1, 0], [1, 0, 1], [0, 1, 0]],
                 [[1, 0, 1], [0, 1, 0], [1, 0, 1]],
                 [[0, 1, 0], [1, 0, 1], [0, 1, 0]]])

# Verificar si comparten algún valor True
comparten_valores_true = np.any(arr1 & arr2)

if comparten_valores_true:
    print("Los arrays comparten al menos un valor True.")
else:
    print("Los arrays no comparten valores True.")


# Crear una máscara booleana para identificar los valores diferentes de 1 en arr1
mask = arr1 != 1

# Reemplazar los valores diferentes de 1 en arr1 con los valores correspondientes de arr2
arr1[mask] = arr2[mask]

# Mostrar el resultado
print(arr1)