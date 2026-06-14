# 1er utilizar los modulos
import modulos
modulos.borrar_pantalla()
# modulos.function1()
n="Daniel Carreon"
a="Carreon"

nombre,apellidos=modulos.funcion4(n,a)
print(f"El nombre completo es: {nombre} {apellidos}")

#2da formar de utilizar modulos
from modulos import borrar_pantalla, funcion3, funcion4

borrar_pantalla()
n="Daniel Carreon"
a="Carreon"
funcion3(n,a)

nombre,apellidos=funcion4(n,a)
print(f"El nombre completo es: {nombre} {apellidos}")