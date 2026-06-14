from paquete1 import modulos, modulo_paquete

modulos.borrar_pantalla()

nom="Juan"
ape="Polainas"

nombre,apellidos=modulos.funcion4(nom,ape)
edad=modulo_paquete.solicitar_Edad()

print(f"Nombre: {nombre}\nApellidos:{apellidos}\nEdad: {edad}")