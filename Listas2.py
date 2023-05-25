#Suma de elemntos de una lista
notas=[55,78,25,35,90,62]
#Para sumar los elementos de una lista se utiliza la funcion SUM
suma=sum(notas)
print("La suma de las notas es: ",suma)
print("Ejercicio 1 - Calcular el promedio de las notas de la lista")
promedio=suma/6
print("El promedio de las notas es: ",promedio)

#Mostra la cantidad de elemento de una lista notas
print("Ejercicio 2 - Mostrar la cantidad de elementos de la lista de notas")
#Para mostrar la cantidad de elementos  que tiene una lista se utilizara la funcion len
print(len(notas))
print("Ejercicio 3 - Calcular el promedio de las notas con a funcion len")
notafinal=suma/len(notas)
print("La nota es: ",notafinal)

#Contar el numero de veces de cada elemento de una lista
print("Ejercicio 4 - Contar las notas de 55 de la lista de notas")
#Para contar el numero de veces de un elemento de la lista se utiliza la funcion COUNT
print("La cantidad de notas con 55 es: ", notas.count(55))
letras=["a","a","s","g","u","l","g","a","r","45","p",45,12,2,7,True,False]
pritn("La cantidad de veces encontrado es: ",letras.count(False))