#crear una lista 
nombres=["kevin","Yelsit","Nayeli","Alfredo","limberth","jhonnatan"]
print("Ejercicio 1 - acceder al primer elemento de la lista")
print("el primer elento de la lista es: ",nombres[0])
#acceder al ultimo elemento de la lista 
print("Ejercicio 2 - acceder al ultimo elemento de la lista")
print("el ultimo elento de la lista es: ",nombres[-1])
#acceder a un rango de elemento de la lista 
print("Ejercicio 3 - acceder a un rango de elemento de la lista")
print("el rango de la lista es: ",nombres[0:3])
#modificar elementos de la lista 
print("Ejercicio 4 - modificar elemento de la lista")
nombres[0]="kevin arroyo"
nombres[1]="yelsit ancachi"
nombres[2]="nayeli vargas"
print(nombres)
#modificar varios elementos de la lista 
print("Ejercicio 5 - modificar elemento de la lista")
nombres[3:7]=["alfredo nina","limberth copa", "jhonnatan garcia"] 
print(nombres)
#agregar un elemnto a una lista
print("Ejercicio 6 - agregar un elemento a la lista")
#para añadir un elemento se usa la funcion append
nombres.append("ruth pereira")
print(nombres)
#para añadir varios elemento se usa la funcion extend
print("Ejercicio 7 - agregar varios elementos a la lista")
nombres.extend(["juan gonzales", "erika flores", "estefani condori"])
print(nombres)
#insertar un elemento en una posicion especifica 
print("Ejercicio 8 - insertar un elemento en la posiicion 0")
#para agregar un elemento en una posicion especifica de una lista se usa la funcion insert
nombres.insert(0,"juanito perez")
nombres.insert(1,"pericode lospalotes")
print(nombres)
#eliminar elementos de una lista con la funcion remove
print("Ejercicio 9 - eliminar el nombre de juanito perez")
nombres.remove("juanito perez")
print(nombres)
#eliminar el ultimo elemento de la lista con la funcion pop
print("Ejercicio 10 - eliminar el ultimo elemento de la lista")
nombres.pop()
print(nombres)
#eliminar un elemento  en una posicion especifica con la funcion del
print("Ejercicio 11 - eliminar un elemento  en una posicion especifica")
del nombres[0]
del nombres[5]
del nombres[6]
print(nombres)
#la funcion para ordenar una lista,  con la funcion sort
print("Ejercicio 12 - ordenar una lista ")
nombres.sort()
print(nombres)