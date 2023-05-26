#
print("ejercicio 1- condicionales")
print("ingresara 5 notas, calcular el promedio y determinar si esta aprovado o reprobado")
#variables input: tipo de datos float
#1 variable promedio=sumadenotas/5
#condicion: la nota minima >=61 "aprovado" caso contrario "reprobado"
nota1=float(input("ingrese una nota: "))
nota2=float(input("ingrese una nota: "))
nota3=float(input("ingrese una nota: "))
nota4=float(input("ingrese una nota: "))
nota5=float(input("ingrese una nota: "))
sumanotas=nota1+nota2+nota3+nota4+nota5
promedio=sumanotas/5
if promedio >=61:
    print("aprobado su nota es : ",promedio)
else:
    print("reprobado su nota es : ",promedio)

#bucles
print("bucles")
#condicional while 
print("1.- bucle while")
#while condicion:
    #bloque de codigos
#ejercicio 1
print("ejercicio 2- crear un bucle en donde solamente se desactive al pulsar 0")
numero=None
while numero !=0:
    numero=int(input("ingrese un numero: "))
#caso 2 con condicional if
print("caso 2 mezcla con una condicion if")
while True:
    numero2=int(input("ingrese un numero: "))
    if numero2==0:
        break
#ejercicio 3- mostrar en pantalla la tabla de multiplicar del 9
print("ejercicio 3- tabla de multiplicar")
num1=9
num2=1
resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1,"x",num2,"=",resultado)
    num2=num2+1
#ejercicio 4 -mostrar en pantalla la tabla de multiplicar del numero de usuario 
print("ejercicio 3- tabla de multiplicar con numero del usuario")
num1=int(input("ingrese el numero de la tabla de multiplicar: "))
num2=1
resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1,"x",num2,"=",resultado)
    num2=num2+1
#ejercicio 5- crear un bucle donde se desactive depende el ususario
print("ejercicio 5 ")
num1=int(input("ingrese el numero de la tabla de multiplicar: "))
num2=1
resultado=0
opcion=input("desea ver otra tabla de multplicar? si o no")
while num2<=10:
    resultado=num1*num2
    print(num1,"x",num2,"=",resultado)
    num2=num2+1
    if opcion=="si":
        num1=int(input("ingrese el numero de la tabla de multiplicar: "))
        num2=1
        resultado=0
        while num2<=10:
            resultado=num1*num2
            print(num1,"x",num2,"=",resultado)
            num2=num2+1
    elif opcion=="no":
        break