"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden


  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

set1={"Python","SQL","Estructurado"}
print(set1)

set2={"Hola",True,33,3.1416}
print(set2)

set2_respaldo = set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={""}
print(set3)

set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
set3.add(3)
print(set3)

set3.pop()
set3.pop()
print(set3)

set3.clear()          
print(set3)

set3.add("33")
print(set3)

lista = [10,9.5,8.2,3.4,8.5,10]
print(lista)
conjunto = set(lista)
lista = list(conjunto)
print(lista)

set1={"Python", "SQL", "Estructurado","SQL"}
for i in set1:
 print(set1)
  
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados



#Solucion 1

entrar="si"
emails=set()
while entrar == "si":
  email=input("Ingrese su email: ").strip()
  emails.add(email)
  entrar = input("¿Desea ingresar otro?: ").lower().strip()
print(emails) 

## Version clase

lista_emails=[]
opc="S"
while opc=="S":
  lista_emails.append(input("Ingresa un email: ")).lower().strip()
  opc=input("¿Deseas ingresar otro email (S/N?").upper().strip()
  
set_emails = set(lista_emails)
lista_emails=list(set_emails)
print(emails)

#Solucion 2

## Version clase

lista_emails=[]
opc= True
while opc==True:
  lista_emails.inset(0,input("Ingresa un email: ")).lower().strip()
  opc=input("¿Deseas ingresar otro email (S/N?").upper().strip()
  if opc == "S":
    opc = True
  else:
    opc == False  
    
set_emails = set(lista_emails)
lista_emails=list(set_emails)
print(emails)






## Version tarea
entrar = "si"
emails = []

while entrar == "si":
    email = input("Ingrese su email: ").strip()
    emails.append(email)  
    entrar = input("¿Desea ingresar otro?: ").lower().strip()

emails_unicos = set(emails)

for correo in emails_unicos:
    print(correo)
    


