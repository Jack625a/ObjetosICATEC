#eJERCICIO 1 - VALIDACION DE DATOS
#REALIZAR UN PROGRAMA QUE EJECUTE LA VENTA DE UN PRODUCTO Y PROPOCIONE TIPOS DE ENVIO COON DIFERENTES PRECIOS
from tkinter import *
from tkinter import ttk
#Envio:
#1. Auto
#2. Moto
#3. Bicicleta
#CALCULO DE EL PRODUCTO EN BASE A EL TIPO DE ENVIO
class Aplicacion():
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Tienda CATEC")

        #Definir la variables de control
        self.precio=DoubleVar(value=0.0)
        self.total=DoubleVar(value=0.0)
        self.envio=StringVar(value="")
        self.cantidad=IntVar(value=1)

        logo=PhotoImage(file='1.png')

        #Declarion de los objetos de la ventana
        self.imagen1=Label(self.ventana,image=logo,anchor="center")
        self.producto=Label(self.ventana,text="Producto 1")
        self.textoCantidad=Label(self.ventana,text="Cantidad")
        self.cantidad=SpinBox(self.ventana, from_=1, to=30, wrap=True, textvariable=self.cantidad, state='readonly')
        self.TextEnvio=Label(self.ventana,text="Tipo de Envio")
        self.envio1=RadioBox(self.ventana,text="AUTO", variable=self.envio, value="A")
        self.envio2=RadioBox(self.ventana,text="MOTO", variable=self.envio, value="M")
        self.envio3=RadioBox(self.ventana,text="BICI", variable=self.envio, value="B")
        self.textPrecio=Label(self.ventana, text="Precio: ")
        self.Precio=Entry(self.ventana, textvariable=self.precio, width=12)
        self.textTotal=Label(self.ventana, text="Costo Total: ")
        self.Total=Label(self.ventana,textvariable=self.total, bg="black", fg="white")
        self.boton=Button(self.ventana,text="Comprar",command=self.calcular())

        #Definir la posiciones de los componentes
        self.imagen1.pack()
        self.producto.pack()
        self.textoCantidad.pack()
        self.cantidad.pack()
        self.TextEnvio.pack()
        self.envio1.pack()
        self.envio2.pack()
        self.envio3.pack()
        self.textPrecio=Label(self.ventana, text="Precio: ")
        self.Precio=Entry(self.ventana, textvariable=self.precio, width=12)
        self.textTotal=Label(self.ventana, text="Costo Total: ")
        self.Total=Label(self.ventana,textvariable=self.total, bg="black", fg="white")
        self.boton=Button(self.ventana,text="Comprar",command=self.calcular())

