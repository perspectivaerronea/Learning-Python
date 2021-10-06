import numpy as np

a = 4
b = 5
c = a + b
print(c)

d = "Hola"
e = "Mundo"
f = d + " " + e
print(f)

g = [6,7,8,19,1,2,3,4,5]

print(str(g[1]) + " <-- Esto demuestra que en Python los arrays comienzan en 0.")

h = g

h_list = np.array(h)

print(h_list)

print(str(h_list[1]) + " <-- Esto demuestra que los arreglos de numpy también arrancan desde 0.")




