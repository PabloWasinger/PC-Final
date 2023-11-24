import vehiculos
import tableros
import matplotlib.pyplot as plt
import funciones 
import time
import computer
 
def main():
    print("Bienvenido a la batalla aerea!")
    time.sleep(1)
    input("Presiona enter para comenzar: ")


    # Creamos los tableros del jugador
    playerboard_jugador = tableros.PlayerBoard("Player")
    hitboard_jugador = tableros.HitBoard("Player")

    # Creamos tableros de la computadora
    playerboard_computer = tableros.PlayerBoard("Computer")
    hitboard_computer = tableros.HitBoard("Computer")


    # Dibujamos los tableros
    figure = plt.figure()
    x, y, z = playerboard_jugador.posicion
    playerboard_jugador.plotboard = figure.add_subplot(x, y, z, projection="3d")
    playerboard_jugador.dibujar_tablero()
    
    
    x, y, z = hitboard_jugador.posicion
    hitboard_jugador.plotboard = figure.add_subplot(x, y, z, projection="3d")
    hitboard_jugador.dibujar_tablero()

    plt.ion()
    plt.show()

    # Pedimos los vehiculos al jugador
    s = "Posicionamiento de vehículos"
    print(f"{s}\n{'-' * len(s)}")
    time.sleep(1)
    print("Jugador 1, ingrese las coordenadas de los vehiculos:")
    vehiculos_jugador = {}
    funciones.crear_objetos_jugador(vehiculos_jugador, playerboard_jugador)
    print("Vehiculos colocados!")

    # La computadora coloca los vehiculos
    time.sleep(1)
    print("Espera mientras la computadora coloca los vehicuos...")
    time.sleep(2)
    playerboard_computer.strings = computer.get_starting_board()
    playerboard_computer.map_computer_board()
    vehiculos_computadora = computer.get_vehicles()
    print("Empecemos!")
    time.sleep(1)

    # Comienza el juego
    ganador = funciones.reproducir_partida(playerboard_jugador, hitboard_jugador, playerboard_computer, hitboard_computer, vehiculos_jugador, vehiculos_computadora)
    
    # Finaliza el juego
    print("Ha finalizado el juego! ")
    time.sleep(1)
    if ganador == "PLAYER":
        print("Felicitaciones! Has ganado!")

    else:
        print("Que lastima, has perdido :(")
    
    time.sleep(1)
    input("Muchas gracias por jugar! Presiona enter para finalizar el programa: ")






if __name__ == "__main__":
    main()

