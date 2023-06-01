class Persona:
    #atributos
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    #acciones o meotdos
    def hablar(self):
        print("hello my name's: ",self.nombre)
    def comer(self):
        print("nesecito comer")
        comida=input("ingrese la comida: ")
        print(self.nombre,"comiendo.. ",comida)
    def dormir(self):
        print(self.nombre," est durmiendo.... zzzz")
#objetos de la clase persona
persona1=Persona("romer nina",26,"man")
persona2=Persona("alfredo poma",25,"man")
persona3=Persona("maria",28,"woman")

#LLAMAR A NUESTRAS ACCIONES O METODOS
print("Persona 1")
persona1.hablar()
print("Persona 2")
persona2.comer()
print("Persona 3")
persona3.dormir()