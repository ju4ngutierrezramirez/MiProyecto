estudiantes = []

def agregar_estudiantes(id, nombre, edad, grupo):
    estudiante = {"id": id,"nombre": nombre,"edad": edad,"grupo": grupo}
    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print(estudiante)

def buscar_estudiante(id):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            return estudiante
    return None

id = int(input("ID del estudiante: "))
resultado = buscar_estudiante(id)
if resultado:
        print("Estudiante encontrado:")
        print(resultado)
else:
    print("Estudiante no encontrado.")


def actualizar_estudiante(id, nuevo_nombre, nueva_edad, nuevo_grupo):
    estudiante = buscar_estudiante(id)
    if estudiante:
        estudiante["nombre"] = nuevo_nombre
        estudiante["edad"] = nueva_edad
        estudiante["grupo"] = nuevo_grupo
        print("Estudiante actualizado correctamente.")
    else:
        print("No se encontró un estudiante con ese ID.")   


def eliminar_estudiante(id):
    estudiante = buscar_estudiante(id)
    if estudiante:
        estudiantes.remove(estudiante)
        print("Estudiante eliminado correctamente.")
    else:
        print("No se encontró un estudiante con ese ID.")



agregar_estudiantes(1, "Ana", 16, "A")
agregar_estudiantes(2, "Luis", 17, "B")
mostrar_estudiantes()

actualizar_estudiante(1, "Ana Martínez", 17, "C")
mostrar_estudiantes()

eliminar_estudiante(2)
mostrar_estudiantes()

while True:
    print("\n--- Sistema escolar ---")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        grupo = input("Grupo: ")
        agregar_estudiantes(id, nombre, edad, grupo)
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        id = int(input("ID del estudiante: "))
        estudiante = buscar_estudiante(id)
        if estudiante:
            print("Estudiante encontrado:")
            print(estudiante)
        else:
            print("Estudiante no encontrado.")
        
    elif opcion == "4":
        id = int(input("ID del estudiante a actualizar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_edad = int(input("Nueva edad: "))
        nuevo_grupo = input("Nuevo grupo: ")
        actualizar_estudiante(id, nuevo_nombre, nueva_edad, nuevo_grupo)
    elif opcion == "5":
        id = int(input("ID del estudiante a eliminar: "))
        eliminar_estudiante(id)
    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")


