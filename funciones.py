#Ejercicios funciones - Python
#Realizar una funcion para determinar si un nummero es primo
print("Ejercicios funciones - Python")
print("Realizar una funcion para determinar si un numero es primo")
#Crear la funcion
def primo(numero):
    #Determinar si el numero es primo o no
    if numero<2:
        return False
    for i in (2,int(numero**0.5)+1):
        #Determinar el modulo de los valores de la iteracion
        if numero%i==0:
            return False
    return True

#Ejemplo de uso de la funcion PRIMO
numero=int(input("Ingrese un numero para determinar si es primo: "))
if primo(numero):
    print("El numero ingresado",numero, "es primo")
else:
    print("El numero ingresado",numero, "no es primo")

#Ejercicio 2 - Funcion con Parametro de Caracteres
print("Ejercicio 2 - Crear una funcion para validar un formulario, la entrada de datos de correo debera validarse con el @")
#Nombre, Correo, Celular
#Formulario registro
#Paso 1 : Determinar el nombre y los parametros de la funcion
def validarCorreo(email):
    #Determinar el parametro que validara la entrada de datos
    simboloBuscado="@"
    correoValidado=False
    #Recorrido a la entrada de datos por el usuario
    for x in email:
        if x==simboloBuscado:
            return True
    return False
def validarCelular(celular):
    cantidad=0
    while celular!=0:
        cantidad+=1
        celular//=10
    return cantidad==8
#Ejemplo de uso de la funcion VALIDAR
print("FORMULARIO DE REGISTRO")
nombre=input("Ingrese su nombre: ")
#Agregar la comparativa si cumple o no la condicion de los digitos
while True:
    celular=int(input("Ingrese su celular: "))
    if validarCelular(celular):
        print("Numero Valido")
        break
    else:
        print("ERROR - Ingrese un numero de celular valido")
#Agregar un bucle repetitivo para la validacion  del correo
#Mientras no se ingrese un correo valido el programa debera seguir solicitando 

while True:

    correo=input("Ingrese su correo: ")
    if validarCorreo(correo):
        print("Registro Valido")
        break
    
    else:
        print("Correo no valido - Ingrese su correo nuevamente")

#Crear una funcion que valida la entrada de datos del celular, la cantidad de digitos en Bolivia es 8
#PASO 1 nombre funcion, parametros


print(validarCelular(celular))