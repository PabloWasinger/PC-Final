class MiClase:
    def __init__(self, valor_inicial):
        self.atributo_instancia = valor_inicial

    def definir_atributo_clase(self, nuevo_valor):
        self.atributo_clase = nuevo_valor

# Crear instancias de la clase
objeto1 = MiClase(10)
objeto2 = MiClase(20)

# Imprimir el atributo de instancia para cada objeto
print(objeto1.atributo_instancia)  # Salida: 10
print(objeto2.atributo_instancia)  # Salida: 20

# Intentar acceder al atributo de clase antes de definirlo
# Esto generará un error, ya que el atributo aún no ha sido definido.
# print(MiClase.atributo_clase)  # Generará un error

# Llamar al método para definir el atributo de clase
objeto1.definir_atributo_clase(100)

# Ahora se puede acceder al atributo de clase desde la clase o cualquier instancia
print(MiClase.atributo_clase)    # Salida: 100
print(objeto2.atributo_clase)     # Salida: 100
