#herencia en programacion orientada a objetos
#ejercicio 1 .- herencia basica
print("ejercicio 1 .- herencia basica")
#crear la clase principal 
class Persona:
    def __init__(self,ci,nombre):
        self.nombre=nombre
        self.ci=ci
        #definir los metodos o acciones de la clase
    def hablar(self):
        print("hola bienvenido mi nombre es ",self.nombre)
    def comer(self):
        print(self.nombre," esta comiendo...")
#paso 2- crear la sub clase en la heredaremos los atributos de la clase
class Estudiante(Persona):
    def __init__(self,carrera, ci, nombre):
        self.carrera=carrera
        super().__init__(ci,nombre)

    def estudiar(self):
        print(self.nombre," esta estudiando para su examen de objetos 1")

class Docente(Persona):
    def __init__(self,materiadesignada,ci,nombre):
        self.materiadesignada=materiadesignada
        super().__init__(ci, nombre)
    def evaluar(self, nombreEstudiante):
        nota1=int(input("ingrese la nota = "))
        nota2=int(input("ingrese la nota = "))
        nota3=int(input("ingrese la nota = "))
        total=nota1+nota2+nota3
        notafinal=total/3
        print("la nota final del estudiante",nombreEstudiante,"es :",notafinal)
        if notafinal <51:
            print("el estudiante",nombreEstudiante,"esta reprobado en la materia",self.materiadesignada,"que es dictado por el docente ",self.nombre)
        else:
            print("el estudiante",nombreEstudiante,"esta aprobado en la materia",self.materiadesignada,"que es dictado por el docente ",self.nombre)
#paso 3.- crear los objetos de clase estudiante
estudiante1=Estudiante("sistemas informaticos",731774,"kevin arroyo")
estudiante2=Estudiante("sistemas informaticos",935664,"limberth copa")
estudiante3=Estudiante("sistemas informaticos",958575,"nayeli vargas")
docente1=Docente("objetos 1",7835776,"kevin montaño")
docente2=Docente("estructura de datos",995866,"alberto bustamante")

print(estudiante1.nombre)
print(estudiante1.ci)
print(estudiante1.carrera)
estudiante1.hablar()
estudiante1.estudiar()
docente1.evaluar(estudiante2.nombre)
docente2.evaluar(estudiante3.nombre)

