#paso 1 - importar las librerias de tkinter
import tkinter as tk
from tkinter import ttk
#paso 2 - crear una ventana
ventana=tk.Tk()
#propiedad para establecer el tamaño de una ventana(ancho y alto )con geometry
#ventana2=tk.Tk()
ventana.geometry('800x800+100+100')
#asignar un nombre a la ventana
ventana.title("ventana de prueba - objetos I - CATEC")
#titulo de la pagina o programa
titulo=tk.Label(
    ventana,
    text="objetos I - Python - Tkinder",
    font=("roboto",35)
    ).place(x=150,y=10)
subtitulo=tk.Label(ventana,text="Posicionamiento en los ejes x e y").place(x=250,y=200)
#funciones para el click
def clickboton():
    print("se hizo click en el boton")
    subtitulo=tk.Label(
        ventana,
        text="se hizo click en el boton",
        font=("arial",15)
        ).place(x=250, y=200)
    #subtitulo.config(tex="se hizo click en el boton")
#botones en tkinter
#los atributos a definir son: la ventana donde se agrega el boton, tex
boton1=tk.Button(
    ventana, #ventana donde se agrega
    text="boton 1",#texto del boton
    bg="green",#color de fondo del boton
    fg="yellow",
    width=10,#ancho del boton
    font=("calibri",18), #estilo de fuente del botos
    border=10,#borde del boton
    command=clickboton
    ).place(x=100, y=100)

#entrada de datos =  Entry
nombre=tk.Entry(
    ventana, #casilla donde se agregara
    width=20
    ).place(x=100,y=250)
#listas de datos con listbox
listaColores=tk.Listbox(
    ventana, #la ventana de la lista
    width=20 #el ancho de la lista
    ).place(x=100, y=350)
#parametros a definir de la lista (id, texto)
listaColores.insert(0,"rojo")
listaColores.insert(1,"mostaza")
listaColores.insert(2,"azul")
listaColores.insert(3,"verde")
listaColores.insert(4,"celeste")
listaColores.insert(5,"cafe")

listaColores.place(x=100,y=300)
#
#ckeckbutton
casilla=Checkbutton(ventana,tex="prender").place(x=300,y=200)
#mostrar la ventana creada
ventana.mainloop()


