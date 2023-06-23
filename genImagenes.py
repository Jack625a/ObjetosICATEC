import openai
openai.api_key="APIKEY"
mensaje=input("Ingrese el mensaje para la generación de la imagen: ")
respuesta=openai.Image.create(
    prompt=mensaje,
    n=2,
    size="1024x1024"
)
url_imagenGenerada=respuesta['data'][0]['url']
print(url_imagenGenerada)