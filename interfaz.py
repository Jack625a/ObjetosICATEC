#import tkinter as tk
from tkinter import *
from tkinter import ttk



ventana = Tk()
#Propieda para establecer el tamaño de una ventana (anchoxalto) =>geometry
ventana.geometry("800x500")
#ventana2=tk.Tk()
#Titulo a la ventana
ventana.title("Objetos I - CATEC")
#Labels (ventana donde se agrega el texto,texto)
#Posicionamiento en los ejes X - Y => Place
titulo=Label(
    ventana, #Ventana donde sera agregada
    text="Objetos I - Python - Tkinter", #texto que se mostrara
    font=("Roboto",35),
    fg="green"
    ).place(x=100,y=5)
#subtitulo=tk.Label(ventana,text="Posicionamiento en los ejes X - Y => Place").place(x=200,y=200)
#Funcion para el click
def clickBoton():
    print("Se hizo click en el boton")
    subtitulo=Label(
        ventana,
        text="Se hizo click en el boton",
        fg="red",
        font=("Happy Money",18)).place(x=200,y=200)
    #subtitulo.Config(text="Se hizo click en el boton")


#Posicionamiento grid maneja la posición en columnas y filas. columm - row

#Botones en Tkinter
#los atributos a definir(ventana donde se agrega el boton, texto)
boton1=Button(
    ventana, #ventana donde se agrega
    text="Boton 1", #Texto del boton
    bg="green", #Color de Fond
    fg="white",
    width=20, #Ancho del boton
    font=("Calibri",18), #Estilo de el texto del boton
    border=10, #Bordeado en el boton
    command=clickBoton
    ).place(x=100,y=100)
#Entrada de datos =>Entry
#Entry(ventana donde se agregara,ancho de la entrada de datos)
#textEntrada=StringVar()
nombre=Entry(
    ventana,#la ventana donde se agrega
    width=20, #definir el ancho de la entrada de datos
    #textvariable=textEntrada
    ).place(x=100,y=250)

#Listas de datos=> Listbox =>insert
#ListBox(ventana donde se agregara, ancho)
listaColores=Listbox(
    ventana, #La venta donde se agrega la lista
    width=20 #Ancho de la lista
    )
#Parametros a definir de la lista(id,texto)
listaColores.insert(0,"Rojo")
listaColores.insert(1,"Verde")
listaColores.insert(2,"Azul")
listaColores.insert(3,"Amarillo")
listaColores.insert(4,"Cafe")
listaColores.insert(5,"Rosado")

listaColores.place(x=100,y=300)
#casillas de verificacion
#Checkbutton
casilla=Checkbutton(ventana,text="PRENDER").place(x=300,y=300)

ventana.mainloop()

