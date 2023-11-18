import matplotlib.pyplot as plt
import numpy as np
import funciones

def main():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    np.set_printoptions(threshold=np.inf)

    zepellin1 = Zeppelin()
    print("Zeppelin 1: ", end='\0')
    zepellin1.position_vehicle()


    globo1 = Globo()
    print("Globo 1: ", end='\0')
    globo1.position_vehicle()

    avion1 = Avion()
    print("Avion 1: ", end='\0')
    avion1.position_plane()
    avion1.rotar()

    molde = zepellin1.posicion + globo1.posicion + avion1.posicion

    colors = np.empty(molde.shape, dtype=object)

    colors[avion1.indices] = "red"
    print(avion1.indices)
    print(molde.shape)

    # Set colors for zeppelin1 and globo1
    # Set colors for zeppelin1 and globo1
    for index in zip(*zepellin1.indices):
        colors[index] = (1, 0, 0, 0.5)

    for index in zip(*globo1.indices):
        colors[index] = (0, 1, 0, 0.3)
        
    colors[1][1][1] = (1, 0, 0, 1)

    

    # Plot the voxels with different colors
    voxels = ax.voxels(molde, facecolors=colors, edgecolor='k')

    plt.show()




class Vehiculo():
    issunken = False
    def __init__(self):
        self.posicion = np.zeros((15, 15, 10))
        self.indices = 0
        self.molde = 0
        self.clase = None

    def position_vehicle(self):
        offset = self.molde
        check = True
        while check: # While para chequear que no colisione
            x, y, z = funciones.get_coords(self.clase) # Pedir las coordenadas del vehiculo
            self.posicion[(offset[0] + x): (offset[1] + x), (offset[2] + y):(offset[3] + y), (offset[4] + z):(offset[5] + z)] = True # Con el molde del vehiculo(offset) + las coordenadas definir la posicion del vehiculo

            if self.clase == "zeppelin":
                self.rotar()

            check = funciones.check_collision() # Chequear si colisiona, pedir coordenadas devuelta si lo hace
        
        self.indices = np.where(self.posicion) # Variable con los indices de la posicion


    def rotar(self):
        axes = int(input("Cuantos grados deseas rotar el vehiculo? (0, 90, 180 o 270): ")) # Le pedimos al usuario los grados de rotacion
        while axes not in (0, 90, 180, 270):
            axes = input("Error: el numero debe ser (0, 90, 180 o 270)")
        
        rotaciones = axes // 90
        if axes != 0:
            for _ in range(rotaciones): # Rotar 90 grados x veces
                # Transponer coordenadas x e y de la matriz
                self.posicion = np.transpose(self.posicion, axes=(1, 0, 2))
                # Invertir la matriz a lo largo de los ejes especificados
                self.posicion = np.flip(self.posicion, axis=(0,1))
        self.indices = np.where(self.posicion)



class Globo(Vehiculo):
    def __init__(self):
        super().__init__()
        self.clase = "globo"
        self.molde = (0, 3, 0, 3, 0, 3)
        self.color = "blue"

class Zeppelin(Vehiculo):
    def __init__(self):
        super().__init__()
        self.clase = "zeppelin"
        self.molde = (0, 5, 0, 2, 0, 2)
        self.color = 'red'

class Avion(Vehiculo):
    def __init__(self):
        super().__init__()
        self.clase = "avion"
        self.color = 'white'
        self.body = (0, 4, 1, 2, 0, 1) 
        self.wing = (2, 3, 0, 3, 0, 1)
        self.tail = (0, 1, 1, 2, 0, 2)
        self.indices = 0

    def position_plane(self):
        body, wing, tail = self.body, self.wing, self.tail
        check = True
        while check:
            x, y, z = funciones.get_coords()
            # Definimos la forma del avion
            self.posicion[(body[0] + x):(body[1] + x), (body[2] + y):(body[3] + y), (body[4] + z):(body[5] + z)] = True
            self.posicion[(wing[0] + x):(wing[1] + x), (wing[2] + y):(wing[3] + y), (wing[4] + z):(wing[5] + z)] = True
            self.posicion[(tail[0] + x):(tail[1] + x), (tail[2] + y):(tail[3] + y), (tail[4] + z):(tail[5] + z)] = True

            self.rotar()

            check = funciones.check_collision()
        
        self.indices = np.where(self.posicion)
        


class Elevador(Vehiculo):
    def __init__(self):
        super().__init__()
        self.clase = "elevador"
        self.molde(0, 1, 0, 1, 0, 10)
        self.color = "gray"

if __name__ == "__main__":
    main()
