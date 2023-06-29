#Importar las librerias
import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk
import openai
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import os
import requests, io

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
    fondo=fondo.resize((800,512))

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
    def generacion():
        openai.api_key=("") #API KEY OBTENIDO
        user_prompt = entrada_prompt.get("0.0", tkinter.END)
        user_prompt += "in style: " + estilos_selector.get()
        #Realizar la creacion de la imagen en base al prompt enviado
        response=openai.Image.create(
            prompt=user_prompt,
            n=int(slider_cantidad.get()),
            size="512x512"
        )
        #Almacenar el resultado de las imagenes generadas en una lista vacia
        Imagen_url=[]
        for i in range(len(response['data'])):
            Imagen_url.append(response['data'][i]['url'])
        print(Imagen_url)
        #Recorrido de las url creadas y pasar al ingreso de las imagenes a la lista Imagenes 
        
        imagenes=[]
        for url in Imagen_url:
            response = requests.get(url)
            image=Image.open(io.BytesIO(response.content))
            imagenGenerada=ImageTk.PhotoImage(image)
            imagenes.append(imagenGenerada)

    #Funcion para el ingreso de las imagenes al LIENZO
        def ingreso_imagen(index=0):
            canvas.image = imagenes[index]
            canvas.create_image(0, 0, anchor="nw", image=imagenes[index])
            index = (index + 1) % len(imagenes) 
            canvas.after(3000, ingreso_imagen, index)

        ingreso_imagen()

    #Paso 5.Crear la pantalla con los componentes:
    ventana=ctk.CTk()
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
    slider_cantidad=ctk.CTkSlider(pantalla, from_=1, to=10, number_of_steps=9)
    slider_cantidad.grid(row=2,column=1)

    #Boton para la generacion
    boton=ctk.CTkButton(pantalla,text="Generar Imagen", command=generacion)
    boton.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

    canvas=tkinter.Canvas(ventana,width=512,height=512)
    canvas.pack(side="left")

    ventana.mainloop()
#Opcion 2 del menu
def opcion2():
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

    canvas=tkinter.Canvas(ventana,width=512, height=512)
    canvas.pack(side="left")

    #Insercion de la imagen
    imagen=Image.open("aprender.jpg")
    imagen=imagen.resize((512,512))
    imagen_mostrada=ImageTk.PhotoImage(imagen)
    imagen_label=tkinter.Label(canvas,image=imagen_mostrada)
    imagen_label.pack()

    ventana.mainloop()

#Opcion 3 del menu
def opcion3():
    def obtener_respuesta(pregunta):
        respuesta=openai.Completion.create(
            engine="text-davinci-003",
            prompt=pregunta,
            temperature=0.5,
            max_tokens=200,
        )
        return respuesta.choices[0].text.strip()

    #FUNCION PARA ACTIVAR EL RECONOCIMIENTO DE VOZ
    def reconociminetovVoz():
        r=sr.Recognizer()
        with sr.Microphone(device_index=2) as source:
            print("Cual su pregunta?")
            audio=r.listen(source)
        try:
            pregunta=r.recognize_google(audio,language="es-ES")
            entrada_prompt.delete("0.0",tkinter.END)
            entrada_prompt.insert(tkinter.END,pregunta)
            generar_respuesta()
        except sr.UnknownValueError as e:
            print("Error no se reconocio el audio")
        except sr.RequestError as re:
            print("Error comprube su conexion a internet")

    def generar_respuesta():
        pregunta=entrada_prompt.get("0.0",tkinter.END)
        respuesta=obtener_respuesta(pregunta)
        respuesta_text.delete("0.0",tkinter.END)
        respuesta_text.insert('end',respuesta)
        convertirVoz(respuesta)

    #Funcion para convertir el texto en voz
    def convertirVoz(texto):
        engine=pyttsx3.init()
        engine.setProperty("rate",150)
        engine.say(texto)
        engine.runAndWait()

    #CREACION DE LAS VENTANA
    ventana=ctk.CTk()
    ventana.title("Aprende a Programar - CATEC")
    ctk.set_appearance_mode("dark")
    pantalla=ctk.CTkFrame(ventana)
    pantalla.pack(side="left",padx=20,pady=20)

    prompt_label=ctk.CTkLabel(pantalla,text="Ingrese su pregunta.")
    prompt_label.grid(row=0,column=0,padx=10,pady=10)
    entrada_prompt=ctk.CTkTextbox(pantalla,height=10)
    entrada_prompt.grid(row=0,column=1,padx=10,pady=10)

    #Boton para el envio del prompt al servicio del modelo
    boton=ctk.CTkButton(pantalla,text="Realizar Pregunta", command=generar_respuesta )
    boton.grid(row=1,column=0,padx=10,pady=10)

    #Bton para obtner la respuesta con voZ
    boton_voz=ctk.CTkButton(pantalla,text="Pregunta por Voz",command=reconociminetovVoz)
    boton_voz.grid(row=1,column=1,padx=10,pady=10)

    #MOSTRAR EN PANTALLA LA RESPUESTA OBTENIDA POR EL MODELO
    respuesta_label=ctk.CTkLabel(pantalla,text="Respuesta")
    respuesta_label.grid(row=2,column=0,padx=10,pady=10)
    respuesta_text=ctk.CTkTextbox(pantalla,height=200)
    respuesta_text.grid(row=2,column=1,padx=10,pady=10)

    canvas=tkinter.Canvas(ventana,width=512, height=512)
    canvas.pack(side="left")

    #Insercion de la imagen
    imagen=Image.open("aprender.jpg")
    imagen=imagen.resize((512,512))
    imagen_mostrada=ImageTk.PhotoImage(imagen)
    imagen_label=tkinter.Label(canvas,image=imagen_mostrada)
    imagen_label.pack()

    ventana.mainloop()

ventana=ctk.CTk()
ventana.title("Pantalla Principal")
ventana.geometry("800x512")
ventana.resizable(False,False)
ctk.set_appearance_mode("dark")

#Pantalla de las opciones
pantalla=ctk.CTkFrame(ventana)
pantalla.pack(fill=tkinter.BOTH, expand=True)


cargar_contenidoMenu()
ventana.mainloop()