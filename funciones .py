#Ejercicios Funciones - Python
#Realizar una funcion para determinar si un numero es primo
print("Ejercicios Funciones - Python")
print("Ejercicio 1 -Realizar una funcion para determinar si un numero es primo ")
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

#Ejercicio 2- Funcion con Parametro de Caracteres
print("Ejercicio 2 - Crear una funcion para validar un formulario, la entrada de datos de correo debera validarse con el @")
#Nombre, Correo, Celular
#Formulario registro
#PASO 1: determinar el nombre y los parametros de la funcion
def validarCorreo(email):
    #Determinar el parametro que validara la entrada de datos
    simboloBuscado="@"
    correoValidado=False
    #Recorrido a la entrada de datos por el usuario
    for x in email:
        if x==simboloBuscado:
            return True
    return False
#Crear una funcion que valide la entrada de datos del celular, la cantidad de digitos para celulares en Bolivia es 8 digitos
#PASO 1 nombre funcion, parametros
def validarCelular(celular):
    cantidad=0
    while celular!=0:
        cantidad+=1
        celular//=10
    return cantidad==8
#Ejemplo de uso de la funcion VALIDAR
print("FORMULARIO DE REGISTRO")
nombre=input("Ingrese su Nombre: ")
#Agrgar la compartiva si cumple o no la condicion de los digitos del celular
while True:
    celular=int(input("Ingrese su Celular: "))
    if validarCelular(celular):
        print("Celular valido")
        break
    else:
        print("Error ingrese un numero de celular valido")
#Agregar un bucle repetitivo para la validacion del correo
#Mientras no se ingrese un correo valido el programa debera seguir solicitando ingresar un correo
while True:
    correo=input("Ingrese su Correo: ")  
    if validarCorreo(correo):
        print("Registro valido")
        print("Se registro correctamente el nombre ",nombre, " con el correo ",correo)
        break
    else:
        print("Correo no valido")
