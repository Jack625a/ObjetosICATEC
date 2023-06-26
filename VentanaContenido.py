#Importar las libreriass 
import customtkinter as ctk 
import tkinter
import openai
from PIL import Image, ImageTk

openai.api_key="API KEY" #REEMPLAZAR POR SU API KEY a
def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        temperature=0.5,
        max_tokens=200,
    )
    return respuesta.choices[0].text.strip()

def generar_respuesta():
    pregunta=entrada_prompt.get("0.0",tkinter.END)
    respuesta=obtener_respuesta(pregunta)
    respuesta_text.delete("0.0",tkinter.END)
    respuesta_text.insert(tkinter.END,respuesta)