#condicionales if
print("1 obtener 5 calificaciones por teclado")
print("calcular el promedio y determinar APROB y REPRO")
nota1=float(input("ingrese una nota: "))
nota2=float(input("ingrese una nota: "))
nota3=float(input("ingrese una nota: "))
nota4=float(input("ingrese una nota: "))
nota5=float(input("ingrese una nota: "))
sumaNotas=nota1+nota1+nota1+nota1+nota1
promedio=sumaNotas/5
if promedio>=61:
    print("aprobado con ",promedio)
else:
    print("reprobado con ",promedio)

#bucle condicional while
print("1 bucles condicional while")
numero=None
while numero!=0:
    numero=int(input("ingrese un numero: "))
#caso 2 while con condicional if
while True:
    numero2=int(input("ingrese un numero2: "))
    if numero2==0:
        break
#ejercicio 3 tabla del 9
print("ejercicio 3 tabla del 9")
num1=9
num2=1
resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1," x ",num2," = ",resultado)
    num2=num2+1
print("ejercicio 4 tabla cualquier numero")
num1=int(input("ingrese un numero: "))
num2=1
resultado=0
while num2<=10:
    resultado=num1*num2
    print(num1," x ",num2," = ",resultado)
    num2=num2+1
#5 crear un bucle para cualquier tabla
while True:
    opcion=input("desea continuar si/no: ")
    if opcion=="no":
        break
    num3=int(input("ingrese un numero: "))
    num1=1
    while num1<=10:
        resultado=num3*num1
        print(num3," x ",num1," = ",resultado)
        num1=num1+1
    
#caso 2
pregunta2=None
while pregunta2!="no":
    opcion=input("desea continuar si/no: ")
    if opcion=="no":
        break
    num2=int(input("ingrese un numero: "))
    num1=1
    while num1<=10:
        resultado=num2*num1
        print(num2," x ",num1," = ",resultado)
        num1=num1+1