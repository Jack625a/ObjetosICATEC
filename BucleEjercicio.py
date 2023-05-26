#Ejercicio 5 - Crear un bucle donde se desactive cuando el usuario asi lo desida, el bucle 2 preguntara al usuario que tabla de multiplicar desea ver
#Desea seguir mostrando las tablas de multiplicar? SI - NO
pregunta=None
while True:
    pregunta=input("Desea seguir mostrando las tablas de multiplicar? Escriba Si par continuar - Escriba No para Salir:> ")
    if pregunta=="NO":
        break
    else:
        nume1=int(input("Que tabla de multiplicar desea ver: "))
        nume2=1
        resultado=0
        while nume2<=10:
            resultado=nume1*nume2
            print(nume1," x ",nume2, "=", resultado)
            nume2=nume2+1

print("CASO 2 ")
#CASO 2
pregunta2=None
while pregunta2!="NO":
    pregunta2=input("Desea seguir mostrando las tablas de multiplicar? Escriba Si par continuar - Escriba No para Salir:> ")
    num1=int(input("Que tabla de multiplicar desea ver: "))
    num2=1
    resultados=0
    while num2<=10:
        resultados=num1*num2
        print(num1," x ",num2, "=", resultados)
        num2=num2+1