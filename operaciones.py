#operadores en python
#operadores aritmeticos
num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero: "))
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num1/num2
potencia=num1**2
potencia2=num2**3
print("la suma de",num1,"+",num2,"=", suma)
print("la resta de",num1,"-",num2,"=", resta)
print("la multiplicacion de",num1,"*",num2,"=", multiplicacion)
print("la division de",num1,"/",num2,"=", division)
print(num1,"elevado a 2 es ",potencia)
print(num2,"elevado a 3 es ",potencia2)
#operadores logicos
print("operadores logicos")
#operador del igual que ==, mayor que >, menor que <, diferente que !=, mayor o igual que >=, menor o igual que <=
print(num1>num2)
#operadores de cadenas de caracteres
print("operadores de cadena de caracteres")
#concatenacion + ,
a="limberth"
b="copa"
#tabulacion \n \t
print(a,b)
print(a, "\n", b)
print(a, "\t", b)
#funciones de cadenas de caracteres
print(" funciones de cadenas de caracteres ")
#len 
print(len(a))
print(min(a))
print(max(b))

print("ejercicio -1 calcular cual de los 2 numeros ingresdos es el mayor")
if num1>num2:
    print("el numero mayor es :",num1)
elif num1==num2:
    print("los 2 numeros ingresados son iguales ")
else:
    print("el numero mayor es :",num2)

print("ejercicio 2 - determinar cual numero es mayor de 3 numeros ingresados por teclado ")
num3=float(input("ingrese un numero: "))
if num1>num2 and num1>num3:
    print("el numero mayor es :",num1)
elif num2>num1 and num2>num3:
    print("el numero mayor es :",num2)
elif num3>num1 and num3>num2:
    print("el numero mayor es :",num3)
elif num3>num1:
    print("el numero mayor es ",num3)
else:
    print("el numero mayor es ",num2)
