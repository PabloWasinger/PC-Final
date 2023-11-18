
def main():
    pass

def get_coords():
    """Pide y devuelve coordenadas de modo x y z"""

    while True:
        coords = input()

        splitcoords = coords.split()
        try:
            x, y, z = map(int, splitcoords)

            break

        except:
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
