
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

def check_collision():
    """Chequea si colisiona con un obejto o se va fuera del mapa
    DEvuelve 0 si no hay colisiones
    Devuelve 1 si colisiona con un objeto
    DEvuelve 2 si se va fuera del mapa"""
    
    #primero para ver si los coordinaciones estan en la mapa

    if not (0 <= x < board.shape[0] and 0 <= y < board.shape[1] and 0 <= z < board.shape[2]):
        return 2

    #necesito ver si hay un occupied cell, no se el codigo para esto

    if _:
        return 1

    else:
        return 0



if __name__ == "__main__":
    main()
