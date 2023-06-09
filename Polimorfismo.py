#Polimorfismo
#Diferentes casos de Polimorfismo
#Caso 1 - Polimorfismo con metodos
#Ejemplo 1 Clase Persona
class Persona:
    #def __init__(self,ci, nombre):
        #self.nombre=nombre
        #self.ci=ci
    # Definir los metodos o acciones de la clase
    def hablar(self):
        print("Hola bienvenidos mi nombres es")
    def comer(self):
        print(" esta comiendo")
#PASO 1 CREAR LA SUBCLASE -> HERENCIA
class Estudiante(Persona):
    def estudiar(self):
        print(self.nombre, "esta estudiando para su examen de OBJETOS I")

class Docente(Persona):
    def evaluar(self,nombreEstudiante):
        nota1=int(input("Ingrese la nota: "))
        nota2=int(input("Ingrese la nota: "))
        nota3=int(input("Ingrese la nota: "))
        total=nota1+nota2+nota3
        notafinal=total/3
        print("La nota final del estudiante",nombreEstudiante, "es: ",notafinal)
        if notafinal<51:
            print("El estudiante ",nombreEstudiante, "esta Reprobado en la materia",self.materiadesignada, "que es dictada por el docente ",self.nombre)
        else:
            print("El estudiante ",nombreEstudiante, "esta Aprobado en la materia",self.materiadesignada, "que es dictada por el docente ",self.nombre)

def hablar_Persona(estudiante):
    print(estudiante.hablar())

estudiante1=Estudiante()
docente1=Docente()
hablar_Persona(estudiante1)
hablar_Persona(docente1)
evaluar(docente1)