#Ejercicio 1- Crear una clase para una tienda de barrio
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos={}
    #definir los metodos o acciones
    def agregar_productos(self,producto,precio):
        self.productos[producto]=precio
    #metodo mostrar los productos
    def mostrar_productos(self):
        print("Productos disponibles en la tienda de barrio",self.nombre)
        for producto, precio in self.productos.items():
            print("Producto:",producto," - ","Precio: ",precio,"Bs")

#Crear los objetos de la clase Tienda de Barrio
tienda=Tienda("Tienda de barrio Doña Esperanza",451255656,"6 de octubre y bolivar #785")
#Agregar productos de forma dinamica - se ingres por teclado
#CREAR UN BUCLE REPETITIVO PARA AGREGAR MAS PRODUCTOS A LA TIENDA
#poner 2 opciones- 1 Continuar Agregando 2 Salir
while True:
    print("Desea seguir agregando productos a la tienda")
    opciones=int(input("1. Continuar Agregando - 2. Salir"))
    if opciones==1:
        producto1=input("Ingrese el nombre del producto: ")
        precio1=float(input("Ingrese el precio del producto: "))
        tienda.agregar_productos(producto1,precio1)
    else:
        tienda.mostrar_productos()
        break

#Agregar los productos a la tienda 
tienda.agregar_productos("Pan",0.50)
tienda.agregar_productos("Pepsi",9)
tienda.agregar_productos("Harina",10)
tienda.agregar_productos("Queso",5)
tienda.agregar_productos("Aceite",15)
tienda.agregar_productos("Coca Cola",10)

#Mostrar los productos de la tienda


#CREAR UN BUCLE REPETITIVO PARA AGREGAR MAS PRODUCTOS A LA TIENDA
#poner 2 opciones- 1 Continuar Agregando 2 Salir

