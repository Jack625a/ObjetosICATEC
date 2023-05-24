#Crear una lista
nombre=["Kevin","Yeltsin","Ramiro","Alfredo","Alberto","Nayeli"]

#Acceder al primer elemento de la lista
print("Ejercicio 1 - Acceder al primer elemento de la lista")
print("El primer elemento de la lista es: ",nombre[0])

#Acceder al ultimo elemento de la lista
print("Ejercicio 2 - Acceder al primer elemento de la lista")
print("El ultimo elemento de la lista es: ",nombre[4])

#Acceder a un rango de elemento de la lista
print("Ejercicio 3 - Acceder a un rango de elemento de la lista")
print(nombre[4:7])

#Modificar un elemento de la lista
print("Ejercicio 4 - Modificar un elemento de la lista")
nombre[0]="Kevin Arroyo"
nombre[1]="Yeltsin Ancachi"
nombre[2]="Ramiro Ayaviri"
print(nombre)

#Modificar varios elementos de la lista
print("Ejercicio 5 - Modificar varios elementos de la lista")
nombre[3:8]=["Alfredo Nina","Nayeli Vargas","Limberth Copa","Jhonatan Garcia"]
print(nombre)

#Agregar elementos a una lista
#Agregar un elemento a la lista
print("Ejercicio 6 - Agregar un elemento a la lista")
#Para agregar un elemento a la lista se utiliza la funcion del append
nombre.append("Ruth Pereira")
print(nombre)

#Agregar varios elementos a una lista
#Para agregar varios elementos a la lista se utiliza la funcion del extend
print("Ejercicio 7 - Agregar varios elementos a la lista")
nombre.extend (["Juan Gonzales","Maria Claros","Jose Prado"])
print(nombre)

#Insertar un elemnto en una posicicon especifica de la lista
print("Ejercicio 8 - Insertar un elemento en la posicion 0")
#Para agregar eun elemento en una posicion especifica de la lista se utiliza la funcion insert
nombre.insert(0,"Julio Paredes")
nombre.insert(1,"Claudia Rocha")
print(nombre)

#Eliminar elementos de una lista
#Eliminar  un elemnto de la lista
print("Ejercicio 9 - Eliminar el nombre de Juan Gonzales")
#Para eliminar un elemento de la lista se utiliza la funcion remove
nombre.remove("Juan Gonzales")
nombre.remove("Maria Claros")
print(nombre)

#Eliminar el ultimo elemento de la lista
print("Ejercicio 10 - Eliminar el ultimo elemento de la lista")
#Para eliminar el ultimo elemento de cualquier lista se utiliza la funcion pop
nombre.pop()
print(nombre)

#Eliminar un elemento en una posicion especifica
print("Ejercicio 11 - Eliminar un elemento en una posicion especifica")
#Para eliminar un elemento en una posicion especifica se utiliza la funcion del
del nombre[0]
del nombre[7]
del nombre[6]
print(nombre)

#Funcion para ordenar una lista
print("Ejercicio 12 -  Ordenar la lista de nombres")
#Para ordenar una lista en orden alfabetico se debera utilizar la funcion sort
nombre.sort()
print(nombre)
