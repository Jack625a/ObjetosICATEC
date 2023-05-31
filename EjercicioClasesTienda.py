#Ejercicio 1 - CREAR UNA CLASE PARA UNA TIENDA DE BARRIO
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos={}
    #Definir las acciones o metodos
    def agregar_productos(self,producto,precio):
        self.productos[producto]=precio
    #Metodo para mostrar los productos
    def mostrar_productos(self):
        print("Productos Disponibles en la Tienda de Barrio",self.nombre)
        for producto, precio in self.productos.items():
            print("El producto: ",producto,"Precio",precio)

#Crear los objetos de la clase Tienda de Barrio
tienda=Tienda("Tienda de barrio Doña Esperanza",421454,"6 de octubre y bolivar # 181")

#Agregar productos de fomra dinamica es decir que se ingrese por teclado

while True:
    print("Desea seguir agregando productos a la tienda?")
    opciones=int(input("1. Continuar Agregando - 2. Para salir"))
    if opciones==1:
        producto1=input("Ingrese el nombre del producto: ")
        precio1=float(input("Ingrese el precio del producto: "))
        tienda.agregar_productos(producto1,precio1)
        
    else:
        tienda.mostrar_productos()
        break
#Agregar los productos a la tienda
tienda.agregar_productos("Pan",0.50)
tienda.agregar_productos("Pepsi",10)
tienda.agregar_productos("Coca Cola",13)
tienda.agregar_productos("Queso",5)
tienda.agregar_productos("Harina",10)
tienda.agregar_productos("Aceite",15)

#Mostrar 
tienda.mostrar_productos()

#CREAR UN BUCLE REPETITIVO PARA AGREGAR MAS PRODUCTOS A LA TIENDA
#Poner 2 opciones . 1 Continuar Agregando 
