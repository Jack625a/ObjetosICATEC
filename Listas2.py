#Suma de elementos de una lista
notas=[55,78,25,35,90,6285,55,55]

#Para sumar los elementos de una lista se utiliza la función SUM
suma=sum(notas)
print("La suma de las notas es: ",suma)
print("Ejercicio 1 - Calcular el promedio de las notas de la lista")
promedio=suma/6
print("El promedio de las notas es: ",promedio)

#Mostrar la cantidad de elementos de una lista
print("Ejercicio 2 -  Mostrar la cantidad de elementos de la lista notas")
#Para mostrar la cantidad de elementos que tiene una lista se utilizara la funcion len
print(len(notas))
print("Ejercicio 3 - Calcular el promedio de las notas con la funcion len")
notafinal=suma/len(notas)
print("La nota final es: ",notafinal)

#Contar el numero veces de cada elemento de una lista
print("Ejercicio 4 - Contar las notas de 55 de la lista de notas")
#Para contar el numero veces de un elemento de la lista se utiliza la funcion COUNT
print("La cantidad de notas con 55 es: ", notas.count(55))
letras=["a","b","c","d","e","f","g","h","i","j","k","l","m",25,12,43,7,True,False]
print("La cantidad de veces encontradas es: ",letras.count(False))