import matplotlib.pyplot as plt
import numpy as np
import funciones

class Vehiculos():
    issunken = False
    def __init__(self):
        self.posicion = np.zeros((15, 15, 10))

    def position_vehicle(self, offset):

        x, y, z = funciones.get_coords() # Pedir las coordenadas del vehiculo
        self.posicion[(offset[0] + x): (offset[1] + x), (offset[2] + y):(offset[3] + y), (offset[4] + z):(offset[5] + z)] = True # Con el molde del vehiculo(offset) + las coordenadas definir la posicion del vehiculo
    
    def sumar_moldes(self):
        pass




class Globo(Vehiculos):
    def __init__(self):
        super().__init__()
        self.molde = (0, 3, 0, 3, 0, 3)

class Zeppelin(Vehiculos):
    def __init__(self):
        super().__init__()
        self.molde = (0, 5, 0, 2, 0, 2)

class Avion(Vehiculos):
    def __init__(self):
        pass

class Elevador(Vehiculos):
    def __init__(self):
        pass


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

np.set_printoptions(threshold=np.inf)

zepellin1 = Zeppelin()
print("Zeppelin 1: ", end='\0')
zepellin1.position_vehicle(zepellin1.molde)

print(zepellin1.posicion)

globo1 = Globo()
print("Globo 1: ", end='\0')
globo1.position_vehicle(globo1.molde)



vehiculos1 = globo1.posicion + zepellin1.posicion
ax.voxels(vehiculos1)

plt.show()