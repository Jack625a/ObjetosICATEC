#Importar las librerias
import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk

#Opcion 1  del menu
def opcion1():
    #
    pass
#Opcion 2 del menu
def opcion2():
    #
    pass
#Opcion 3 del menu
def opcion3():
    #
    pass

ventana=ctk.CTk()
ventana.title("Pantalla Principal")
ventana.geometry("512x512")
ventana.resizable(False,False)
ctk.set_appearance_mode("dark")

#Pantalla de las opciones
pantalla=ctk.CTkFrame(ventana)
pantalla.pack(fill=tkinter.BOTH, expand=True)

#Imagen de fondo para la ventana
fondo=Image.open("fondo.jpg")
fondo=fondo.resize((512,512))

fondo_Imagen=ctk.CTkLabel(pantalla)
imagen_fondo=ImageTk.PhotoImage(fondo)
fondo_Imagen.configure(image=imagen_fondo)
fondo.image=imagen_fondo
fondo_Imagen.place(x=0,y=0)
#Titulo de su Trabajo Final
titulo=ctk.CTkLabel(pantalla,text="Titulo de su Trabajo Final", font=("Arial",30))
titulo.place(x=115,y=50)

#cREAR LOS BOTONES DE LAS OPCIONES
#Boton Opcion 1
imagen_opcion1=Image.open("opcion1.png")
imagen_opcion1=imagen_opcion1.resize((150,70))
btn_imagenOpcion1=ctk.CTkButton(pantalla,image=ImageTk.PhotoImage(imagen_opcion1), command=opcion1, font=("Verdana",18), text="Opcion 1")
btn_imagenOpcion1.place(x=150,y=200)
#Boton Opcion 2
imagen_opcion2=Image.open("opcion2.jpg")
imagen_opcion2=imagen_opcion2.resize((150,70))
btn_imagenOpcion2=ctk.CTkButton(pantalla,image=ImageTk.PhotoImage(imagen_opcion2), command=opcion2, font=("Verdana",18), text="Opcion 2")
btn_imagenOpcion2.place(x=150,y=300)

#Boton Opcion 3
imagen_opcion3=Image.open("opcion3.jpg")
imagen_opcion3=imagen_opcion3.resize((150,70))
btn_imagenOpcion3=ctk.CTkButton(pantalla,image=ImageTk.PhotoImage(imagen_opcion3), command=opcion3, font=("Verdana",18), text="Opcion 3")
btn_imagenOpcion3.place(x=150,y=400)


ventana.mainloop()