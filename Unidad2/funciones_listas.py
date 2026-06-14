"""
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")

#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]

numeros=[23,45,8,24]

varios=["hola",3.1416,True]

vacia=[]

#Imprimir el contenido de una lista

print(paises)
print(numeros)
print(varios)
print(vacia)
print(paises[1])

#Recorrer la lista
#1er forma
for i in paises:
    print(i)

# #2do forma
for i in range(0,len(paises)):
    print(paises[i])


#ordenar elementos de una lista
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
paises.sort() #Ordena la lista de forma ascendente
print(paises)

#dar la vuelta a una lista

paises.reverse() #Da la vuelta a la lista
print(paises)



#Agregar, insertar, Añadir un elemento a una lista
#1er forma
paises.append("Honduras") #Agrega un elemento al final de la lista
print(paises)

#2da forma
paises.insert(1,"Colombia") #Agrega un elemento en la posicion que se le indique
print(paises)
paises.insert(8,"Australia") #Agrega un elemento en la posicion que se le indique
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4) #Elimina el ultimo elemento de la lista
print(paises)

#2da forma
paises.remove("EUA") #Elimina el elemento que se le indique
print(paises)

#Buscar un elemento dentro de la lista
resp= "Brasil" in paises
print(resp)

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
num=int(input("Ingrese un numero a buscar: "))
cuantos= numeros.count(num)
print(f"El numero {num} aparece {cuantos} veces en la lista")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion=numeros.index(23) #Regresa la posicion del primer elemento que encuentra
print(f"La posicion del numero es {posicion}")

#Unir el contenido de una lista dentro de otra lista
numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
numeros2=[500,100]
print(numeros2)
numeros.extend(numeros2) #Agrega el contenido de numeros2 a numeros
print(numeros)
#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
resultante=numeros+numeros2
print(resultante)
resultante.sort()
resultante.reverse()
print(resultante)




