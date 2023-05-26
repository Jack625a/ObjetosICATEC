#operadores
num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero: "))
suma=num1+num2
resta=num1-num2
multi=num1*num2
div=num1/num2
potencia1=num1**2
potencia2=num2**3
print("la suma es:",suma)
print("la resta es:",resta)
print("la multiplicacion es:",multi)
print("la division es:",div)
print("la potencia1 es:",potencia1)
print("la potencia2 es:",potencia2)

#operadores logicos
print(num1>num2)
#operadores cadenas
a="romer "
b="nina"
print(a+b)

#tabulacion
print(a,"\n", b)
print(a,"\t", b)

#funcion min caracter menor
#funcion max caracter mayor
print(len(a))
print(min(b))
print(max(a))

print("mayor de 2 numeros por teclado")
if num1>num2:
    print("el mayor es: ",num1)
elif num1==num2:
    print("error son iguales")
else:
    print("el mayor es: ",num2)

print("determinar el mayor de tres numeros")
num3=float(input("ingrese un numero: "))
if num1>num2:
    if num1>num3:
        print("el numero mayor es:",num1)
    else:
        print("el numero mayor es:",num3)
elif num2>num3:
    print("el numero mayor es:",num2)
else:
    print("el numero mayor es:",num3)
    
    
    
    