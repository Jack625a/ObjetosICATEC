#ejercicio 5- crear un bucle donde se desactive depende el ususario
print("ejercicio 5 ")
opcion=input("desea ver otra tabla de multplicar? si o no :")
while True:
    if opcion=="no":
        break
    else:
        num1=int(input("ingrese el numero de la tabla de multiplicar: "))
        num2=1
        resultado=0
        while num2<=10:
            resultado=num1*num2
            print(num1,"x",num2,"=",resultado)
            num2=num2+1

#caso2
print("caso 2- bucles")
pregunta2=None
while pregunta2!="no":
    nume1=int(input("ingrese el numero de la tabla de multiplicar: "))
    nume2=1
    resultado=0
    while nume2<=10:
        resultado=nume1*nume2
        print(nume1,"x",nume2,"=",resultado)
        nume2=nume2+1