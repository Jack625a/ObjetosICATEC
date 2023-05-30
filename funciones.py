#Ejercicios Funciones - Python
#Realizar una funcion para determinar si un numero es primo
print("Realizar una funcion para determinar si un numero es primo")
#crear la funcion
def primo(numero):
    #determinar si el numero es primo o no
    if numero<2:
        return False
    for i in range(2,int(numero**0.5)+1):
        #determinar el modulo de los valores de la iteracion
        if numero%i==0:
            return False
    return True

#Ejemplo de uso de la funcion PRIMO
numero=int(input("Ingrese un número para determinar si es primo: "))
if primo(numero):
    print("El numero ingresado ",numero, "es primo")
else:
    print("El numero ingresado ",numero, "no es primo")