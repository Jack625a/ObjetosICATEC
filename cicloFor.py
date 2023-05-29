#Ejercicio COMPLETO - variable, entrada de datos, condicionales, bucles, listas
print("Calcular el promedio de edades de la materia Objetos I y verificar si el promedio es mayor o igual a 23, integrando todas la funcionalidades vistas en clase")
#Solicitar al usuario ingresar la cantidad de edades que se realizara el promedio
cantidad_Edades=int(input("Ingrese la cantidad de estudiantes de la Materia: "))
#Crear una lista vacia para almacenar la edades de los estudiantes
edades=[]
#Solicitar al usuario que ingrese las edades de los estudiantes
for i in range(1,cantidad_Edades+1,1):
    edad=int(input("Ingrese la edad: "))
    edades.append(edad)
#Calcular el Promedio de la edades
suma_Edades=sum(edades)
promedio_Edades=suma_Edades/cantidad_Edades
print("El promedio de las edades es: ",promedio_Edades)
#Verificar si el promedio es mayor o igual a 23
if promedio_Edades>=23:
    print("El promedio de edades de la materia Objetos I ",promedio_Edades, " es mayor a 23")
else:
    print("El promedio de edades de la materia Objetos I ",promedio_Edades, " es menor a 23")