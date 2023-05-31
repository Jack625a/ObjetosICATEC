#programacion orientada a objetos
class persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def hablar(self):
        print("hola bienvenido mi nombre es: ",self.nombre)
    def comer(comida):
        comida=input("ingrese la comida: ")
        print("comiendo...",comida)
    def dormir(dormir):
        print("Durmiendo...",dormir)
    def caminar(camina):
        print("Caminando...",camina)

#objetos de la clase persona
persona1=persona("limberth",22,"hombre")
persona2=persona("kevin arroyo",27,"hombre")
persona3=persona("nayeli",20,"mujer")
persona4=persona("fernanda",23,"mujer")
#llamar a nuestras acciones o metodos
print("persona 1")
persona1.hablar()
print("persona 2")
persona2.comer()
print("persona 3")
persona3.dormir()
print("persona 4")
persona4.caminar()