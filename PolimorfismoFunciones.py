#Polimorfismo con Funciones
#Ejemplo 2 -Crear 3 clases para calcular el area de las figuras aplicando el Polimorfismo
#Area rectangulo - ciruclo - triangulo
class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return self.altura*self.base
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def calcularArea(self):
        return 3.1416*self.radio**2

class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return (self.base*self.altura)/2

def calcularAreas(figura):
    print(f"El area del {figura.calcularArea()}")

#Varibles de entrada para el calculo de las areas
#Menu de opcines de las figuras
while True:
    print("Calculo de Areas de las Figuras")
    opcion=input("Desea seguir calculando las areas de las figuras, Si continuar, No para salir: ")
    if opcion=='Si':
        print("Seleccione la figura que desea calcular su area")
        print("Area del Rectangulo= AR")
        print("Area del Circulo= AC")
        print("Area del Triangulo= AT")
        seleccion=input("> ")
        if seleccion=='AR':
            base=float(input("Ingrese la base: "))
            altura=float(input("Ingrese la altura: "))
            resultado=Rectangulo(base,altura)
            calcularAreas(resultado)
        elif seleccion=='AC':
            radio=float(input("Ingrese el radio: "))
            resultado=Circulo(radio)
            calcularAreas(resultado)
        elif seleccion== 'AT':
            base=float(input("Ingrese la base: "))
            altura=float(input("Ingrese la altura: "))
            resultado=Triangulo(base,altura)
            calcularAreas(resultado)
        else:
            print("Operacion no valida")
    else:
        print("Gracias por utilizar el programa...")
        break








#rectangulo=Rectangulo(60,45)
#circulo=Circulo(7)
#triangulo=Triangulo(20,35)
#print("Area Rectangulo")
#calcularAreas(rectangulo)
#calcularAreas(circulo)
#calcularAreas(triangulo)




