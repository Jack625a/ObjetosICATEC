#Ejercicio 2 - Herencia Vehiculo
print("Ejercicio 2 - Herencia - clase Vehiculo - subclase autoSeleccionado")
#paso 1 crear clase padre
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
#crear acciones o metodos de la clase vehiculo
    def conducir(self):
        print("El vehiculo ",self.marca, "esta en movimiento")
#paso 2 crear subclases para heredar acciones y atributos
class AutoSeleccionado(Vehiculo):
    def __init__(self,marca,modelo,color,tipodecaja,combustible):
        super().__init__(marca,modelo)
        self.color=color
        self.tipodecaja=tipodecaja
        self.combustible=combustible
#acciones o metodos de la subclase
    def tocarBocina(self):
        chofer=input("Quien esta conduciendo el auto? ")
        print(chofer," esta tocando la bocina.... del auto", self.marca)
    def ponerMusica(self):
        chofer=input("Quien esta conduciendo el auto? ")
        print(chofer,"puso la musica a todo volumen del auto",self.marca)
#Crear los objetos de la subclase AutoSeleecionado
auto1=AutoSeleccionado("Toyota",2015,"rojo","Mecanico","Gasolina")
auto2=AutoSeleccionado("Ford",2022,"negro","Automatico","Gasolina")
auto3=AutoSeleccionado("Nissan",2023,"blanco","Automatico","Electrico")

auto1.conducir()
auto2.tocarBocina()
auto3.ponerMusica()