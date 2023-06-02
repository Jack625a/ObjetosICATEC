#Herencia en Programacion Orientada a Objetos
#Ejercico 1 - Herencia Basica
print("Ejercico 1 - Herencia Basica")
#Paso 1 - crear la clase principal (clase PADRE)
class Persona:
    def __init__(self,ci, nombre):
        self.nombre=nombre
        self.ci=ci
    # Definir los metodos o acciones de la clase
    def hablar(self):
        print("Hola bienvenidos mi nombres es",self.nombre)
    def comer(self):
        print(self.nombre," esta comiendo")
#Paso 2 - crear la sub clase en el cual heredaremos los atributos de la clase padre
class Estudiante(Persona):
    def __init__(self,carrera,ci,nombre):
        self.carrera=carrera
        super().__init__(ci,nombre)
    def estudiar(self):
        print(self.nombre, "esta estudiando para su examen de OBJETOS I")

class Docente(Persona):
    def __init__(self,materiadesignada,ci,nombre):
        self.materiadesignada=materiadesignada
        super().__init__(ci,nombre)
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


#Paso 3 - Crear los objetos de la clase Estudiante
estudiante1=Estudiante("Sistemas Infomaticos",3545125,"Kevin Arroyo Montaño")
estudiante2=Estudiante("Sistemas Infomaticos",75455215,"Juan")
estudiante3=Estudiante("Sistemas Infomaticos",96455215,"Maria")
docente1=Docente("Objetos I",742658,"Kevin Arroyo Montaño")
docente2=Docente("Estructura de Datos", 552256,"Alberto Bustamante")

print(estudiante1.nombre)
print(estudiante1.ci)
print(estudiante1.carrera)
estudiante1.hablar()
estudiante1.estudiar()
docente1.evaluar(estudiante2.nombre)
docente2.evaluar(estudiante3.nombre)