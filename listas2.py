#suma de elementos de una lista
notas=[55,78,25,35,90,62,55,67,55]
#funcion sum
suma=sum(notas)
print("lista: ",notas)
print("la suma es: ",suma)
print("1 promedio de las notas")
promedio=suma/6
print("el promedio es: ",promedio)
#mostrar la cantidad de elementos len
print("2 cantidad de elementos de la lista")
print("longitud de la lista: ",len(notas))
print("3 calcular promedio con funcion len")
notaF=suma/len(notas)
print("el promedio es: ",notaF)
#contar el numero de veces de cada elemento lista
print("3 contar las notas de 55 de la lista")
#para contar el numero de veces de la lista cont
print("cantidad de notas 55 es: ",notas.count(55))

letras=["a","a","a","a","l","g",1,True,False]
print("la cantidad encontrada es",letras.count("g"))