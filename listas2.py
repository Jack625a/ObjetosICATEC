#Suma de elementos de una lista
notas=[55,78,25,35,90,62,85,55,55]
#Para sumar los elementos de una lista se utiliza la funcion SUM
suma=sum(notas)
print("La suma de las notas es: ",suma)
print("Ejercicio 1 - Calcular el promedio de las notas de la lista")
promedio=suma/7
print("El promedio de las notas es: ",promedio)
#Mostrar la cantidad de elemento de una lista
print("Ejercicio 2 - Mostrar la cantidad de elemento de la lista notas")
#Para mostrar la cantidad de elementos que tiene una lista se utilizara la funcion len
print(len(notas))
print("Ejericicio 3 - Calcular el Promedio de las notas con la funcion len")
notafinal=suma/len(notas)
print("La nota final es: ",notafinal)
#Contar el numero veces de cada elemento de una lista
print("Ejercicio 4 - Contar las notas de 55 de la lista notas")
#Para contar el numero de veces de un elemento de la lista se utiliza la funcion count
print("La cantidad de notas con 55 es: ", notas.count(55))
letras=["a","f","e","w","j","m",54,34,24,True,False,True,True]
print("la cantidad de veces encontrado es: ",letras.count("a"))