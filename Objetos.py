#Programacion Orientada a Objetos
#CLASE PERSONA
#iNGRESAR EL METODO PARA INICALIZAR LA CLASE __init__
class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    #ACCIONES O METODOS
    def hablar(self):
        print("Hola bienvenidos mi nombre es: ",self.nombre)
    def comer(comida):
        print("Necesito comer")
        comida=input("Ingrese la comida ")
        print(" esta comiendo... ",comida)
    def dormir(self):
        print(self.nombre," est durmiendo.... zzzz")

#OBJETOS DE LA CLASE PERSONA
persona1=Persona("Kevin Arroyo",27,"Hombre")
persona2=Persona("Juan",25,"Hombre")
persona3=Persona("Maria",28,"Mujer")

#LLAMAR A NUESTRAS ACCIONES O METODOS
print("Persona 1")
persona1.hablar()
print("Persona 2")
persona2.comer()
print("Persona 3")
persona3.dormir()

