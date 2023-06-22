#Paso 1 - Obtener la Api Key de Openai => https://platform.openai.com/account/api-keys
#ApiKey: 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
#Paso 2 - Instalar las librerias
#pip install openai - pip install pillow - pip install customtkinter
#Paso3 - Importar todas las librerias que se usara
import customtkinter as ctk
import tkinter
import openai
from PIL import Image, ImageTk
import os
import requests, io
#Paso 4 - Crear la funcion para la generacion de las Imagenes

def generacion():
    openai.api_key=("") #API KEY OBTENIDO
    user_prompt=prompt_entry.get("0.0",tkinter.END)
    #Realizar la creacion de la imagen en base al prompt enviado
    respuesta=openai.Image.create(
        prompt=user_prompt,
        n=int(number_slider.get()),
        size="512x512"
    )
    #Almacenar el resultado de las imagenes generadas en una lista vacia
    Imagen_url=[]
    for i in range(len(respuesta['data'])):
        Imagen_url.append(respuesta['data'][i]['url'])
    print(Imagen_url)
    #Recorrido de las url creadas y pasar al ingreso de las imagenes a la lista Imagenes 
    imagenes=[]
    for url in Imagen_url:
        respuesta=requests.get(url)
        image=Image.open(io.BytesIO(respuesta.content))
        imagenGenerada=ImageTk.PhotoImage(image)
        imagenes.append(imagenGenerada)

#Funcion para el ingreso de las imagenes al LIENZO
def ingreso_imagen(index=0):
    canvas.image=imagenes[index]
    canvas.create_image(0,0,anchor="nw",image=imagenes[index])
    index=(index+1)% len(imagenes)
    canvas.after(3000,ingreso_imagen,index)

#Llamar a la funcion para la creacion del lienzo
ingreso_imagen()

#Paso 5.Crear la pantalla con los componentes:
ventana=ctk.CTK()
ventana.title("GENERACION DE IMAGENES - CATEC")
ctk.set_appearance_mode("dark")
pantalla=ctk.CTkFrame(ventana)
pantalla.pack(side="left",padx=20,pady=20)
prompt_label=ctk.CTkLabel(pantalla, text="Prompt")
prompt_label.grid(row=0,column=0, padx=10,pady=10)
entrada_prompt=ctk.CTkTextbox(pantalla,height=10)
entrada_prompt.grid(row=0,column=1,padx=10,pady=10)

estilo_label=ctk.CTkLabel(pantalla, text="Estilo de la Imagen")
estilo_label.grid(row=1,column=0,padx=10,pady=10)
estilos_selector=ctk.CTkComboBox(pantalla,values=["Realistic","Cartoon","3D Ilustration","Flat Art"])
estilos_selector.grid(row=1,column=1,padx=10,pady=10)

cantidad_label=ctk.CTkLabel(pantalla, text="Cantidad de Imagenes")
cantidad_label.grid(row=2,column=0)
slider_cantidad=ctK.CTkSlider(pantalla,from_=1, to=5)
slider_cantidad.grid(row=2,column=1)

#Boton para la generacion
boton=ctk.CTkButton(pantalla,text="Generar Imagen", command=generacion)
boton.grid(row=3,column=0,padx=10,pady=10)

canvas=tkinter.Canvas(ventana,width=512,height=512)
canvas.pack(side="left")

ventana.mainloop()

