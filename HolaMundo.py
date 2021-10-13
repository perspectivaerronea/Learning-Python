import numpy as np
""" 
a = 4
b = 5
c = a + b
print(c)

d = "Hola"
e = "Mundo"
f = d + " " + e
print(f)

g = [6,7,8,-9,1,2,3,4,5]

print(str(g[1]) + " <-- Esto demuestra que en Python los arrays comienzan en 0.")

h = g

h_list = np.array(h)

print(h_list)

print(str(h_list[1]) + " <-- Esto demuestra que los arreglos de numpy también arrancan desde 0.")


print(h)

print("Probando cambiar algo en la notebook")


 """

print("triplets")
g = [6,-7,8,-9,1,2,-3,4,7,-3]
h = np.array(g)
TS = 0
TNS = 0
techo = int(input("Ingrese un número"))
for i in range(0, len(g)-2):
    n1 = h[i]
    for j in range(i+1,len(g) - 1):
        n2 = h[j]
        for k in range(j+1,len(g)):
            n3 = h[k]
            nt = n1+n2+n3
            if (nt <= techo):
               print("El Triplet sirve")
               print(str(n1) + " + " + str(n2) + " + " + str(n3) + " = " + str(nt))
               TS = TS + 1
            else:   
               print("El Triplet no sirve")
               print(str(n1) + " + " + str(n2) + " + " + str(n3) + " = " + str(nt))
               TNS = TNS + 1

print("")
print("Sirven " + str(TS) + " triplets, y los " + str(TNS) + " no sirven.") 


