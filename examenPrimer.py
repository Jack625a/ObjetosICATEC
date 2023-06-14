#Para empezar, importamos el módulo random para generar números aleatorios. 
import random
class Loteria:
    def __init__(self,minimo,maximo):
        self.minimo=minimo
        self.maximo=maximo
    def jugar(self):
        ganador=random.randint(self.minimo, self.maximo)
        return ganador
class Usuario:
    def __init__(self,nombre):
        self.nombre=nombre
        self.boletos=[]
    def comprarBoleto(self,numero):
        if numero>=10 and numero<=20:
            self.boletos.append(numero)
            print(f"{self.nombre} compro correctamente el boleto {numero}")
        else:
            print("Error el boleto no se encuentra en el rango de 1000 a 2000")
    def mostrarBoleto(self):
        print(f"Boletos comprados por el usuario {self.nombre} : ")
        for boleto in self.boletos:
            print(boleto)
    def verificarGanador(self,ganador):
        for boleto in self.boletos:
            if boleto==ganador:
                print(f" {self.nombre} es el ganador, FELICITACIONES...")
                return True
            return False

loteria=Loteria(10,20)
usuarios=[]
while True:
    print("Loteria")
    print("1. Para agregra un usuario")
    print("2. Para comprar un boleto")
    print("3. Para iniciar el Juego")
    print("0. Para Salir")
    opcion=int(input("Seleccione una opcion: "))
    if opcion==1:
        nombre=input("Ingrese el nombre del usuario: ")
        usuario=Usuario(nombre)
        usuarios.append(usuario)
        print(f"{nombre} Fue agregado correctamente....")
    elif opcion==2:
        nombre_usuario=input("Ingrese su nombre de usuario: ")
        for usuario in usuarios:
            if usuario.nombre==nombre_usuario:
                numero_boleto=int(input("Ingrese el numero de su boleto a comprar: "))
                usuario.comprarBoleto(numero_boleto)
                break
            else:
                print("Usuario no registrado, realice el registro del usuario en la opcion 1")
    elif opcion==3:
        ganador=loteria.jugar()
        print(f"El numero ganador es... {ganador}")
        for usuario in usuarios:
            usuario.mostrarBoleto()
            if usuario.verificarGanador(ganador):
                break
            else:
                print("Ningun usuario compro el boleto ganador...")
    elif opcion==0:
        break
    else: 
        print("Opcion invalida verifique las opciones del menu e intente nuevamente")