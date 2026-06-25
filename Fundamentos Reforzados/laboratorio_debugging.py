#Caso 1 – Error de sintaxis
print("Hola mundo")
#Error es de sintaxis, usaba “” y deberia de haber sido "" y faltaba un ) al debugear ya imprime 

#Caso 2 – Error de tipo de dato
edad = 18
print(edad + 2)
#Error es de tipo de dato, se estaba sumando un numero con un string, al debugear se corrige el error y se imprime el resultado correcto    

#Caso 3 – Variable no definida
nombre="Juan"
print(nombre)  
#Error es de variable no definida, se estaba imprimiendo una variable que no habia sido definida, al debugear se define la variable y se imprime el resultado correcto  

#Caso 4 – Error en función  
def sumar(a, b):
    return a + b
print(sumar(5,10))
#Error al no pasarle los argumentos correctos a la funcion, se realiza la correccion agregando los dos valores y realizando prueba, asignando un print para validar el retorno de la funcion

#Caso 5 – Error lógico
edad = 17
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
#Error lógico, se estaba evaluando la edad de una persona, sino existe else no imprime nada, pero falto el operador logic = ya que tambien si es igual a 18 es mayor de edad, y si se colcoa el se el programa muestra un resultado mas completo si es menor o mayor