#bucle iterativo for
print("ej 1 mostrara los 10 primeros numeros")
for i in range(1,11,1):
    print(i)
#recorrido en rangos no conocidos
#1 mostrar elementos de la lista ciclo for
print("1 mostrar elementos de la lista ciclo for")
numeros=[1,2,3,4,5,6,7,8,9]
for num in numeros:
    print(num)
print("2 Mostrar la suma de los elementos de la lista")
suma=0
for numero in numeros:
    suma+=numero
print("La suma de los numeros es: ",suma)
print("ej-3 Numeros pares del 1 al 100")
for n in range(1,101):
    if n%2==0:
        print(n)
print("Ej-4 mostrar los numeros pares por teclado")
inicio=int(input("Ingrese el numero inicial del rango: "))
final=int(input("Ingrese el numero final del rango: "))
for a in range(inicio,final+1):
    if a%2==0:
        print(a)
