import random

class Loteria: 
    def __init__(self, minimo, maximo):
        self.minimo=minimo
        self.maximo=maximo
    def jugar(self):
        ganador=random.randint(self.minimo, self.maximo)
        return ganador
class usuario:
    def __init__(self, nombre):
        self.nombre=nombre
        self.boletos=[]
    def comprarboleto(self, numboleto):
        numboleto=int(input("ingrese el numero de su boleto"))
        if numboleto >1000 and numboleto <2000:
            print("compra exitosa"+self.jugar)
        else:
            print("error de compra")
    def mostrarboleto(self):
        if self.boletos >0:
            print("total de boletos comprados es: "+self.boletos)
        else:
            print("no se realizo ninguna compra")
    def verificarelganador(self):
        if self.ganador == self.boletos:
            print("felicidades")
        else:
            print("siga participando")
    def aggusuarios(self,nombre):
        aggusuarios={}
        self.nombre[aggusuarios]

loteria = Loteria(1000,2000)
usuario=[]
while true:
    print("***************************")
    print("***     menu            ***")
    print("*** 1.- usuario         ***")
    print("*** 2.- comprar         ***")
    print("*** 3.- jugar           ***")
    print("*** 0.- salir           ***")
    print("***************************")
    op=int(input("seleccione una de las opciones: "))
    if op ==1:
        input(print("ingrese el nombre de usuario: "))
        (print("agregado exitosamente"))
    elif op ==2:
        int(input("cuantos boletos desea comprar: "))
        print("compra exitosa")
    elif op==3:
        sorteo=int(input("ingrese el numero de boleto para participar: "))
        if sorteo == ganador:
            print("felicidades usted es el ganador")
            break
        else:
            print("lo sentimos mucho, siga participando")
            break
    elif op==0:
        print("Que tenga buen dia hasta luego...")
        break
    else:
        print("error, siga jugando a la loteria..!!")
    
