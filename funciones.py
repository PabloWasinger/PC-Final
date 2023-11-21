import numpy as np
def main():
    pass

def get_coords(clase):
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

def check_hit(molde, coordenadas, lista_vehiculos):
    """
    recibe las coordenadas del disparo,
    si hay un vehiculo retorna el vehiculo,
    si no lo encuentra, retorna False
    """

    if molde [coordenadas[0]] [coordenadas[1]] [coordenadas[2]] == 1: #chequeo si el valor ingresado es True
        for vehiculo in lista_vehiculos:
            if vehiculo [coordenadas[0]] [coordenadas[1]] [coordenadas[2]] == 1:
                return vehiculo
    else:
        return False




def check_collision(molde, vehiculo):
    """
    Chequea si colisiona con un obejto o se va fuera del mapa
    DEvuelve 0 si no hay colisiones
    Devuelve 1 si colisiona con un objeto
    DEvuelve 2 si se va fuera del mapa"""

    suma = np.sum(vehiculo.posicion) #sumo la cantidad de valores True que tiene la matriz
    
    if suma == vehiculo.cuadrados: #comparo la cantidad de valores True que tiene la matriz con la que debería tener
        valor_comun = np.any (molde & vehiculo.posicion) #veo si la matriz tiene algún valor igual que el molde en alguna posicion
        return int(valor_comun) #retorno 0 o 1 
    return 2

def actualizar_pantalla():
    pass


if __name__ == "__main__":
    main()
