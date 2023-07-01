#Importar las librerias 
import customtkinter as ctk 
import tkinter
import openai
from PIL import Image, ImageTk
from tkinter import ttk

openai.api_key="" #REEMPLAZAR POR SU API KEY 

#respuesta_label=ctk.StringVar(value="")

def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        temperature=0.6,
        max_tokens=200,
    )
    return respuesta.choices[0].text.strip()

def generar_respuesta():
    seleccion=lista_opciones.get()
    prompt=f"Convertirse en experto en {seleccion} y realizar una explicación detallada de la pregunta."
    pregunta=entrada_prompt.get("0.0",tkinter.END)
    pregunta=f"{prompt} {pregunta}"
    respuesta=obtener_respuesta(pregunta)
    respuesta_text.delete("0.0",tkinter.END)
    respuesta_text.insert('end',respuesta)
    #respuesta_label.configure(text=respuesta)
    #print(respuesta)

ventana=ctk.CTk()
ventana.title("Aprende a Programar - CATEC")
ctk.set_appearance_mode("dark")
pantalla=ctk.CTkFrame(ventana)
pantalla.pack(side="left",padx=20,pady=20)

#Selector de lista de opciones para la mejora de la respuesta (Lista en base a su tema)
opciones=["Php","Python","Css","C","C++","Java","Kotlin"] #grupo 1
opciones2=["Alimentacion Saludable","Alimentacion para bajar de peso","Alimentacion para enfermedades","Alimentacion para Niños","Alimentacion para Adultos Mayores"]#GRUPO 2
lista_opciones=ttk.Combobox(pantalla,values=opciones2)
lista_opciones.grid(row=0,column=1, padx=10,pady=10)

titulo=ctk.CTkLabel(pantalla,text="Seleccione un Lenguaje de Programación que desea aprender")#GRUPO 1
titulo2=ctk.CTkLabel(pantalla,text="Seleecione el tipo de alimentacion que desea consultar")#GRUPO 2
titulo2.grid(row=0,column=0,padx=10,pady=10)
prompt_label=ctk.CTkLabel(pantalla,text="Ingrese su pregunta.")
prompt_label.grid(row=1,column=0,padx=10,pady=10)
entrada_prompt=ctk.CTkTextbox(pantalla,height=10)
entrada_prompt.grid(row=1,column=1,padx=10,pady=10)

#Boton para el envio del prompt al servicio del modelo
boton=ctk.CTkButton(pantalla,text="Realizar Pregunta", command=generar_respuesta )
boton.grid(row=2,column=1,padx=10,pady=10)

#MOSTRAR EN PANTALLA LA RESPUESTA OBTENIDA POR EL MODELO
respuesta_label=ctk.CTkLabel(pantalla,text="Respuesta")
respuesta_label.grid(row=3,column=0,padx=10,pady=10)
respuesta_text=ctk.CTkTextbox(pantalla,height=200,width=250)
respuesta_text.grid(row=3,column=1,padx=10,pady=10)
#boton para volver al menu
boton_menu=ctk.CTkButton(pantalla,text="Menu Principal",command=ventana.quit)
boton_menu.grid(row=4,column=0,columnspan=2, sticky="news", padx=10, pady=10)

canvas=tkinter.Canvas(ventana,width=512, height=512)
canvas.pack(side="left")

#Insercion de la imagen
imagen=Image.open("aprender.jpg")
imagen=imagen.resize((512,512))
imagen_mostrada=ImageTk.PhotoImage(imagen)
imagen_label=tkinter.Label(canvas,image=imagen_mostrada)
imagen_label.pack()

ventana.mainloop()




