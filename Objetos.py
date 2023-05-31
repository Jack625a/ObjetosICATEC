#Programacion orientada a objetos
#CLASE PERSONA
#INGRESAR EL METODO PARA INICIALIZAR LA CLASE __init__
class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    #ACCIONES O METODOS
    def hablar(self):
        print("HOLA BIENVENIDOS MI NOMBRE ES: ",self.nombre)
        print("Necesito Comer")
    def comer(comida):
        comida=input("Ingrese la comida ")
        print("Esta Comiendo...",comida)
    def dormir(self):
        print(self.nombre," Esta Durmiendo... ZZz")
#OBJETOS DE LA CLASE PERSONA
persona1=Persona("Yel",22,"Hombre")
persona2=Persona("Juano",26,"Hombre")
persona3=Persona("Ari",24,"Mujer")

#LLAMAR A NUESTRAS ACCIONES O METODOS
print("Persona 1")
persona1.hablar()
print("Persona 2")
persona2.comer()
print("Persona 3")
persona3.dormir()