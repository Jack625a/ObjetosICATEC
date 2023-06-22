#eJERCICIO 1 - VALIDACION DE DATOS
#REALIZAR UN PROGRAMA QUE EJECUTE LA VENTA DE UN PRODUCTO Y PROPOCIONE TIPOS DE ENVIO COON DIFERENTES PRECIOS
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
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

        #lISTA DE PRODUCTOS
        self.productos=[
            {"nombre":"Producto1","precio":25,"imagen":"7.jpg"},
            {"nombre":"Producto2","precio":35,"imagen":"2.jpg"},
            {"nombre":"Producto3","precio":55,"imagen":"3.jpg"},
            {"nombre":"Producto4","precio":15,"imagen":"4.jpg"},
            {"nombre":"Producto5","precio":82,"imagen":"5.jpg"},
            {"nombre":"Producto6","precio":250,"imagen":"6.jpg"}

        ]
        self.productos_seleccion=self.productos[0]
           
        #Declarion de los objetos de la ventana
        self.imagenProducto=Label(self.ventana,image=None)
        self.ProductosTienda=ttk.Combobox(self.ventana, values=[producto["nombre"]
            for producto in self.productos
        ], state="readonly", font=("Arial",16))
        self.ProductosTienda.current(0)
        #Actulizador de seleccion blind - ComboboxSelected
        self.ProductosTienda.bind("<<ComboboxSelected>>",self.actualizar_producto)

        #self.producto=Label(self.ventana,text="Producto 1")
        self.textoCantidad=Label(self.ventana,text="Cantidad")
        self.cantidadSeleccion=Spinbox(self.ventana, from_=1, to=30, wrap=True, textvariable=self.cantidad, state='readonly')
        self.TextEnvio=Label(self.ventana,text="Tipo de Envio")
        self.envio1=Radiobutton(self.ventana,text="AUTO", variable=self.envio, value="A", font=("Happy Monnkey",16))
        self.envio2=Radiobutton(self.ventana,text="MOTO", variable=self.envio, value="M",font=("Happy Monnkey",16))
        self.envio3=Radiobutton(self.ventana,text="BICI", variable=self.envio, value="B",font=("Happy Monnkey",16))
        self.textPrecio=Label(self.ventana, text="Precio: ")
        self.Precio=Entry(
            self.ventana, #VEntana donde se agrega el componente
            textvariable=self.productos_seleccion["precio"], #dato obtenido para la varibale
            width=12
            )
        self.textTotal=Label(self.ventana, text="Costo Total: ")
        self.Total=Label(self.ventana,textvariable=self.total, bg="black", fg="white")
        self.boton=Button(self.ventana,text="Comprar",command=self.calcular)

        #actulizacion de la Imagen con respecto al producto seleccionado
        self.actulizar_imagen()

        #Definir la posiciones de los componentes
        self.imagenProducto.pack()
        self.ProductosTienda.pack()
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

        #self.ventana.mainloop()
    
    #Definir las acciones o metodos de la clase
    #Metodo para actulizar el Producto con respecto a la seleccion
    def actualizar_producto(self, event):
        nombre_producto=self.ProductosTienda.get()
        for producto in self.productos:
            if producto["nombre"]==nombre_producto:
                self.productos_seleccion=producto
                self.Precio.delete(0,END)
                self.Precio.insert(0, str(producto["precio"]))
                self.actulizar_imagen()

    def actulizar_imagen(self):
        ruta_imagen=self.productos_seleccion["imagen"]
        #Definir el tamaño de la imagen
        imagen=Image.open(ruta_imagen)
        imagen=imagen.resize((200,200))
        imagen=ImageTk.PhotoImage(imagen)
        self.imagenProducto.configure(image=imagen)
        self.imagenProducto.image=imagen

    def calcular(self):
        #Realizar el calculo del costo Total
        #Obtener el precio del producto
        precio_producto=self.productos_seleccion["precio"]
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

        #Mostrar nuestra notificacion de la compra realizada
        mensaje=f"Precio Total: {costo_total} Bs"
        messagebox.showinfo("Compra Exitosa ",mensaje)

#Crear el objeto de la clase
app=Aplicacion()
app.ventana.mainloop()