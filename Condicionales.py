#Condicionales IF
print("Ejercicios - Condicionales")
print("Ejercicio 1 - Obtener 5 calificaciones por teclado, calcular el promedio de las notas y determinar la condicion (APROBADO  - REPROBADO) la nota minima es 61")
#5 variables input: tipo de dato de entrada FLOAT
#1 Variable promedio=sumadenotas/5
#condicion: la nota minima >= 61 "aprobado" caso contrario "reprobado"
nota1=float(input("Ingrese una nota: "))
nota2=float(input("Ingrese una nota: "))
nota3=float(input("Ingrese una nota: "))
nota4=float(input("Ingrese una nota: "))
nota5=float(input("Ingrese una nota: "))
sumaNotas=nota1+nota2+nota3+nota4+nota5
promedio=sumaNotas/5
if promedio>=61:
    print("APROBADO con ",promedio)
else:
    print("REPROBADO con ",promedio)

#BUCLES 
print("BUCLES")
#1. BUCLES CONDICIONALES WHILE
print("1. BUCLES CONDICIONALES - WHILE")
#while condicion:
    #bloque de codigos
#Ejercicio 1
print("Ejercicio 2 - crear un bucle en donde solamente se desactive cuando el usuario ingrese 0")
numero=None
numero=None
while numero !=0:
    numero=int(input("Ingrese un numero "))
#caso 2 con condicional if
print("CASO 2 mezcla con una condicional if")
while True:
    numero2=int(input("Ingrese un numero "))
    if numero2==0:
        break
#Ejercicio 3- Mostrar en pantalla la tabla de multiplicar del 9
print("Ejercicio 3- Mostrar en pantalla la tabla de multiplicar del 9")
#condicion b <= 10
#incremento b++ 
#variables 2 - a=9 , b=1
#resultado=a*b
#print(a,"x",b,"=",resultado)
num1=9
num2=1
resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1," x ",num2, "=", resultado)
    num2=num2+1
#Ejercicio 4 - Mostrar en pantalla la tabla de multiplicar del numero que el usuario ingrese por teclado
print("Ejercicio 4 - Mostrar en pantalla la tabla de multiplicar del numero que el usuario ingrese por teclado")
nume1=int(input("Que tabla de multiplicar desea ver: "))
nume2=1
resultado=0
while nume2<=10:
    resultados=nume1*nume2
    print(nume1," x ",nume2, "=", resultados)
    nume2=nume2+1

#Ejercicio 5 - Crear un bucle donde se desactive cuando el usuario asi lo desida, el bucle 2 preguntara al usuario que tabla de multiplicar desea ver
#Desea seguir mostrando las tablas de multiplicar? SI - NO
pregunta=None
while pregunta!="No":
    pregunta=input("Desea seguir mostrando las tablas de multiplicar? Escriba Si par continuar - Escriba No para Salir")
    



#2. BUCLES ITERATIVOS FOR
print("2. BUCLES ITERATIVOS FOR")