#paso 1 herencia basica
print("1 herencia basica")
class Persona:
    def __init__(self,ci,nombre):
        self.nombre=nombre
        self.ci=ci
#definir los metodos o acciones
    def hablar(self):
        print("hi.. ny name's: ",self.nombre)
    def comer(self):
        print(self.nombre," is eating")
#paso 2 crear subclase en el cual se hereda los atrinutos
class Estudiante(Persona):
    def __init__(self,carrera,ci,nombre):
        self.carrera=carrera
        super().__init__(ci,nombre)
    def estudiar(self):
        print(self.nombre,"is studyng for OBJECT I test")

class Docente(Persona):
    def __init__(self,materiaDesig,ci,nombre):
        self.materiaDesig=materiaDesig
        super().__init__(ci,nombre)
    def evaluar(self,nombreEstudiante):
        nota1=float(input("ingrese la nota: "))
        nota2=float(input("ingrese la nota: "))
        nota3=float(input("ingrese la nota: "))
        total=nota1+nota2+nota3
        notafinal=total/3
        print("la nota final del estudiante: ",nombreEstudiante)
        print("es: ",notafinal)
        if notafinal<51:
            print("El estudiante ",nombreEstudiante)
            print("Esta Reprobado en la materia",self.materiaDesig) 
            print("Que es dictada por el docente ",self.nombre)
        else:
            print("El estudiante ",nombreEstudiante)
            print("Esta Aprobado en la materia",self.materiaDesig) 
            print("Que es dictada por el docente ",self.nombre)

#paso 3 crear objetos de la clase estudiante
estudiante1=Estudiante("Sistemas Informaticos",123,"romer nina")
estudiante2=Estudiante("Sistemas Informaticos",456,"alfredo poma")
estudiante3=Estudiante("Sistemas Informaticos",789,"maria")
docente1=Docente("objetos I",654,"kevin arroyo")
docente2=Docente("estructura de datos",987,"alberto bustamante")
print(estudiante1.nombre)
print(estudiante1.ci)
print(estudiante1.carrera)
estudiante1.hablar()
estudiante1.estudiar()
docente1.evaluar(estudiante2.nombre)
docente2.evaluar(estudiante3.nombre)