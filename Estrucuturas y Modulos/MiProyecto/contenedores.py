from collections import deque

fila = deque()
# Agregar elementos
fila.append("A")
fila.append("B")
fila.append("C")
print(fila) # deque(['A','B','C'])
# Sacar el primer elemento
primero = fila.popleft()
print(primero) # A
print(fila) # deque(['B','C'])