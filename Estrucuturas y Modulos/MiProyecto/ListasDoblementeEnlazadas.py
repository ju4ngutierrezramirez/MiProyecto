class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = NodoDoble(valor)

        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.anterior = actual

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente

        print("None")


# Uso
lista = ListaDoble()

lista.agregar("A")
lista.agregar("B")
lista.agregar("C")

lista.mostrar()