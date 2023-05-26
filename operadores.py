#Operadores en Python
#Operadores Aritméticos
num1=float(input("Ingrese un numero: "))
num2=float(input("Ingrese un numero: "))  
suma=sum
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num1/num2
potencia=num1**2
potencia2=num2**3
print("La suma de ",num1, "+",num2, "es: ", suma)
print("La resta de ",num1, "-",num2, "es: ", resta)
print("La mutiplicacion de ",num1, "*",num2, "es: ", multiplicacion)
print("La division de ",num1, "/",num2, "es: ", division)
print(num1, "elevado a 2 es ",potencia)
print(num2, "elevado a 3 es ",potencia2)

#Operadores lógicos
print("Operadores Lógicos")
#Operador igual que ==
#Operador mayor que >
#Operador menor que <
#Operador diferente que !=
#Operador mayor o igual que >=
#Operador menor o igual que <=
print(num1>num2)
#Operadores  de cadena de caracteres
print("Operadores de cadena de caracteres")

#CONCATENACION + ,
a="Yel "
b="David "
c="Nayelita"

#Tabulacion y salto de linea \n \t
print(a,b)
print(a, "\n", b)
print(a, "\t", b)

#Funciones de cadena de caracteres
print("Funciones de cadena de caracteres")
#LEN: nos devuelve el numero de caracteres de una cadena
print(len(c))
print(min(a))
print(max(b))
#min: Nos devuelve el caracter menor de la cadena
#max: Nos devuelve el caracter mayor de la cadena


#Condicionales 
print("Ejercicio 1 - cual es el mayor de los dos numeros ingresados por teclado")
if num1>num2:
    print("El numero mayor es ",num1)
elif num1==num2:
    print("Error los dos numeros ingresados son iguales")
else:
    print("El numero mayor es ",num2)

print("Ejercicio 2 - Determinar cual numero es mayor de tres numeros ingresados por teclado")
num3=float(input("Ingrese un numero: "))
if num1>num2 and num1>num3:
    print("El numero mayor es ",num1)
elif num2>num1 and num2>num3:
    print("El numero mayor es ",num2)
elif num3>num1 and num3>num2:
    print("El numero mayor es ",num3)
elif num3>num1:
    print("El numero mayor es ",num3)
else:
    print("El numero mayor es ",num2)