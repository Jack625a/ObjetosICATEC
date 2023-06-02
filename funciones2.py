#validar formulario: entrada de datos correo @
print("validar formulario: entrada de datos correo @")
#PASO 1: determinar los parametros de la funcion
def validarCorreo(email):
    simbolo="@"
    correoValidado=False
    for x in email:
        if x==simbolo:
            return True
    return False

def validarMovil(movil):
    cantidad=0
    while movil!=0:
        cantidad+=1
        print(cantidad)
        movil//=10 #division entero
        print(movil)
    return cantidad==8

print("FORMULARIO DE REGISTRO")
#nombre=input("Ingrese su nombre: ")

nombre=input("Ingrese su nombre: ")
if nombre.isalpha():
  print("el nombre es: ",nombre)
else:
  print("el nombre no debe estar vacio")

while True:
    movil=int(input("Ingrese su movil: ")) 
    if validarMovil(movil):
        print("Celular valido")
        print("Se registro correctamente movil:",movil)
        break
    else:
        print("Error ingrese un numero de celular valido")

while True:
    correo=input("Ingrese su Correo: ")  
    if validarCorreo(correo):
        print("Registro valido")
        print("Se registro correctamente email:",correo)
        break
    else:
        print("Correo no valido")


