from tkinter import *
from tkinter import ttk


ventana = Tk()
#Propieda para establecer el tamaño de una ventana (anchoxalto) =>geometry
ventana.geometry("800x500")
#ventana2=tk.Tk()
#Titulo a la ventana
ventana.title("Objetos I - CATEC")
#Variables de Control
#Tipo numerico
entero=IntVar()
decimal=DoubleVar()
#Tipo cadenas de caracteres
cadena=StringVar(value="Tipos de datos Cadena de Carcteres")
#Tipo Logicos, booleanos
booleano=BooleanVar()
#Metodo SET =>ASIGNAR UN VALOR 
nombre=StringVar()
ci=IntVar()
nombre.set("Kevin Arroyo Montaño")
ci.set(5514753)
resultado=Entry(ventana,textvariable=nombre, width=20).place(x=200,y=50)
resultado2=Label(ventana,textvariable=ci).place(x=200,y=100)
#Metodo GET =>OBTENER UN VALOR
print("Nombre del usuario: ",nombre.get())
print("Numero de carnet: ",ci.get())
#Metodo TRACE =>DECTAR LOS CAMBIOS DE ESTADO DE UNA VARIABLE
#componente.trace(tipo,funcion)
#Sucesos en el tipo de analisis
#1. Lectura de variable "r"
#2. Escritura del valor "w"
#3. Borrado de la variable "u"
def cambiar(*args):
    print("Se realizo cambios en el valor de la varibale")
def leer(*args):
    print("Se realizo la lectura del valor de la variable")
materia=StringVar()
materia.trace("w",cambiar)
materia.trace("r",leer)
materia.set("Objetos I")
print(materia.get())
print(materia.get())



ventana.mainloop()