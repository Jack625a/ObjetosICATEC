#ejercicio 2 - herencia intriduccion
#crear una clase para vehiculos el cual tenga sus diferentes atributos y acciones
#
print("ejercicio 2 - herencia - clase vehiculo - sub clase autoseleccionado")
#paso 1 crear la clase padre
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
#crear las acciones o metodos de la clase vehiculos
    def conducir(self):
        print("el vehiculo",self.marca,"esta en movimiento...")
#paso 2 - crear las sub clases que heredan los atributos y acciones de la clase padre
class Autoseleccionado(Vehiculo):
    def __init__(self, marca, modelo,color,tipodecaja,combustible):
        super().__init__(marca, modelo)
        self.color=color
        self.tipodecaja=tipodecaja
        self.combustible=combustible
    #acciones o metodos de la subclase
    def tocarbocina(self):
        chofer=input("quien esta conduciendo el auto? ")
        print(chofer," esta tocando la bocina...del auto",self.marca)
    def ponermusica(self):
        chofer=input("quien esta conduciendo el auto? ")
        print(chofer," esta reproduciendo la musica' ave de paso - grupo los genios '")
#crear los objetos
auto1=Autoseleccionado("toyota",2015,"rojo","mecanico","gasolina")
auto2=Autoseleccionado("for",2022,"negro","automatico","gasolina")
auto3=Autoseleccionado("nissan",2023,"blanco","automatico","electrico")

auto1.conducir()
auto2.tocarbocina()
auto3.ponermusica()