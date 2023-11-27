# WarGames
## Trabajo practico final de Pensamiento Computacional, Universidad de San Andrés
Este codigo reproducirá el juego "Batalla Aerea" en el que se jugará contra la computadora. Cada jugador tiene 2 tableros: "Playerboard" donde se colocarán los vehículos y "Hitboard" donde se verán los disparos realizados. El juego consiste en disparar al tablero del otro jugador pasando coordenadas, tratando de adivinar donde ha posicionado el vehiculo. Aquel que logre hundir todos los vehiculos del enemigo, será el ganador
<img width="1595" alt="Screenshot 2023-11-26 at 21 36 12" src="https://github.com/PabloWasinger/PC-Final/assets/108641186/62af7f40-ef08-44cb-8b7d-3518aebaf79f">

## Setup
- Debes tener instalado Numpy y Matplotlib
- Clonar el repositorio: https://github.com/PabloWasinger/PC-Final.git
- Reproducir **main.py**
- El juego es interactivo a través de la terminal, y será visualizado en una ventana abierta por matplotilib
  
<img width="409" alt="Screenshot 2023-11-26 at 21 31 01" src="https://github.com/PabloWasinger/PC-Final/assets/108641186/685adfe2-cde6-46bc-8610-5997f131b7f9">

## ¿Como está estructurado el código?
- [main.py](main.py): Código principal, donde se definen las variables mas importantes y se llama a las funciones del juego.
- [funciones.py](funciones.py): Están guardadas las funciones principales del juego.
- [tableros.py](tableros.py): Están definidas las clases de los tableros, así como las funciones que los modifican.
- [vehiculos.py](vehiculos.py): Están definidas las clases de los vehiculos, así como las funciones que los modifican.
- [computer.py](computer.py): Funciones requeridas del TP
- [probabilitymap.py](probabilitymap.py): Algoritmo de la computadora para decidir donde disparar, definida como una clase BattleAirMap


## ¿Como está diseñado el algoritmo de la computadora?
Es un algoritmo basado en [esta estrategia](http://www.datagenetics.com/blog/december32011/), desarrollada para el juego "Batalla Naval", por Nick Berry de Datagenetics.
Partiendo de la suposición de que el jugador contrario colocó los vehiculos de manera aleatoria, se creó una función de probabilidad de densidad para encontrar la posición a la cual el tiro tendrá la mayor probabilidad de éxito.
El algoritmo toma en cuenta que hay 4 clases de vehiculo con su respectiva cantidad de instancias:
- 5 Globos
- 2 Zeppelin
- 3 Aviones
- 1 Elevador
Para decidir la probabilidad de que haya un vehiculo en cada posición del tablero, se basa en una superposición de todas las posibles posiciones en la que cada instancia de los vehiculos enemigos se pueden encontrar. Las posiciones seran posibles si no se encuentran obstruidas, ya sea por un tiro errado, un vehiculo hundido o por que parte del vehiculo se va fuera del mapa. Cada vez que se derribe un vehiculo enemigo, este se dejará de tener en cuenta para la simulación.

Por otra parte, una vez que se consigue un "hit", el mapa de probabilidad se actualiza dandole mas peso a aquellas posiciones posibles donde lel lugar del "hit" forma parte del vehiculo, haciendo que sea muy facil hundir un vehiculo una vez encontrado al menos una de sus posiciones.

Los calculos de la computadora serán visibles a través de un "mapa de probabilidades" visualizado con matplotlib, donde las posiciones más probables del vehiculo enemigo tendrán un color más oscuro, mientras que las posiciones menos probables, un color más claro.


### Como se ve el mapa de probabilidades al empezar la partida:
<img width="1710" alt="Screenshot 2023-11-26 at 17 47 13" src="https://github.com/PabloWasinger/PC-Final/assets/108641186/533a4e40-47c2-45a0-97b0-e608a82070b0">
Se puede observar que la probabilidad de que los vehiculos estén en el medio al principio de la partida es mayor, por lo que a medida que el mapa tiende al centro este se oscurece.

### Como se ve el mapa de probabilidades despues de dar con un "hit":
<img width="1710" alt="Screenshot 2023-11-26 at 18 25 59" src="https://github.com/PabloWasinger/PC-Final/assets/108641186/f79391fd-7b41-4d00-9b67-1a31b8fdabf2">
Como se puede ver, una vez encontrado el "hit" las posiciones adyacentes pasan a tener un peso muy importante.
