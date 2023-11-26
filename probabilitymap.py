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
            'Plane': {"count": 0, "size":{"body": (0, 4, 1, 2, 0, 1),
                                          "wings": (2, 3, 0, 3, 0, 1),
                                          "tail": (0, 1, 0, 1, 1, 2)}}
        }
        self.rotations= {
            "Balloon": 1, 
            "Zeppellin": 2,
            "Plane": 4,
            "Elevator": 1}

        self.sunkenpositions = 0

        # Inicializar el mapa de probabilidad
        self.prob_map = np.zeros(self.board_size, dtype=int)
        self.pltfig = None
        self.pltax = None

    def gen_prob_map(self, hitboard):


        # Reiniciar mapa de probabilidades
        self.prob_map = np.zeros(self.board_size, dtype=int)

        # Iterar sobre cada vehiculo en todas las posiciones posibles
        for ship_type, ship_info in self.ships.items(): # Por cada clase de vehiculo
            ship_size = ship_info["size"]
            for count in range(ship_info["count"]):# Por cada vehiculo de la clase
                for rot in range(self.rotations[ship_type]): # Por cada rotacion del vehiculo

                    # Rotado 0 o 180 grados
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
                                        plane_map = self.gen_plane_map()
                                
                                if hitboard[x][y][z] == "HIT":
                                    self.prob_map[x][y][z] = 0
        
        return self.prob_map




    def gen_plane_map(self, position):
        pass


    



    def check_ship_fit(self, ship_type, position, ship_size, hitboard):

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



    def check_sunken_vehicles(self, hitboard):

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

    
        
    
    def visualize_prob_map(self):
        self.pltfig = plt.figure()
        self.pltax = self.pltfig.add_subplot(111, projection='3d')

        # Obtener las coordenadas de los voxels con probabilidad mayor a cero
        x, y, z = np.where(self.prob_map > 0)

        # Obtener los valores de probabilidad para cada voxel
        values = self.prob_map[x, y, z]

        # Crear el gráfico de voxels
        self.pltax.voxels(self.prob_map > 0, facecolors=plt.cm.viridis(values), edgecolor='k')

        self.pltax.set_xlabel('X Label')
        self.pltax.set_ylabel('Y Label')
        self.pltax.set_zlabel('Z Label')
