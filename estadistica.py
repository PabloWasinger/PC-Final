import random
def ran():
    return (random.randint(0,14),random.randint(0,14),random.randint(0,9))

def calculo(dic:dict):
    """
    La función realiza un cálculo en un diccionario para obtener coordenadas generadas aleatoriamente.
    Recibe:
    - dic: Un diccionario en donde se almacena la frecuencia de ocurrencia de las coordenadas.
    """
    for i in range (22500):
        coordenadas = ran()
        if coordenadas in dic:
            dic[coordenadas] +=1
        else:
            dic[coordenadas] = 1

dic_estadísticas = {}
calculo(dic_estadísticas)
lista = []
for coordenadas, cant in dic_estadísticas.items():
    lista.append((coordenadas,cant))

lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True)    
with open ("estad5.txt", "w+") as file:
    for i in lista_ordenada:
        file.write(f"{i[0]} : {i[1]}\n")