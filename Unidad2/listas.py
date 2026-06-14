print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[10,34,25,45]
print(numeros)

lista="["
for i in numeros:
    lista+=f"{i}, "
print(f"{lista}]")


lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]}, "
print(f"{lista}]")

lista="["
i=0
while i < len(numeros):
    lista+=f"{numeros[i]}, "
    i+=1
print(f"{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra


palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabra=input("Ingrese una palabra: ").strip()

#1ER FORMA
if palabra in palabras:
    print(f"Encontre la palabra en la lista")
else:
    print(f"No encontre la palabra en la lista")

#2DA FORMA
palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabra=input("Ingrese una palabra: ").strip()
encontro = False
for i in palabras:
    if i == palabra:
        print(f"Encontre la palabra en la lista")
        encontro = True
if encontro== True:
    print(f"Encontre la palabra en la lista")
else:
    print(f"No encontre la palabra en la lista")

#3ER FORMA

palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabra=input("Ingrese una palabra: ").strip()
encontro = False
for i in palabras:
    if palabras[i]:
        print(f"Encontre la palabra en la lista")
        encontro = True
if encontro== True:
    print(f"Encontre la palabra en la lista")
else:
    print(f"No encontre la palabra en la lista")

# 4ta FORMA

palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabra=input("Ingrese una palabra: ").strip()
encontro = False
while i<len(palabras):
    if palabras[i] == palabra:
        print(f"Encontre la palabra en la lista")
        encontro = True
if encontro== True:
    print(f"Encontre la palabra en la lista")
else:
    print(f"No encontre la palabra en la lista")

# Ejemplo 3 Añadir elementos a la lista

lista = ["", ""]

# Version 1
true=True
while true:
    lista.append(input("Ingrese un dato a la lista: ").strip().upper())
    true = input(" Deseas añadir mas elementos (Si/No)? ").lower().strip()
    if true == "no":
        true = False
    else:
        true = True

# Version 2
true="si"
while true=="si":
    lista.append(input("Ingrese un dato a la lista: ").strip().upper())
    true = input(" Deseas añadir mas elementos (Si/No)? ").lower().strip()
print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
    ["Carlos","6181234567"],
    ["Alberto", "6182344567"],
    ["Martin","61812341223"]
    ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[c][r])

lista=""

for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c], }"
    lista+="\n"

print("["+lista+"]")