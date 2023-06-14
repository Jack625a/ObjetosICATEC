import random

class Loteria:
    def __init__(self, minimo, maximo):
        self.minimo = minimo
        self.maximo = maximo

    def jugar(self):
        resultado = random.randint(self.minimo, self.maximo)
        return resultado


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.boletos = []

    def comprarBoleto(self, numero):
        if numero >= 1000 and numero <= 5000:
            self.boletos.append(numero)
            print(f"¡{self.nombre} ha comprado el boleto {numero}!")
        else:
            print("El número de boleto debe estar en el rango del 1000 al 5000.")

    def mostrarBoletos(self):
        print(f"Boletos de {self.nombre}:")
        for boleto in self.boletos:
            print(boleto)

    def verificarGanador(self, resultado):
        for boleto in self.boletos:
            if boleto == resultado:
                print(f"¡Felicidades, {self.nombre}! Has ganado con el boleto {boleto}.")
                return True
        return False


loteria = Loteria(1000, 5000)
usuarios = []

while True:
    opcion = input("¿Desea agregar un usuario, comprar un boleto o jugar a la lotería? (1: Usuario / 2: Comprar / 3: Jugar / 0: Salir): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = Usuario(nombre)
        usuarios.append(usuario)
        print(f"Usuario {nombre} agregado exitosamente!")

    elif opcion == "2":
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        for usuario in usuarios:
            if usuario.nombre == nombre_usuario:
                numero_boleto = int(input("Ingrese el número de boleto a comprar: "))
                usuario.comprarBoleto(numero_boleto)
                break
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        resultado = loteria.jugar()
        print("¡El resultado del sorteo es:", resultado, "!")
        for usuario in usuarios:
            usuario.mostrarBoletos()
            if usuario.verificarGanador(resultado):
                break
        else:
            print("Ningún usuario ha ganado.")

    elif opcion == "0":
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
