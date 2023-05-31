#funcion sumar
def sumar(num1,num2):
    resultado=num1+num2
    return resultado
a=float(input("ingrese num con decimal: "))
b=float(input("ingrese num con decimal: "))
print(sumar(a,b))
print(sumar(4.6,5.4))


print("1 determinar si un numero es primo ")
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
numero=int(input("Ingrese un numero: "))
if primo(numero):
    print("El numero ingresado ",numero, "es primo")
else:
    print("El numero ingresado ",numero, "no es primo")