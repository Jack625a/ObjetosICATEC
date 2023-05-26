#Ejercicio 5 - Crear un bucle donde se desactive cuando el usuario asi lo decida, el bucle 2 preguntara al usuario que tabla de multiplicar desea ver
#Desea seguir mostrando las tablas de multiplicar

num1=int(input("Ingrese el numero que desee"))
num2=1
Resultado=0
 while True:
        pregunta=(input("Ingrese SI o NO"))
        if pregunta!="NO":
            break
while num2<=10:
resultado=num1*num2
    print(num1," X ", num2, "=", resultado)
    num2=num2+1
pregunta=input("Desea seguir mostrando las tablas de multiplicar? Escriba SI para seguir viendo y NO para salir")
if pregunta=="SI":

   