#Ejercicio examen 2
#Crear una clase para el manejo del instituto CATEC
#Se tendran 3 clases diferentes.
#Class estudiante- Class Materia - Class Instituto
#class Instituto=> agregarMaterias, agregarEstudiante, agregarDocentes, buscarMateria, buscarDocente, buscarEstudiante
#class Estudiante=> agregarNota, obtenerNota
#class Materia=> verInformacion
#Paso 1. Definir el nombre y atributos de las clases 
class Estudiante:
    def __init__(self,nombre,ci):
        self.nombre=nombre
        self.ci=ci
        self.notas={}
    #Acciones de la clase
    def agregarNota(self,materia,nota):
        self.notas[materia]=nota
    def obtenerNota(self,materia):
        return self.notas.get(materia,"Materia no Encontrada")

class Materia:
    def __init__(self,nombre,sigla,docente):
        self.nombre=nombre
        self.sigla=sigla
        self.docente=docente
    #Acciones de la clase
    def verInformacion(self):
        return f"Materia: {self.nombre} - Siglas: {self.sigla} - Docente: {self.docente}"

class Instituto:
    def __init__(self,nombre):
        self.nombre=nombre
        self.materias=[]
        self.docentes=[]
        self.estudiantes=[]
    #Acciones o Metodos de la clase Instituto
    def agregarMaterias(self,materia):
        self.materias.append(materia)
    def agregarEstudiante(self,estudiante):
        self.estudiantes.append(estudiante)
    def agregarDocentes(self,docente):
        self.docentes.append(docente)

    def obtenerMateria(self):
        for materia in self.materias:
            print(materia.verInformacion())      
    def buscarMateria(self,sigla):
        for materia in self.materias:
            if materia.sigla==sigla:
                return materia
            return None
    def buscarDocente(self,nombre):
        for docente in self.docentes:
            if docente.nombre==nombre:
                return docente
            return None
    def buscarEstudiante(self,ci):
        for estudiante in self.estudiantes:
            if estudiante.ci==ci:
                return estudiante
            return None
#Paso 3. Crear el objeto de la instancia Instituto
catec=Instituto("Instituto CATEC")
#Paso4. Crear la funcion principal para el uso de los metodos o acciones
#funcion principal para agregar materias, estudiantes , docentes
while True:
    opcion=input("Desea seguir agregando mas materias? Si para continuar, No para Salir: ")
    if opcion=="No":
        print("Gracias por agregar las materias la Instituto...")
        break
    else:
        nombreMateria=input("Ingrese el nombre de la Materia: ")
        siglaMateria=input("Ingrese la sigla de la Materia: ")
        docenteMateria=input("Ingrese el docente de la Materia: ")
        materia=Materia(nombreMateria,siglaMateria,docenteMateria)
        catec.agregarMaterias(materia)
#AGREGAR ESTUDIANTES
while True:
    opcion=input("Desea seguir agregando mas estudiantes? Si para continuar, No para Salir: ")
    if opcion=="No":
        break
    else:
        nombreEstudiante=input("Ingrese el nombre del estudiante: ")
        ciEstudiante=int(input("Ingrese el carnet del estudiante: "))
        estudiante=Estudiante(nombreEstudiante,ciEstudiante)
        catec.agregarEstudiante(estudiante)
#BUCEL PARA AGREGAR DOCENTES:
while True:
    opcion=input("Desea seguir agregando mas docentes? Si para continuar, No para Salir: ")
    if opcion=="No":
        break
    else:
        nombreMateriaAsignada=input("Ingrese el nombre de la materia asignada: ")
        nombreDocente=input("Ingrese el nombre del docente: ")
        siglaAsignacion=input("Ingrese la sigla de la Materia Asignada: ")
        docente=Materia(nombreMateriaAsignada,siglaAsignacion,nombreDocente)
        catec.agregarDocentes(docente)
        
#Mostrar todas materias Agregadas en el Instituto
print("Materias del Instituto Catec")
catec.obtenerMateria()
#Funcion Para la calificacion de los estudiantes
while True:
    nombreDocenteMateria=input("Ingrese su nombre completo: ")
    docenteDesignado=catec.buscarDocente(nombreDocenteMateria)
    if docenteDesignado:
        siglaMateria=input("Ingrese la sigla de la materia: ")
        materiaCalificar=catec.buscarMateria(siglaMateria)

        if materiaCalificar:
            for estudiante in catec.estudiantes:
                nota=float(input(f"Ingrese la nota del estudiante {estudiantes.nombre}: "))
                estudiante.agregarNota(materiaCalificar,nota)
            print("Notas calificadas correctamente")
        else:
            print("No se encontro la materia")
    else:
        print("No se encontro al docente")



    



#caso 2

#cambiar por For range(1,100)
while True:
    cantidadFinal=int(input("Cuantos estudiantes desea agregar? "))
    for i in range(1,cantidadFinal+1):
        opcion=input("Desea seguir agregando mas estudiantes? Si para continuar, No para Salir: ")
        if opcion=="No":
            break
        else:
            nombreEstudiante=input("Ingrese el nombre del estudiante: ")
            ciEstudiante=int(input("Ingrese el carnet del estudiante: "))
            estudiante=Estudiante(nombreEstudiante,ciEstudiante)
            catec.agregarEstudiante(estudiante)