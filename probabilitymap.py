import numpy as np
import matplotlib.pyplot as plt


class BattleAirComputer:
    def __init__(self):
        # Definir dimensiones del tablero
        self.board_size = (15, 15, 10)

        # Definir dimensiones de los vehículos
        self.ships = {
            'Balloon': {"count": 5, "size":(3, 3, 3)},
            'Zeppelin': {"count": 3, "size":(5, 2, 2)},
            'Elevator': {"count": 1, "size":(1, 1, 10)},
            'Plane': {"count": 3, "size":{"body": (0, 4, 1, 2, 0, 1),
                                          "wings": (2, 3, 0, 3, 0, 1),
                                          "tail": (0, 1, 0, 1, 1, 2)}}
        }
        self.rotations= {
            "Balloon": 1, 
            "Zeppelin": 2,
            "Plane": 1,
            "Elevator": 1}

        self.sunkenpositions = 0

        # Inicializar el mapa de probabilidad
        self.prob_map = np.zeros(self.board_size, dtype=int)
        self.pltfig = None
        self.pltax = None

    def gen_prob_map(self, hitboard)->np.ndarray:
        """
        La función genera un mapa de probabilidades basado en el estado del tablero de disparos.
        Recibe:
        - hitboard: Un objeto que representa el tablero de disparos.
        Retorna:
        - prob_map: El mapa de probabilidades actualizado.

        """


        # Reiniciar mapa de probabilidades
        self.prob_map = np.zeros(self.board_size, dtype=int)

        # Iterar sobre cada vehiculo en todas las posiciones posibles
        for ship_type, ship_info in self.ships.items(): # Por cada clase de vehiculo
            ship_size = ship_info["size"]
            for count in range(ship_info["count"]):# Por cada vehiculo de la clase
                for rot in range(self.rotations[ship_type]): # Por cada rotacion del vehiculo

                    # Rotado 0 o 180 grados
                    if ship_type != "Plane":
                        size0, size1, size2 = ship_size[0], ship_size[1], ship_size[2]
                    # Rotado 90 o 270 grados
                    if rot % 2 == 0:
                        size0, size1 = size1, size0

                    for x in range(self.board_size[0] - size0 + 1):
                        for y in range(self.board_size[1] - size1 + 1):
                            for z in range(self.board_size[2] - size2 + 1):
                                
                                if ship_type != "Plane":

                                    # Verificar si el barco cabe en esta posición, si cabe aumentarle 1 de probabilidad
                                    if self.check_ship_fit(ship_type, (x, y, z), (size0, size1, size2), hitboard):
                                        aumento = np.count_nonzero(hitboard[x:x + ship_size[0], y:y + ship_size[1], z:z + ship_size[2]] == 'HIT') * 3 # Target mode: Si hay algun hit en esa zona aumenta las chances de que haya un vehiculo
                                        self.prob_map[x:x + ship_size[0], y:y + ship_size[1], z:z + ship_size[2]] += 1 + aumento

                                    
                                
                                else:
                                    if self.check_ship_fit(ship_type, (x, y, z), ship_size, hitboard):
                                        plane_map = self.gen_plane_map(ship_size, hitboard, (x, y, z))
                                
                                if hitboard[x][y][z] == "HIT":
                                    self.prob_map[x][y][z] = 0
        
        return self.prob_map




    def gen_plane_map(self, ship_size, hitboard, coords)->None:
        body = ship_size["body"]
        wings = ship_size["wings"]
        tail = ship_size["tail"]

        x, y, z = coords
        aumento = np.count_nonzero(hitboard[x + body[0]:x + body[1], y + body[2]:y + body[3], z + body[4]:z + body[5]] == 'HIT') * 3
        aumento += np.count_nonzero(hitboard[x + wings[0]:x + wings[1], y + wings[2]:y + wings[3], z + wings[4]:z + wings[5]] == "HIT") * 3
        aumento += np.count_nonzero(hitboard[x + tail[0]:x + tail[1], y + tail[2]:y + tail[3], z + tail[4]:z + tail[5]] == "HIT") * 3
        
        self.prob_map[x + body[0]:x + body[1], y + body[2]:y + body[3], z + body[4]:z + body[5]] += 1 + aumento
        self.prob_map[x + wings[0]:x + wings[1], y + wings[2]:y + wings[3], z + wings[4]:z + wings[5]] += 1 + aumento
        self.prob_map[x + tail[0]:x + tail[1], y + tail[2]:y + tail[3], z + tail[4]:z + tail[5]] += 1 + aumento


    



    def check_ship_fit(self, ship_type:str, position:tuple, ship_size, hitboard)->bool:
        """
        La función verifica si el vehículo entra en la posición especificada.
        Recibe:
        - ship_type: El tipo de vehículo.
        - position: Una tupla con las coordenadas.
        - ship_size: La dimensión del vehiculo.
        - hitboard: Un objeto que representa el tablero de disparos.
        Retorna:
        - True si el vehículo entra en la posición, False en lo contrario.
        """

        x, y, z = position

        # Verificar si la posición está ocupada
        if ship_type != "Plane":
            if np.any((hitboard[x:x + ship_size[0], y:y + ship_size[1], z:z + ship_size[2]] != '?') & (hitboard[x:x + ship_size[0], y:y + ship_size[1], z:z + ship_size[2]] != 'HIT')):
                return False
            
        else:
            body = ship_size["body"]
            wings = ship_size["wings"]
            tail = ship_size["tail"]

            check_body = np.any((hitboard[x + body[0]:x + body[1], y + body[2]:y + body[3], z + body[4]:z + body[5]] != '?') & (hitboard[x + body[0]:x + body[1], y + body[2]:y + body[3], z + body[4]:z + body[5]] != 'HIT')) 
            check_wings = np.any((hitboard[x + wings[0]:x + wings[1], y + wings[2]:y + wings[3], z + wings[4]:z + wings[5]] != '?') & (hitboard[x + wings[0]:x + wings[1], y + wings[2]:y + wings[3], z + wings[4]:z + wings[5]] != 'HIT')) 
            check_tail = np.any((hitboard[x + tail[0]:x + tail[1], y + tail[2]:y + tail[3], z + tail[4]:z + tail[5]] != '?') & (hitboard[x + tail[0]:x + tail[1], y + tail[2]:y + tail[3], z + tail[4]:z + tail[5]] != 'HIT')) 
            
            if (check_body + check_wings + check_tail):
                return False

        return True



    def check_sunken_vehicles(self, hitboard)->None:
        """
        La función chequea y verifica si el vehículo esta hundido basándose en el tablero de disparos.
        Recibe:
        - hitboard: Un objeto que representa el tablero de disparos.        
        """

        # Tomar en cuenta diferencia de posiciones de vehiculos hundidos respecto al turno anterior
        before = self.sunkenpositions
        after = np.count_nonzero(hitboard == 'SUNK')
        newsunken = after - before

        # Suponer dependiendo de cuantos nuevas posiciones "SUNK", que vehiculo se hundió, restarle 1
        if newsunken:
            if newsunken == 27:
                vehicle = "Balloon"
            elif newsunken == 20:
                vehicle = "Zeppelin"
            elif newsunken == 7:
                vehicle = "Avion"
            elif newsunken == 10:
                vehicle = "Elevator"

            self.sunkenpositions = after
            self.ships[vehicle]["count"] -= 1

    def get_shooting_coords(self)->None:
        """
        La función obtiene las coordenadas para realizar un disparo basándose en el mapa de probabilidades.
        """
        max_indices = np.where(self.prob_map == np.amax(self.prob_map))
        selected_index = (max_indices[0][0], max_indices[1][0], max_indices[2][0])
        return selected_index
        
    
    def define_plot_map(self)->None:
        """
        La función define un gráfico para visualizar el mapa de probabilidades.
        """
        self.pltfig = plt.figure()
        self.pltax = self.pltfig.add_subplot(111, projection='3d')
        self.pltax.set_title("Mapa de probabilidades")
        self.pltax.set_xlabel('X Label')
        self.pltax.set_ylabel('Y Label')
        self.pltax.set_zlabel('Z Label')

    def refresh_plot_map(self)->None:
        """
        La función refresca y actualiza el mapa de probabilidades.
        """
        # Obtener las coordenadas de los voxels con probabilidad mayor a cero

        # Obtener los valores de probabilidad para cada voxel
        x, y, z = np.meshgrid(np.arange(self.prob_map.shape[0]), np.arange(self.prob_map.shape[1]), np.arange(self.prob_map.shape[2]))
        # Aplanar las matrices para obtener listas de coordenadas
        x = x.flatten()
        y = y.flatten()
        z = z.flatten()

        # Aplanar los datos
        data_flat = self.prob_map.flatten()
        # Crear el gráfico de voxels
        self.pltax.scatter(x, y, z, c=data_flat, cmap='hot_r')

        plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
        plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real

