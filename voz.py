#Instalar las librerias a uttilizar
#pip install SpeechRecognition (REALIZA EL RECONOCIMIENTO DE VOZ)
#pip install pyttsx3 (CONVIERTE EL TEXTO EN VOZ)
#IMPOTAR TODAS LAS LIBRERIAS A UTILIZAR
import customtkinter as ctk
import tkinter
import openai
import pyttsx3
import speech_recognition as sr

openai.api_key="API_KEY"

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