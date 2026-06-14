# Ejercicio 1

contador = 0
diccionario = {}
while contador < 1:
	nombre = input("Ingrese nombre: ")
	tel = int(input("Ingrese numero: "))
	diccionario[nombre] = tel
	contador+=1

buscado = input("Buscar: ")


if buscado in diccionario:
	tel = diccionario[buscado]
	print(f"Encontrado: ",buscado)
else:
    print("No encontrado")
    
## Ejercicio 2

# Lista original con muchos duplicados
numeros = [10, 20, 10, 30, 40, 20, 50, 10]

# 1. Convierte la lista en un set para quitar los duplicados
conjunto = set(numeros)

# 2. Convierte el conjunto de nuevo a una lista para poder trabajar con ella
lista_limpia = list(set(conjunto))

# 3. Imprime el resultado
print("Lista limpia:", lista_limpia)