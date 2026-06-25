class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

auto_nuevo = Auto("Nissan", "Skyline", 2025)
auto_nuevo.mostrar_informacion()
otro_auto = Auto("Toyota", "Corolla", 2020)
otro_auto.mostrar_informacion()