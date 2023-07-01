# Importar las librerias
import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
import VentanaContenido
import voz
import generacionImagenes


ventana=ctk.CTk()
ventana.title("Pantalla Principal")
ventana.geometry("900x550")
ventana.resizable(False,False)
ctk.set_appearance_mode("dark")

#Pantalla de las opciones
pantalla=ctk.CTkFrame(ventana)
pantalla.pack(fill=tkinter.BOTH, expand=True)

def abrir_opciones(opcion_nombre):
    #para limpiar el contenido de la ventan principal con respecto a sus opciones
    for pantallas in pantalla.winfo_children():
        pantallas.destroy()

    barra_opciones=ctk.CTkFrame(pantalla)
    barra_opciones.pack(side="top",fill=ctk.X)

    #Botones para regresar al menu principal
    boton_volver=ctk.CTkButton(barra_opciones,text="Menu Principal", command=menuPrincipal)
    boton_volver.pack(side="left",padx=10,pady=10)

    #CREAR UNA CONDICIONAL EN BASE A LA SELECCION
    if opcion_nombre=="Opcion1":
        opcion1()
    elif opcion_nombre=="Opcion2":
        opcion2()
    elif opcion_nombre=="Opcion3":
        opcion3()
#funcion para redirigir al menu
def menuPrincipal():
    for pantallas in pantalla.winfo_children():
        pantallas.destroy()
    cargar_contenidoMenu()
    

#Cargar contenido del Menu
def cargar_contenidoMenu():
    #Imagen de fondo para la ventana
    fondo=Image.open("fondo.jpg")
    fondo=fondo.resize((900,550))

    fondo_Imagen=ctk.CTkLabel(pantalla)
    imagen_fondo=ImageTk.PhotoImage(fondo)
    fondo_Imagen.configure(image=imagen_fondo)
    fondo.image=imagen_fondo
    fondo_Imagen.place(x=0,y=0)
    #Titulo de su Trabajo Final
    titulo=ctk.CTkLabel(pantalla,text="Titulo de su Trabajo Final", font=("Arial",30))
    titulo.place(x=200,y=50)
    integrantes=ctk.CTkLabel(pantalla,text="Integrantes del grupo", font=("Verdana",16))
    integrantes.place(x=200,y=100)

    #cREAR LOS BOTONES DE LAS OPCIONES
    #Boton Opcion 1
    imagen_opcion1=Image.open("opcion1.png")
    imagen_opcion1=imagen_opcion1.resize((150,70))
    btn_imagenOpcion1=ctk.CTkButton(pantalla,image=ImageTk.PhotoImage(imagen_opcion1), command=lambda:abrir_opciones("Opcion1"), font=("Verdana",18), text="Generación de Imagenes con IA")
    btn_imagenOpcion1.place(x=150,y=200)
    #Boton Opcion 2
    imagen_opcion2=Image.open("opcion2.jpg")
    imagen_opcion2=imagen_opcion2.resize((150,70))
    btn_imagenOpcion2=ctk.CTkButton(pantalla,image=ImageTk.PhotoImage(imagen_opcion2), command=lambda:abrir_opciones("Opcion2"), font=("Verdana",18), text="Aprende a Programar")
    btn_imagenOpcion2.place(x=150,y=300)

    #Boton Opcion 3
    imagen_opcion3=Image.open("opcion3.jpg")
    imagen_opcion3=imagen_opcion3.resize((150,70))
    btn_imagenOpcion3=ctk.CTkButton(pantalla,image=ImageTk.PhotoImage(imagen_opcion3), command=lambda:abrir_opciones("Opcion3"), font=("Verdana",18), text="Realiza una Pregunta por Voz")
    btn_imagenOpcion3.place(x=150,y=400)

#Opcion 1  del menu
def opcion1():
    ventana = tkinter.Toplevel()
    generacionImagenes.contenido_ventana(ventana)
#Opcion 2
def opcion2():
    ventana = tkinter.Toplevel()
    VentanaContenido.contenido_ventana(ventana)
    
#Opcion 3 del menu

def opcion3():
    ventana = tkinter.Toplevel()
    voz.contenido_ventana(ventana)

cargar_contenidoMenu()
ventana.mainloop()
