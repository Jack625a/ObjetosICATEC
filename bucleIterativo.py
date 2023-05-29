#Bucle iterativo -FOR
#for i in range(inicio,final,salto):
print("Bucle iterativo -FOR")
print("Ejercicio 1 - motrar los 10 primeros numeros")
for i in range(1,11,1):
    print(i)
#RECORRIDOS EN RANGOS NO CONOCIDOS
#Ejercicio 1  - Mostrar los elemento de una lista con el ciclo for
print("Ejercicio 1  - Mostrar los elemento de una lista con el ciclo for")
numeros=[1,2,3,4,5,6,7,8,9]
for num in numeros:
    print(num)
#Ejercicio 2 - Mostrar la suma de los elementos de la lista NUMEROS
print("Ejercicio 2 - Mostrar la suma de los elementos de la lista NUMEROS")
suma=0
for numero in numeros:
    suma=suma+numero
print("La suma de los numeros es: ",suma)
#Ejercicio 3 - Mostrar los numeros pares del 1 al 100
#Para saber si un numero es par solamente se deberar calcular el MODULO o Residuo y si este es cero, el numero sera par
print("Ejercicio 3 - Mostrar los numeros pares del 1 al 100")
print("Numeros pares del rango del 1 al 100")
for n in range(1,101):
    if n%2==0:
        print(n)
#Ejercicio 4 - Mostrar los numeros pares en un rango determinado por el usuario 
print("Ejercicio 4 - Mostrar los numeros pares en un rango determinado por el usuario ")
inicio=int(input("Ingrese el numero inicial del rango: "))
final=int(input("Ingrese el numero final del rango: "))
for a in range(inicio,final+1):
    if a%2==0:
        print(a)





