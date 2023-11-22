import matplotlib.pyplot as plt
import numpy as np
import funciones
import tableros

def main():
    pass




class Vehiculo():
    issunken = False
    def __init__(self, objeto):
        self.posicion = np.zeros((15, 15, 10), dtype=bool)
        self.indices = 0
        self.molde = 0
        self.clase = None
        self.objeto = objeto
        self.cuadrados = 0
        self.health = 0

    def position_vehicle(self, tablero):
        offset = self.molde
        check = True
        while check: # While para chequear que no colisione
            x, y, z = funciones.get_coords(self.clase) # Pedir las coordenadas del vehiculo
            self.posicion[(offset[0] + x): (offset[1] + x), (offset[2] + y):(offset[3] + y), (offset[4] + z):(offset[5] + z)] = True # Con el molde del vehiculo(offset) + las coordenadas definir la posicion del vehiculo
        
            if self.clase == "zeppelin":
                self.rotar()
                
            check = funciones.check_collision(tablero, self) # Chequear si colisiona, pedir coordenadas devuelta si lo hace
            
        self.indices = np.where(self.posicion) # Variable con los indices de la posicion


    def rotar(self):
        check = True
        while check:
            axes = input("Cuantos grados deseas rotar el vehiculo? (0, 90, 180 o 270): ") # Le pedimos al usuario los grados de rotacion
            try:
                axes = int(axes)
                if axes not in (0, 90, 180, 270):
                    print("Error: el numero debe ser (0, 90, 180 o 270)")
                    continue
            except:
                print("Error: el numero debe ser (0, 90, 180 o 270)")
                continue
        
            if axes != 0:
                original_indices = np.where(self.posicion.copy())  # Hacemos una copia de la posición original

                # Rotar según la cantidad de grados especificada
                if axes == 90:
                    self.posicion = np.transpose(self.posicion, axes=(1, 0, 2))
                    self.posicion = np.flip(self.posicion, axis=(0, 1))
                elif axes == 180:
                    self.posicion = np.transpose(self.posicion, axes=(1, 0, 2))
                    self.posicion = np.flip(self.posicion, axis=(0, 1))
                    self.posicion = np.transpose(self.posicion, axes=(1, 0, 2))
                elif axes == 270:
                    self.posicion = np.transpose(self.posicion, axes=(1, 0, 2))


                # Obtiene las coordenadas de los elementos no nulos después de todas las rotaciones
                rotated_indices = np.where(self.posicion)
                
                try:
                    # Calcula el desplazamiento necesario para mantener la posición
                    shift_values = (
                        original_indices[0][0] - rotated_indices[0][0],
                        original_indices[1][0] - rotated_indices[1][0],
                        original_indices[2][0] - rotated_indices[2][0]
                    )

                except:
                    print("Error: el vehiculo debe estar dentro del mapa")
                    check = True
                    continue
                # Ajusta la posición para compensar el cambio debido a la rotación
                self.posicion = np.roll(self.posicion, shift=shift_values, axis=(0, 1, 2))
            check = False
            

        self.indices = np.where(self.posicion)
    



class Globo(Vehiculo):
    def __init__(self, objeto):
        super().__init__(objeto)
        self.clase = "globo"
        self.molde = (0, 3, 0, 3, 0, 3)
        self.color = (0.2, 0.4, 0.7 ,0.8)
        self.cuadrados = 27
        self.health = 1

class Zeppelin(Vehiculo):
    def __init__(self, objeto):
        super().__init__(objeto)
        self.clase = "zeppelin"
        self.molde = (0, 5, 0, 2, 0, 2)
        self.color = (1, 0.4, 0.4 ,0.8)
        self.cuadrados = 20
        self.health = 3


class Avion(Vehiculo):
    def __init__(self, objeto):
        super().__init__(objeto)
        self.clase = "avion"
        self.color = (0.8, 0.8, 0.8, 0.8)
        self.body = (0, 4, 1, 2, 0, 1) 
        self.wing = (2, 3, 0, 3, 0, 1)
        self.tail = (0, 1, 1, 2, 0, 2)
        self.cuadrados = 7
        self.health = 2

    def position_plane(self, tablero):
        body, wing, tail = self.body, self.wing, self.tail
        check = True
        while check:
            x, y, z = funciones.get_coords(self.clase)
            # Definimos la forma del avion
            self.posicion[(body[0] + x):(body[1] + x), (body[2] + y):(body[3] + y), (body[4] + z):(body[5] + z)] = True
            self.posicion[(wing[0] + x):(wing[1] + x), (wing[2] + y):(wing[3] + y), (wing[4] + z):(wing[5] + z)] = True
            self.posicion[(tail[0] + x):(tail[1] + x), (tail[2] + y):(tail[3] + y), (tail[4] + z):(tail[5] + z)] = True

            self.rotar()
            check = funciones.check_collision(tablero, self)
        
        self.indices = np.where(self.posicion)
        


class Elevador(Vehiculo):
    def __init__(self, objeto):
        super().__init__(objeto)
        self.clase = "elevador"
        self.molde = (0, 1, 0, 1, 0, 10)
        self.color = (0.2, 0.2, 0.2, 0.8)
        self.cuadrados = 10
        self.health = 4




if __name__ == "__main__":
    main()
