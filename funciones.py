import numpy as np
import vehiculos
import matplotlib.pyplot as plt
import computer
import probabilitymap
from typing import Optional

def main():
    pass

def get_coords(clase:Optional[str]=None) -> tuple:
    """
    La funcion solicita al usuario las coordenadas en formato (x,y,z).

    Recibe:
    - Define las coordenadas esperadas. Si es un elevador, se esperan dos coordenadas (x,y),
    de lo contrario, se esperan tres (x,y,z).

    Retorna:
    - Una tupla con las coordenadas ingresadas convertidas a enteros.
    
    """
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




def check_hit(coordenadas, hitboard, playerboard_strings):
    """
    Verifica si se ha disparado previamente a las coordenadas especificadas en el tablero de disparos.

    Recibe:
    - coordenadas: Una tupla que contiene las coordenadas (x, y, z) a verificar.
    - hitboard: Un objeto que representa el tablero de disparos, con informacion sobre posiciones ya disparadas.
    - playerboard: Un objeto que representa el tablero del jugador, con informacion sobre las posiciones de los vehiculos.

    Retorna:
    - hit_str: Devuelve la cadena de la posicion en el tablero del jugador correspondiente a las coordenadas.
    Si la posicion ya ha sido disparada, imprime un mensaje y devuelve 0.
    """
    x, y, z = coordenadas
    if hitboard.binario[x][y][z] == True:
        print("Ya disparaste a esta posicion!")
        return None
    
    hit_str = playerboard_strings[x][y][z]    

    return hit_str

    


def check_collision(tablero, vehiculo):
    """
    Verifica si los vehiculos colisionan y/o se van del mapa.
    Recibe:
    - tablero: Un objeto que representa el tablero en el cual se guarda la informacion de la posicion de los vehiculos.
    - vehiculo: Un objeto que representa el vehículo.
    Retorna:
    - bool: Duevuelve True si colisiona o se va fuera del mapa y devuelve y False si no colisiona
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
    """
    La función crea y posiciona los vehiculos en el tablero.
    Recibe:
    - vehiculos_jugador: Un diccionario donde se guardan los vehículos del jugador.
    - playerboard_jugador: Un objeto que representa el tablero del jugador.
    """
    for i in range(5):
        nombre = f"BALLOON_{i}" # Nombre del objeto
        vehiculos_jugador[nombre] = vehiculos.Globo(nombre) # Crear objeto y agregarlo al diccionario
        print(f"- Globo {i} (x y z): ", end = '\0') # Pedir coordenadas
        vehiculos_jugador[nombre].position_vehicle(playerboard_jugador) # Posicionar vehiculo
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre]) # Dibujar vehiculo
        dibujar_playerboard(playerboard_jugador)


    for i in range(2):
        nombre = f"ZEPPELIN_{i}"
        vehiculos_jugador[nombre] = vehiculos.Zeppelin(nombre)
        print(f"- Zeppelin {i} (x y z): ", end = '\0')
        vehiculos_jugador[nombre].position_vehicle(playerboard_jugador)
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre])
        dibujar_playerboard(playerboard_jugador)
        
    for i in range(3):
        nombre = f"PLANE_{i}"
        vehiculos_jugador[nombre] = vehiculos.Avion(nombre)
        print(f"- Avion {i} (x y z): ", end = '\0')
        vehiculos_jugador[nombre].position_plane(playerboard_jugador)
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre])
        dibujar_playerboard(playerboard_jugador)
        
    
    for i in range(1):
        nombre = f"ELEVATOR"
        vehiculos_jugador[nombre] = vehiculos.Elevador(nombre)
        print(f"- Elevador (x y): ", end = '\0')
        vehiculos_jugador[nombre].position_vehicle(playerboard_jugador)
        playerboard_jugador.draw_vehicle(vehiculos_jugador[nombre])
        dibujar_playerboard(playerboard_jugador)






    

def dibujar_playerboard(playerboard):
    """
    Actualiza y visualiza el tablero.
    Recibe:
    - playerboard: Un objeto que representa el tablero del jugador.
    """
    playerboard.plotboard.clear()
    playerboard.dibujar_tablero()
    playerboard.plotboard.voxels(playerboard.binario, facecolors=playerboard.colors, edgecolors='k')
   

    plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
    plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real
    


def dibujar_hitboard(hitboard):
    """
    Actualiza y visualiza el tablero de disparos.
    Recibe:
    - hitboard: Un objeto que representa el tablero de disparos.
    """
    hitboard.plotboard.clear()
    hitboard.dibujar_tablero()
    hitboard.plotboard.voxels(hitboard.binario, facecolors=hitboard.colors, edgecolors='k')
    plt.gcf().canvas.draw_idle()  # Indica a Matplotlib que la figura debe ser actualizada
    plt.pause(0.1)  # Pausa para permitir la actualización en tiempo real



def reproducir_partida(playerboard_jugador, hitboard_jugador, playerboard_computer, hitboard_computer, vehiculos_jugador, vehiculos_computadora):
    """
    Es la función que permite el desarrollo de la partida.
    Recibe:
    - playerboard_jugador: Un objeto que representa el tablero del jugador.
    - hitboard_jugador: Un objeto que representa el tablero de disparos del jugador.
    - playeroboard_computer: Un objeto que representa el tablero de la computadora.
    - hitboard_computer: Un objeto que representa el tablero de disparos de la computadora.
    - vehiculos_jugador: Un diccionario donde se guardan los vehículos del jugador.
    - vehiculos_computadora: Un diccionario donde se guardan los vehículos de la computadora.
    Retorna:
    - str: Retorna "PLAYER" si gana el jugador, y "COMPUTER" si gana la computadora.

    """
    probabilidad = probabilitymap.BattleAirComputer()
    turno = 0
    j = "Disparo Jugador 1"
    c = "Disparo Computadora"
    while True:

        # Turno del jugador
        if turno % 2 == 0:
            print(f"{j}\n{'-' * len(j)}")
            print("Coordenadas (x y z): ", end='\0')
            coords = get_coords()
            disparo = check_hit(coords, hitboard_jugador, playerboard_computer.strings)
            if not disparo:
                pass

            elif disparo == "EMPTY":
                print("Resultado: Errado")
                hitboard_jugador.shoot_board(coords, None) # Actualizo el hitboard
            
            else:
                vehiculo = vehiculos_computadora[disparo] #Conseguir el vehiculo del diccionario
                vehiculo.health -= 1 # Restarle 1 de vida
                hitboard_jugador.shoot_board(coords, vehiculo) # Actualizar hitboard

                if vehiculo.health == 0: # Si se hundió el veihculo
                    print("Resultado: Hundido")
                    playerboard_computer.vida -= 1 # Restar un vehiculo a la computadora

                    if playerboard_computer.vida == 0: # Si se quedó sin vehiculos devuelve el ganador
                        return "PLAYER"
                else:
                    print("Resultado: Tocado")
            

        # Turno de la computadora
        else:
            print(f"{j}\n{'-' * len(j)}")
            coords = computer.next_turn(hitboard_computer.strings)
            print(f"Coordenadas: {coords[0]} {coords[1]} {coords[2]}")
            disparo = check_hit(coords, hitboard_computer, playerboard_jugador.strings)

            if not disparo or disparo == "EMPTY":
                print("Resultado: Errado")
                hitboard_computer.shoot_board(coords, None)
            
            else:
                vehiculo = vehiculos_jugador[disparo]
                vehiculo.health -= 1
                hitboard_computer.shoot_board(coords, vehiculo)
                playerboard_jugador.recibir_tiro(coords, vehiculo)

                if vehiculo.health == 0:
                    print("Resultado: Hundido")
                    playerboard_jugador.vida -= 1

                    if playerboard_jugador.vida == 0:
                        return "COMPUTER"
                    
                else:
                    print("Resultado: Tocado")
        turno += 1



if __name__ == "__main__":
    main()
