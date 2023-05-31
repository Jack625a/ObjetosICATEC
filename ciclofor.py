#Ejercicio COMPLETO - variable, entrada de datos, condicionales, bucles, listas
print("Calcular el promedio de edades de la materia Objetos I y verificar si el promedio es mayor o igual a 23, integrando todas la funcionalidades vistas en clase")
#Solicitar al usuario ingresar la cantidad de edades que se realizara el promedio
cantidad_Edades=int(input("Ingrese la cantidad de estudiantes de la Materia: "))
#Crear una lista vacia para almacenar la edades de los estudiantes
edades=[]
nombres=[]
#Solicitar al usuario que ingrese las edades de los estudiantes
for i in range(1,cantidad_Edades+1,1):
    edad=int(input("Ingrese la edad: "))
    edades.append(edad)
    nombre=input("Ingrese nombre: ")
    nombres.append(nombre)
print(nombres[0],edades[0])
#Calcular el Promedio de la edades
suma_Edades=sum(edades)
promedio_Edades=suma_Edades/cantidad_Edades
print("El promedio de las edades es: ",promedio_Edades)
#Verificar si el promedio es mayor o igual a 23
if promedio_Edades>=23:
    print("El promedio de edades de la materia Objetos I ",promedio_Edades, " es mayor a 23")
else:
    print("El promedio de edades de la materia Objetos I ",promedio_Edades, " es menor a 23")
    
#Mostar un elemento especifico de las listas. (nombre - edad)
print("La cantidad de estudiantes es: ", cantidad_Edades)
id=int(input("Ingrese el id de estudiante que desea mostrar la informacion: "))
print("El estudiante seleccionado es: ",nombres[id-1], " y su edad ", edades[id-1])

def mostrar_Estudiante(id):
    identificador=int(input("Ingrese el id del estudiante que desea mostrar la información: "))
    print("El estudiante seleccionado es: ",nombres[identificador-1], " y su edad ", edades[identificador-1])

