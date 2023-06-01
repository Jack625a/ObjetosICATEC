#Ejercicio 1 - Crear una clase para la utilizacion de una calculadora basica
#Nombre clase => Atributos(self,resultado)
#paso 1 Ingresamos el nombre y los atributos de la clase
class Calculadora:
    def __init__(self):
        self.resultado=0
#Acciones o metodos de la clase - Sumar, Restar, Dividir, Multiplicar
    def sumar(self, num1, num2):
        self.resultado=num1+num2
    def restar(self, num1,num2):
        self.resultado=num1-num2
    def dividir(self, num1,num2):
        if num2!=0:
            self.resultado=num1/num2
        else:
            print("ERROR: no se puede dividir entre cero")
    def multiplicar(self, num1,num2):
        self.resultado=num1*num2
#creacion de los obejtos que pertenecen a la clase CALCULADORA
calculadora=Calculadora()
#Realizar la operaciones de los metodos activos de la clase con respecto a los objetos
#agregar opciones para que el usuario pueda seleccionar que operacion realizar
#los numeros deberan ser con un campo de entrada de datos por teclado
#Añadir un bucle para mostar las opciones de la calculadora hasta que el usuario desee salir 
#1. Continuar con la Calculadora 2. Salir
#While
while True:
    print("¿Desea continuar con la calculadora?")
    continuar=int(input("1. Continuar con la Calculadora 2. Salir: "))
    if continuar==1:
        print("Seleccione la operacion que desea realizar")
        opciones=int(input("1. Sumar - 2. Restar- 3. Multiplicar- 4. Dividir: "))
        if opciones==1:
            a=float(input("Ingrese un número: "))
            b=float(input("Ingrese un número: "))
            calculadora.sumar(a,b)
            print("La suma de",a, "+",b,"=", calculadora.resultado)
        elif opciones==2:
            a=float(input("Ingrese un número: "))
            b=float(input("Ingrese un número: "))
            calculadora.restar(a,b)
            print("La resta de",a, "-",b,"=", calculadora.resultado)
        elif opciones==3:
            a=float(input("Ingrese un número: "))
            b=float(input("Ingrese un número: "))
            calculadora.multiplicar(a,b)
            print("La multiplicar de",a, "x",b,"=", calculadora.resultado)
        elif opciones==4:
            a=float(input("Ingrese un número: "))
            b=float(input("Ingrese un número: "))
            calculadora.dividir(a,b)
            print("La división de",a, "/",b,"=", calculadora.resultado)
        else:
            print("Error operacion no valida")
    else:
        print("Gracias por utilizar la calculadora...")
        break