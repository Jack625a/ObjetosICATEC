#nombre y atributos de la clase
class Calculadora:
    def __init__(self):
        self.resultado=0
#metodos sumar restar multiplicar dividir
    def sumar(self, n1,n2):
        self.resultado=n1+n2
    def restar(self, n1,n2):
        self.resultado=n1-n2
    def dividir(self, n1,n2):
        if n2!=0:
            self.resultado=n1/n2
        else:
            print("no se puede dividir entre 0")
    def multiplicar(self, n1,n2):
        self.resultado=n1*n2
#creacion de objetos que pertenences a calculadora
calculadora=Calculadora()
#realizar las operaciones de los metodos activos respecto a objetos
while True:
    print("¿Desea continuar con la calculadora?")
    print("1 continuar o 2 salir")
    continuar=int(input("opcion: "))
    if continuar==1:
        print("Seleccione la operacion que desea realizar")
        print("1 sumar: 2 restar: 3 multiplicar: 4 dividir")
        opciones=int(input("opcion: "))
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
            print("multiplicacion de",a,"y",b,"=", calculadora.resultado)
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