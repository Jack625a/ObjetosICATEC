class Estudiante:
    #atributos
    def __init__(self,carrera,matricula,ci):
        self.carrera=carrera
        self.matricula=matricula
        self.ci=ci
    #acciones o meotdos
    def estudiar(self):
        nombre=input("ingrese su nombre: ")
        print("me gusta estudiar")
        print("mi carrera es: ",self.carrera,)
        print(" mi nombre es: ",nombre)
        print(" mi matricula es: ",self.matricula)
        print(" mi carnet es: ",self.ci)
    def examen(self):
        exa=input("ingrese examen: ")
        print("tengo examen de ",exa)
        print("mi carrera es: ",self.carrera,)
        print(" mi matricula es: ",self.matricula)
        print(" mi carnet es: ",self.ci)
#objetos de la clase persona
persona1=Estudiante("medicina",123,"87456")
persona2=Estudiante("ingenieria",124,"87451")
persona3=Estudiante("derecho",125,"78542")

#LLAMAR A NUESTRAS ACCIONES O METODOS
print("Persona 1")
persona1.estudiar()
print("Persona 2")
persona2.examen()

