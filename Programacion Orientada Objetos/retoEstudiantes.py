
class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Curso:", self.curso)

    def es_mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")


alumno1 = Estudiante("Lamine", 18, "Python")
alumno1.mostrar_info()
alumno1.es_mayor()