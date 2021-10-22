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



myString = "Hola Mundo"

# print(myString[desde:hasta:paso]) <- Entonces si lo dejo en blanco y completo el paso toma desde el inicio, hasta el final, y si el paso es negativo lo hace desde el final
# si lo hace en positivo va saltando la cantidad especificada. Y dependiendo el inicio/fin que se ponga permite hacer subselecciones del string
print(myString[0])
print(myString[-2])
print(myString[3:])
print(myString[:3])
print(myString[3:6])
print(myString[::3])
print(myString[::-1])

print("tinker"[1:4])

 """ 

lista = [3,1,-5,123,-23]

print(lista)
print(len(lista))

lista.sort()
lista.append(1233)
print(lista)
print(lista.pop())
print(lista.pop(1))
print(lista)
print(lista[1:])
print(lista[::2])

 
#Tambien vi dictionary a= {'a':1,'b':[4,'d',-5]}

a= {'a':1,'b':[4,'d',-5]}
print(a)
print(a['b'])
print(a['b'][2])
a['b'][2] = 'CAMBIADO'
print(a['b'][2])
#Y ví tuplets

b = (1,3,4,5)
print(b)
print(b[3])
# b[3] = 'c' <-- los tuplets son invariables

#SETS
#solo acepta valores únicos

miset = set()
miset.add(1)
print(miset)
miset.add(2)
print(miset)
miset.add(2)
print(miset)

lista_set = [1,1,2,3,4,4,3,3,2,2,6,6]

miset = set(lista_set)
print(miset)
miset = set('Mississippi')
print(miset)

#archivos

myfile = open('myfile.txt')
# myfile = open('myfile2.txt') <-- arroja ErrNo 2 <- no existe ese archivo

print(myfile.read())
print("--")
print(myfile.read())
myfile.seek(0)
print(myfile.read())
print("--")
myfile.seek(0)
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print("--")
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)
myfile.close()
print("--")
print("--")

with open("myfile.txt",mode='r') as f:
    print(f.read())

with open("myfile.txt",mode='a') as f:
    f.write("\nNUEVA LINEA")

with open("myfile.txt", mode='r') as f:
    print(f.read())

with open("archivo2.txt", mode='w') as f:
    f.write("archivo creado desde Python")

with open('archivo2.txt', mode='r') as f:
    print(f.read())
