alumnos = {
"Ana": 90,
"Luis": 85,
"Carlos": 95,
"María": 88,
"Sofía": 92
}

with open("calificaciones.txt", "w") as archivo:
    for nombre, calificacion in alumnos.items():
        archivo.write(f"{nombre},{calificacion}\n")
    # Ambos archivos se llaman calificaciones, pero no hay conflicto ya queson de tipo diferente.

estudiantes = {}

with open("calificaciones.txt", "r") as archivo:
    for linea in archivo:
        nombre, calificacion = linea.strip().split(",")

estudiantes[nombre] = int(calificacion)
print(estudiantes)