#Crear una lista
nombres=["Kevin","Yeltsin","Ramiro","Alfredo","Nayeli","Limberth","Jhonatan"]
#Acceder al primer elemento de la lista
print("Ejercicio 1 - Acceder al primer elemento de la lista")
print("El primer elemento de la lista es: ",nombres[0])
#Acceder al ultimo elemento de la lista
print("Ejercicio 2 - Acceder al ultimo elemento de la lista")
print("El ultimo elemento de la lista es: ",nombres[-1])
#Acceder a un rango de elementos de la lista
print("Ejercicio 3 - Acceder a un rango de elementos de la lista")
print(nombres[4:7])

#Modificar elementos de una lista
print("Ejercicio 4 - Modificar un elemento de la lista")
nombres[0]="Kevin Arroyo"
nombres[1]="Yeltsin Ancachi"
nombres[2]="Ramiro Ayaviri"
print(nombres)
#Modificar varios elemento de una lista
print("Ejercicio 5 - Modificar varios elemento de una lista ")
nombres[3:8]=["Alfredo Nina", "Nayeli Vargas", "Limberth Copa", "Jhonatan Garcia"]
print(nombres)

#Agregar elementos a una lista
#Agregar un elemento a la lista
print("Ejercicio 6 - Agregar un elemento a la lista")
#Para agregar un elemento a la lista se utiliza la funcion del append
nombres.append("Ruth Pereira")
print(nombres)
#Agregar varios elementos a la lista
#Para agregar varios elementos a la lista se utiliza la funcion extend
print("Ejercicio 7 - Agregar varios elementos a la lista")
nombres.extend(["Juan Gonzales", "Maria Claros", "Jose Prado"])
print(nombres)
#Insertar un elemento en una posicion especifica de la lista
print("Ejercicio 8 - Insertar un elemento en la posicion 0")
#Para agregar un elemento en una posicion especifica de la lista se utiliza la funcion insert
nombres.insert(0,"Julio Paredez")
nombres.insert(1,"Claudia Rocha")
print(nombres)

#Eliminar elementos de una lista
#Eliminar un elemento de la lista
print("Ejercicio 9 - Eliminar el nombre de Juan Gonzales")
#Para eliminar un elemento de la lista se utiliza la funcion remove
nombres.remove("Juan Gonzales")
nombres.remove("Julio Paredez")
print(nombres)

#Eliminar el ultimo elemento de la lista
print("Ejercicio 10 - Eliminar el ultimo elemento de la lista ")
#Para eliminar el ultimo elemento de cualquier lista se utiliza la funcion pop
nombres.pop()
print(nombres)
#Eliminar un elemento en una posicion especifica
print("Ejercicio 11 - Eliminar un elemento en una posicion especifica")
#Para eliminar un elemento en una posicion especifica se utiliza la funcion del
del nombres[0]
del nombres[6]
del nombres[7]
print(nombres)

#Funcion para ordenar una lista
print("Ejercicio 12 - Ordenar la lista nombres")
#Para ordenar una lista en orden alfabetico se debera utilizar la funcion sort
nombres.sort()
print(nombres)




