#Condicionales IF
print("Ejercicio 1 - Condicionales")
print("Ejercicio 1 - Obtener 5 calificaciones por teclado, calcular el promedio ")
#5 Variables input: tipo de dato de entrada FLOAT
#1 Variable promedio =sumadenotas/5
#Condicion : la nota minima >=61 "Aprobado" caso contrario "reprobado"
nota1=float(input("Ingrese una nota: "))
nota2=float(input("Ingrese una nota: "))
nota3=float(input("Ingrese una nota: "))
nota4=float(input("Ingrese una nota: "))
nota5=float(input("Ingrese una nota: "))
SumaNotas=nota1+nota2+nota3+nota4+nota5
promedio=SumaNotas/5
if promedio>=61:
    print("APROBADO con: ", promedio)
else:
    print("REPROBADO con: ", promedio)

#Bucles
#1 Bucles Condicionales WHILE
print("1. Bucles Condicionales - WHILE")
#while condicion:
    #Bloque de Códigos
#Ejercicio 2
print("Ejercicio 2 - Crear un bucle en donde solamente se desactive cuando el usuario ")
numero=None
numero=None
while numero !=0:
    numero=int(input("Ingrese un numero "))

#caso 2 con condicional if
print("Caso 2 - Mezcla con una condicional IF")
while True:
    numero2=int(input("Ingrese un numero"))
    if numero2==0:
        break
#Ejercicio 3 - Mostrar en pantalla la tabla de multiplicar del 9

#Condicion <=  10
#Incremento b++
#Decremento b--
#variables 2 - a=9 , b=1
#Resultado=a*b
#print(a,"x",b,"=", resultado)
num1=9
num2=1
Resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1," X ", num2, "=", resultado)
    num2=num2+1

#Ejercicio 4 - Mostrar en pantalla  la tabla de multiplicar que el usuario ingrese por teclado
num1=int(input("Ingrese el numero que desee"))
num2=1
Resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1," X ", num2, "=", resultado)
    num2=num2+1

#Ejercicio 5 - Crear un bucle donde se desactive cuando el usuario asi lo decida, el bucle 2 preguntara al usuario que tabla de multiplicar desea ver
#Desea seguir mostrando las tablas de multiplicar

num1=int(input("Ingrese el numero que desee"))
num2=1
Resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1," X ", num2, "=", resultado)
    num2=num2+1

#2 Bucles Interactivos FORD
print("2. Bucles Interactivos - FORD")