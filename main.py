import vehiculos
import tableros
import matplotlib.pyplot as plt
import funciones 
import time
 
def main():
    print("Bienvenido a la batalla aerea!")
    time.sleep(2)
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
    print(f"{s}\n")
    vehiculos_jugador = {}
    funciones.crear_objetos_jugador(vehiculos_jugador, playerboard_jugador)
    
    
    ashei = input("FInalizar prueba: ")




if __name__ == "__main__":
    main()

