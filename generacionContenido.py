#api key:
import openai
openai.api_key=("API_KEY")

def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        temperature=0.5,
        max_tokens=200,
    )
    return respuesta.choices[0].text.strip()

#Funcion principal para la obtencion de respuesta
while True:
    opcion=input("Desea seguir preguntando? Si para continuar, No para Salir ")
    if opcion=="Si":
        pregunta=input("Ingrese su pregunta: ")
        respuesta=obtener_respuesta(pregunta)
        print(respuesta)
    elif opcion== "No":
        print("Gracias por utilizar el servicio...")
        break
    else:
        print("Error operacion no valida")