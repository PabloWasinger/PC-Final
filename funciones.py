import numpy as np
import vehiculos
import matplotlib.pyplot as plt

def main():
    pass

def get_coords(clase=None):
    """Pide y devuelve coordenadas de modo (x y z) o (x y) si es un elevador"""

    while True:
        coords = input()

        splitcoords = coords.split()
        try:
            if clase == "elevador":
                x, y = map(int, splitcoords)
                z = 0
            else:
                x, y, z = map(int, splitcoords)

            break

        except:
            if clase == "elevador":
                print("Las coordenadas deben ser enteros de modo (x y)\nReingresar coordenadas: ", end = '\0')
            else:
                print("Las coordenadas deben ser enteros de modo (x y z)\nReingresar coordenadas: ", end = '\0')
    return x, y, z




def check_hit(hitboard, playerboard, coordenadas):
    """
    recibe las coordenadas del disparo,
    si hay un vehiculo retorna el vehiculo,
    si no lo encuentra, retorna empty
    """
    x, y, z = coordenadas
    if hitboard.binario[x][y][z] == True:
        print("Ya disparaste a esta posicion!")
        return 0
    
    hit_str = playerboard.strings[x][y][z]    

    return hit_str

    


def check_collision(tablero, vehiculo):
    """
    Chequea si colisiona con un obejto o se va fuera del mapa.
    Duevuelve True si colisiona o se va fuera del mapa y devuelve
    False si no colisiona
    
    """
    molde = tablero.binario
    posicion = vehiculo.posicion
    suma = np.sum(posicion) #sumo la cantidad de valores True que tiene la matriz
    if suma == vehiculo.cuadrados: #comparo la cantidad de valores True que tiene la matriz con la que debería tener
        valor_comun = np.any(molde & posicion) #veo si la matriz tiene algún valor igual en el molde y en alguna posicion
        if valor_comun:
            print ("El vehículo colisiona con otro!\nReescribe las coordenadas: ", end='\0')
            vehiculo.posicion = np.zeros((15, 15, 10), dtype=bool) # Reinicia la posicion del vehiculo
            return True
        else:
            return False              
    print ("El vehículo de fue del tablero!\nReescribe las coordenadas: ", end='\0')
    vehiculo.posicion = np.zeros((15, 15, 10), dtype=bool) # Reinicia la posicion del vehiculo
    return True




def crear_objetos_jugador(vehiculos_jugador, playerboard_jugador):
    for i in range(1):
        nombre = f"BALLOON_{i}" # Nombre del objeto
        vehiculos_jugador[nombre] = vehiculos.Globo(nombre) # Crear objeto y agregarlo al diccionario
        print(f"Globo {i} (x y z): ", end = '\0') # Pedir coordenadas
        vehiculos_jugador[nombre].position_vehicle(playerboard_jugador) # Posicionar vehiculo
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre]) # Dibujar vehiculo
        dibujar_playerboard(playerboard_jugador)
        
    for i in range(1):
        nombre = f"PLANE_{i}"
        vehiculos_jugador[nombre] = vehiculos.Avion(nombre)
        print(f"Avion {i} (x y z): ", end = '\0')
        vehiculos_jugador[nombre].position_plane(playerboard_jugador)
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre])
        dibujar_playerboard(playerboard_jugador)
        
    for i in range(1):
        nombre = f"ZEPPELIN_{i}"
        vehiculos_jugador[nombre] = vehiculos.Zeppelin(nombre)
        print(f"Zeppelin {i} (x y z): ", end = '\0')
        vehiculos_jugador[nombre].position_vehicle(playerboard_jugador)
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre])
        dibujar_playerboard(playerboard_jugador)
    
    for i in range(1):
        nombre = f"ELEVATOR"
        vehiculos_jugador[nombre] = vehiculos.Elevador(nombre)
        print(f"Elevador (x y): ", end = '\0')
        vehiculos_jugador[nombre].position_vehicle(playerboard_jugador)
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre])
        dibujar_playerboard(playerboard_jugador)





    

def dibujar_playerboard(playerboard):
    playerboard.plotboard.clear()
    playerboard.dibujar_tablero()
    playerboard.plotboard.voxels(playerboard.binario, facecolors=playerboard.colors, edgecolors='k')
   

    plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
    plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real
    


def dibujar_hitboard(hitboard):
    hitboard.plotboard.clear()
    hitboard.dibujar_tablero()
    hitboard.plotboard.voxels(hitboard.binario, facecolors=hitboard.colors, edgecolors='k')
    plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
    plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real




if __name__ == "__main__":
    main()
