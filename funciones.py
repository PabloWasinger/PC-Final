def get_coords():
    """Pide y devuelve coordenadas de modo x y z"""
    coords = input()
    check = True

    while check:
        sep = coords.split(" ")
        #Chequear si todos los valores ingresados son enteros
        enteros = True
        try:
            [int(x) for x in sep]
        except:
            enteros = False
        
        if len(sep) != 3 or not enteros: # Si no son todos enteros o no se ingresaron 3 valores
            print("Las coordenadas deben ser enteros de modo (x y z)")
            coords = input("Reingresar coordenadas: ") #Pedir coordenadas devuelta
            continue
        check = False

    return sep

def check_collision():
    pass