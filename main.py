import vehiculos
import tableros
import matplotlib.pyplot as plt
import funciones 
 
def main():
    playerboard_jugador = tableros.PlayerBoard("Player")
    hitboard_jugador = tableros.HitBoard("Player")

    playerboard_computer = tableros.PlayerBoard("Computer")
    hitboard_computer = tableros.HitBoard("Computer")
    plt.ion()
    plt.show()


    playerboard_jugador.colors[0][0][0] = "green"
    figure = plt.figure()
    x, y, z = playerboard_jugador.posicion
    playerboard_jugador.plotboard = figure.add_subplot(x, y, z, projection="3d")
    playerboard_jugador.dibujar_tablero()
    
    
    x, y, z = hitboard_jugador.posicion
    hitboard_jugador.plotboard = figure.add_subplot(x, y, z, projection="3d")
    hitboard_jugador.dibujar_tablero()


    vehiculos_jugador = {}
    funciones.crear_objetos_jugador(vehiculos_jugador, playerboard_jugador)
    
    
    ashei = input("FInalizar prueba: ")




if __name__ == "__main__":
    main()

