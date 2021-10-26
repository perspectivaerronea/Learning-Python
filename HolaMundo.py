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

  

## FOR

myList = [1,2,3,4,5,6,7,8,9,10]
par = 0
impar = 0
total = 0
for num in myList:
    print(f'{total+num} = {total} + {num}')
    total += num    
    #diferencia pares de impares
    if total%2 == 0:
        print(f'{total} es par.')
        par+=1
    else:
        print(f'{total} es impar.')
        impar+=1

print(f"Hay {par} pares y {impar} impares.")

#Si uso _ (guión bajo) determino que el bucle no va a trabar con el elemento con el cual estoy iterando, no sé porque pero es una posibilidad

for _ in 'Hello World':
    print("Buuuu!!! No dependo de nadie")

#Mix de Lista y Tuple - Es más común de lo que se cree y Python se aprovecha de esta posibilidad
myList = [(1,2),(3,4),(5,6), (7,8), (9,10)]

for item in myList:
    print(item)
    for tup in item:
        print(tup)

# TUPLE & PACKING
# Al replicar la estructura interna de la lista, los tuples, obteno los mismos por separado sin necesidad de hacer dos FOR
for (a,b) in myList:
    print(a)
    print(b)
    print(a*b)

myList = [(1,2,3), (4,5,6), (7,8,9)]    
for a,b,c in myList:
    print(b)

#DICCIONARIOS
d = {'k1':1, 'k2':2, 'k3':3, 'k4':4}
for item in d:
    print(item)

#Como vimos el diccionario, por defecto, trae las claves que creamos, más NO sus valores, pero con la propiedad ".items()" podemos obtener los tuples
for item in d.items():
    print(item)
#Ahora que sabemos que con esta combinación obtenemos los tuples podemos usar la técnica de tuple & packaging
for (k,v) in d.items():
    print(f'La clave {k} contiene el valor {v}.')

#Pero si no nos interesan las claves del diccionario y solo queremos los valores podemos usar la propiedad ".values()"
for v in d.values():
    print(f'Valor: {v}')

# BREAK, CONTINUE , PASS
# BREAK - Corta el bucle más cercano - ESCAPE BOTTOM

for v in d.values():
    if v % 2 == 0:
        break
    else:
        print(v)

# CONTINUE - Vuelve al comienzo del bucle más cercano pasando al siguiente ciclo, funciona como un ESCAPE TOP
for v in d.values():
    if v == 3:
        continue
    else:
        print(v)

# PASS - Placeholder para que el compilador no tire error.

# for v in d.values():
    #Comentario
# El coódigo anterior daria error porque al depender de la indentación Python espera encontrar código indentado para determinar el contenido, y por ende, el final del loop
# pero si tenemos un for para usar a futuro, se resuelve con PASS

for v in d.values():
    pass
print("Pasó el bucle sin problemas")

### WHILE
x = 0
while x < 5:
    print(x)
    x+=1
else:
    print("es 5") 
  """  
#RANDOM

mylist = [1,2,3,4,5]
from random import  shuffle 
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

num = (2*5)**(6/(6-3))+0.25
print(num)

#Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Sam Print only the words that start with s in this sentence'

for l in st.split():
    if l[0].lower() == 's':
        print(l)

lista = [w for w in st.split() if w[0] == 's']
print(lista)