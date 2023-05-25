#crear lista
nombres=["Juan","Lucas","Pedro","Mateo","Tomas"]
#acceder al primer elemnto de la lista
print(nombres)
print("1 primer elemnto de la lista es: ",nombres[0])
#acceder al ultimo elemento de la lista
print("ultimo elemnto de la lista es: ",nombres[3])
print("2 ultimo elemnto de la lista es: ",nombres[-1])
#acceder a un rango del elemnto de la lista
print("3 rango: ",nombres[1:3])
#modificar elementos de la lista
print("4 modificar elemento lista")
nombres[0]="Juan Reyes"
print(nombres)
#modificar varios elementos de la lista
print("5 modificar varios elementos lista")
print(nombres[1:5])
nombres[1:5]=["Lucas Reyes","Pedro Reyes","Mateo Reyes","Tomas Reyes"]
print(nombres)
#agregar elementos a la lista
#agregar un elemnto a la lista
print("6 agregar elemento a la lista")
#agregar al ultimo elemento con append
nombres.append("Judas Tadeo")
print(nombres)
#agregar varios elementos a la lista con extend
print("7 agregar varios elemento a la lista")
nombres.extend(["Abraham Lincoln","Harry Kane","Kyle Walker"])
print(nombres)
#Insertar un elemento en una posicion especifica de la lista
print("8 insertar un elemento en la posicion 0")
#Para agregar un elemento  posicion n funcion insert
nombres.insert(0,"Jordi Alba")
nombres.insert(2,"Frank Lampard")
print(nombres)
#eliminar elemento de la lista
print("9 elimnar elemento de la lista")
#Para eliminar un elemento funcion remove
nombres.remove("Frank Lampard")
print(nombres)
#eliminar el ultimo elemento de la lista
print("10 elimnar el ultimo elemento de la lista")
#para eliminar el ultimo elemento de cualquier lista pop
nombres.pop()
print(nombres)
#eliminar un elemento posicion especifica
print("11 elimnar elemento posicion especifica")
#para eliminar elemento funcion especifica del
del nombres[0]
del nombres[5]
del nombres[6]
print(nombres)
#ordenar la lista
print("11 ordenar la lista")
#para ordenar funcion sort
nombres.sort()
print(nombres)
