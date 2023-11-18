
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
    
    pass


if __name__ == "__main__":
    main()
