import json
disfraces = [
     {
    "id": 1,
    "nombre": "Spider-Man",
    "categoria": "Superhéroe",
    "talla": "M",
    "edad_recomendada": "8-10",
    "precio": 550,
    "stock": 5,
    "proveedor": "Proveedor X",
    "temporada": "Halloween",
    "costo_compra": 300
    },   
    {
        "id": 2,
        "nombre": "Batman",
        "categoria": "Superhéroe",
        "talla": "L",
        "edad_recomendada": "10-12",
        "precio": 600,
        "stock": 3,
        "proveedor": "Proveedor Gótica",
        "temporada": "Halloween",
        "costo_compra": 340
    },
    {
        "id": 3,
        "nombre": "Elsa",
        "categoria": "Princesa",
        "talla": "S",
        "edad_recomendada": "4-6",
        "precio": 480,
        "stock": 8,
        "proveedor": "Fantasy Kids",
        "temporada": "Todo el año",
        "costo_compra": 250
    },
    {
        "id": 4,
        "nombre": "Darth Vader",
        "categoria": "Ciencia Ficción",
        "talla": "XL",
        "edad_recomendada": "12+",
        "precio": 850,
        "stock": 2,
        "proveedor": "Galaxy Store",
        "temporada": "Halloween",
        "costo_compra": 500
    },
    {
        "id": 5,
        "nombre": "Pirata del Caribe",
        "categoria": "Pirata",
        "talla": "M",
        "edad_recomendada": "8-12",
        "precio": 520,
        "stock": 6,
        "proveedor": "Aventura Disfraces",
        "temporada": "Fiestas Escolares",
        "costo_compra": 290
    },
    {
        "id": 6,
        "nombre": "Bruja Clásica",
        "categoria": "Terror",
        "talla": "M",
        "edad_recomendada": "7-10",
        "precio": 450,
        "stock": 10,
        "proveedor": "Magic Costumes",
        "temporada": "Halloween",
        "costo_compra": 230
    }]

def crear_disfraz(id, nombre, categoria, talla, edad_recomendada, precio, stock, proveedor, temporada, costo_compra):
    resultado = buscar_disfraz_por_id(id)
    if resultado:
        print("Ya existe un disfraz con ese ID.")
        print("ID:", resultado["id"])
        print("Nombre:", resultado["nombre"])
    else:
        disfraz = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "talla": talla,
        "edad_recomendada": edad_recomendada,
        "precio": precio,
        "stock": stock,
        "proveedor": proveedor,
        "temporada": temporada,
        "costo_compra": costo_compra
    }
        disfraces.append(disfraz)  
        print("Disfraz agregado al inventario.")
             

def buscar_disfraz_por_id(id):
    for disfraz in disfraces:
        if disfraz["id"] == id:
            return disfraz
    return None

def mostrar_disfraz(disfraz):
    print("ID:", disfraz["id"])
    print("Nombre:", disfraz["nombre"])
    print("Categoría:", disfraz["categoria"])
    print("Talla:", disfraz["talla"])
    print("Edad recomendada:", disfraz["edad_recomendada"])
    print("Precio:", disfraz["precio"])
    print("Stock:", disfraz["stock"])
    print("Proveedor:", disfraz["proveedor"])
    print("Temporada:", disfraz["temporada"])
    print("Costo de compra:", disfraz["costo_compra"])
    print("-" * 30)

def mostrar_disfraces():
    if len(disfraces) == 0:
        print("No hay disfraces registrados.")
    else:
        for disfraz in disfraces:
            mostrar_disfraz(disfraz)

def actualizar_disfraz(id, campo, nuevo_valor):
    disfraz = buscar_disfraz_por_id(id)
    if disfraz:
        disfraz[campo] = nuevo_valor
        print("Disfraz actualizado correctamente." )
    else:
        print("No se encontró un disfraz con ese ID.")

def reabastecer_disfraz(id):
    disfraz = buscar_disfraz_por_id(id)
    if disfraz:
        cantidad = int(input("Cantidad a reabastecer: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        disfraz["stock"] += cantidad
        print("Disfraz reabastecido correctamente.")
    else:
        print("No se encontró un disfraz con ese ID.")

def eliminar_disfraz(id):
    disfraz = buscar_disfraz_por_id(id)
    if disfraz:
        disfraces.remove(disfraz)
        print("Disfraz eliminado del inventario.")
    else:
        print("No se encontró un disfraz con ese ID.")

def mostrar_bajo_stock():
    bajo_stock = []
    for disfraz in disfraces:
        if disfraz["stock"] < 5:
            bajo_stock.append(disfraz)
    if bajo_stock:
        print("Disfraces con bajo stock:")
        for disfraz in bajo_stock:
            mostrar_disfraz(disfraz)
    else:
        print("No hay disfraces con bajo stock.")

def guardar_inventario():
    with open("inventario.json", "w", encoding="utf-8") as f:
        json.dump(disfraces, f)
    print("Inventario guardado.")

def cargar_inventario():
    global disfraces
    try:
        with open("inventario.json", "r") as f:
            disfraces = json.load(f)
        print("Inventario cargado.")
    except FileNotFoundError:
        print("No se encontró el archivo de inventario.")

cargar_inventario() 
while True:
    print("\n--- Sistema Inventario Disfraces ---")
    print("1. Agregar disfraces")
    print("2. Mostrar disfraces")
    print("3. Buscar disfraces")
    print("4. Actualizar disfraces")
    print("5. Reabastecer disfraces")
    print("6. Eliminar disfraces")
    print("7. Mostrar bajo stock de disfraces")
    print("8. Guardar inventario de disfraces")
    print("9. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        talla = input("Talla: ")
        edad_recomendada = input("Edad recomendada: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        proveedor = input("Proveedor: ")
        temporada = input("Temporada: ")
        costo_compra = float(input("Costo de compra: "))
        crear_disfraz(id, nombre, categoria, talla, edad_recomendada, precio, stock, proveedor, temporada, costo_compra)
    elif opcion == "2":
        mostrar_disfraces()
    elif opcion == "3":
        id = int(input("ID del disfraz: "))
        disfraz = buscar_disfraz_por_id(id)
        if disfraz:
            print("Disfraz encontrado:") 
            mostrar_disfraz(disfraz)
        else:
            print("Disfraz no encontrado.")
    elif opcion == "4":
        id = int(input("ID del disfraz a actualizar: "))
        disfraz = buscar_disfraz_por_id(id)
        if disfraz:
            print("Disfraz encontrado:") 
            while True:
                print("1. Actualizar nombre")
                print("2. Actualizar categoría")
                print("3. Actualizar talla")
                print("4. Actualizar edad recomendada")
                print("5. Actualizar precio")
                print("6. Actualizar stock")
                print("7. Actualizar proveedor")
                print("8. Actualizar temporada")
                print("9. Actualizar costo de compra")
                print("10. Salir de actualización")
                opcion_actualizacion = input("Selecciona una opción de actualización: ")
                
                if opcion_actualizacion == "1":
                    nuevo_valor = input("Nuevo nombre: ")
                    actualizar_disfraz(id, "nombre", nuevo_valor)
                    
                elif opcion_actualizacion == "2":
                    nuevo_valor = input("Nueva categoría: ")
                    actualizar_disfraz(id, "categoria", nuevo_valor)
                
                elif opcion_actualizacion == "3":
                    nuevo_valor = input("Nueva talla: ")
                    actualizar_disfraz(id, "talla", nuevo_valor)
                elif opcion_actualizacion == "4":
                    nuevo_valor = input("Nueva edad recomendada: ")
                    actualizar_disfraz(id, "edad_recomendada", nuevo_valor)
                elif opcion_actualizacion == "5":
                    nuevo_valor = float(input("Nuevo precio: "))
                    actualizar_disfraz(id, "precio", nuevo_valor)
            
                elif opcion_actualizacion == "6":
                    nuevo_valor = int(input("Nuevo stock: "))
                    actualizar_disfraz(id, "stock", nuevo_valor)
                
                elif opcion_actualizacion == "7":
                    nuevo_valor = input("Nuevo proveedor: ")
                    actualizar_disfraz(id, "proveedor", nuevo_valor)
                   
                elif opcion_actualizacion == "8":
                    nuevo_valor = input("Nueva temporada: ")
                    actualizar_disfraz(id, "temporada", nuevo_valor)
                  
                elif opcion_actualizacion == "9":
                    nuevo_valor = float(input("Nuevo costo de compra: "))
                    actualizar_disfraz(id, "costo_compra", nuevo_valor)
                  
                elif opcion_actualizacion == "10":
                    break
        else:
            print("Disfraz no encontrado.")
    elif opcion == "5":
        id = int(input("ID del disfraz a reabastecer: "))
        reabastecer_disfraz(id)
    elif opcion == "6":
        id = int(input("ID del disfraz a eliminar: "))
        eliminar_disfraz(id)
    elif opcion == "7":
        mostrar_bajo_stock()
    elif opcion == "8":
        guardar_inventario()
    elif opcion == "9":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")
