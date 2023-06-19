#eJERCICIO 1 - VALIDACION DE DATOS
#REALIZAR UN PROGRAMA QUE EJECUTE LA VENTA DE UN PRODUCTO Y PROPOCIONE TIPOS DE ENVIO COON DIFERENTES PRECIOS
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
#Envio:
#1. Auto=15
#2. Moto=10
#3. Bicicleta=8
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

        #Definir la imagen del producto:
        self.imagen=Image.open("1.png")
        self.imagen=self.imagen.resize((200,200))
        self.imagen=ImageTk.PhotoImage(self.imagen)

    
        #Declarion de los objetos de la ventana
        self.imagen1=Label(self.ventana,image=self.imagen)
        self.producto=Label(self.ventana,text="Producto 1")
        self.textoCantidad=Label(self.ventana,text="Cantidad")
        self.cantidadSeleccion=Spinbox(self.ventana, from_=1, to=30, wrap=True, textvariable=self.cantidad, state='readonly')
        self.TextEnvio=Label(self.ventana,text="Tipo de Envio")
        self.envio1=Radiobutton(self.ventana,text="AUTO", variable=self.envio, value="A")
        self.envio2=Radiobutton(self.ventana,text="MOTO", variable=self.envio, value="M")
        self.envio3=Radiobutton(self.ventana,text="BICI", variable=self.envio, value="B")
        self.textPrecio=Label(self.ventana, text="Precio: ")
        self.Precio=Entry(self.ventana, textvariable=self.precio, width=12)
        self.textTotal=Label(self.ventana, text="Costo Total: ")
        self.Total=Label(self.ventana,textvariable=self.total, bg="black", fg="white")
        self.boton=Button(self.ventana,text="Comprar",command=self.calcular())

        #Definir la posiciones de los componentes
        self.imagen1.pack()
        self.producto.pack()
        self.textoCantidad.pack()
        self.cantidadSeleccion.pack()
        self.TextEnvio.pack()
        self.envio1.pack()
        self.envio2.pack()
        self.envio3.pack()
        self.textPrecio.pack()
        self.Precio.pack()
        self.textTotal.pack()
        self.Total.pack()
        self.boton.pack()

        self.ventana.mainloop()
    
    #Definir las acciones o metodos de la clase
    def calcular(self):
        #Realizar el calculo del costo Total
        #Obtener el precio del producto
        precio_producto=self.precio.get()
        #Obtener el tipo de envio seleccionado por el usuario
        tipo_envio=self.envio.get()
        #Obtener la cantidad de producto seleccionado
        cantidad_productos=self.cantidad.get()
        #calculo del total inicial
        costo_total=precio_producto*cantidad_productos

        #Aplicar el costo del envio envase a la seleccion del usuario
        if tipo_envio == "A":
            costo_total+=15
        elif tipo_envio== "M":
            costo_total+=10
        elif tipo_envio== "B":
            costo_total+=8
        #Actualizar el costo total
        self.total.set(costo_total)

#Crear el objeto de la clase
app=Aplicacion()

