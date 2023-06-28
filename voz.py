#Instalar las librerias a uttilizar
#pip install SpeechRecognition (REALIZA EL RECONOCIMIENTO DE VOZ)
#pip install pyttsx3 (CONVIERTE EL TEXTO EN VOZ)
#IMPOTAR TODAS LAS LIBRERIAS A UTILIZAR
import customtkinter as ctk
import tkinter
import openai
import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk

openai.api_key=""

#fUNCION PARA OBTENER UNA RESPUSTA EN BASE A LA CONECCION CON LA RED NEURONAL DEL MODELO DAVINCI 003
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