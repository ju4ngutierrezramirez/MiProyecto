
class Estructuras:
    def __init__(self, lista, diccionario, set):
        self.lista = lista
        self.diccionario = diccionario
        self.set = set


est = Estructuras([4, 2, 3], {'l': 1, 'b': 2, 'c':'v'}, {2, 1, 3})
print(f"Lista: {est.lista}") # Salida: [4, 2, 3]
print(f"Diccionario: {est.diccionario}") # Salida: {'l': 1, 'b': 2, 'c': 'v'}
print(f"Set: {est.set}") # Salida: {2, 1, 3}
# Los conjuntos se definen al crear el objeto en este ejemplo
# Todas se usan para almacenra múltiples datos/valores
# Todas empiezan en índice [0]