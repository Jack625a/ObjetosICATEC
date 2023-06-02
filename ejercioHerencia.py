#Ejercicio 2 - Herencia Introduccion
#Crear un clase para Vehiculos el cual tenga sus diferentes atributos y acciones
#Ademas crear sus subclases herendando los atributos y acciones de la clase principal
print("Ejercicio 2 - Herencia - clase Vehiculo - subclase autoSeleccionado")
#paso 1 - Crear clase Padre
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    #crear las acciones o metodos de la clase Vehiculo
    def conducir(self):
        print("El vehiculo ",self.marca, "esta en movimiento")
#Paso2 - Crear las subclases que heredan los atributos y acciones de la clase Padre
class AutoSeleccionado(Vehiculo):
    def __init__(self,marca,modelo,color,tipodecaja,combustible):
        super().__init__(marca,modelo)
        self.color=color
        self.tipodecaja=tipodecaja
        self.combustible=combustible
    #Acciones o metodo de la subclase 
    def tocarbocina(self):
        chofer=input("Quien esta conduciondo el auto? ")
        print(chofer," esta tocando la bocina.... del auto", self.marca)
    def ponermusica(self):
        chofer=input("Quien esta conduciondo el auto? ")
        print(chofer,"puso la musica a todo volumen del auto",self.marca)
#Crear los objetos de la subclase AutoSeleecionado
auto1=AutoSeleccionado("Toyota",2015,"rojo","Mecanico","Gasolina")
auto2=AutoSeleccionado("For",2022,"negro","Automatico","Gasolina")
auto3=AutoSeleccionado("Nissan",2023,"blanco","Automatico","Electrico")

auto1.conducir()
auto2.tocarbocina()
auto3.ponermusica()
