#crear clase para tienda
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos={}
    def agregar_productos(self,producto,precio):
        self.productos[producto]=precio
    #metodo mostrar lso productos
    def mostrar_productos(self):
        print("Productos Disponibles Tienda",self.nombre)
        for producto, precio in self.productos.items():
            print("Producto:",producto,"-","Precio: ",precio,"Bs")
#crear los objetos de la clase
tienda=Tienda("Tienda Veloz",123456,"6 de octubre y bolivar")

#agregar productos por teclado
#opciones- 1 Continuar Agregando 2 Salir
while True:
    print("Desea seguir agregando productos a la tienda")
    opciones=int(input("1 Agregar -- 2 Salir: "))
    if opciones==1:
        producto1=input("Ingrese el nombre del producto: ")
        precio1=float(input("Ingrese el precio del producto: "))
        tienda.agregar_productos(producto1,precio1)
    else:
        tienda.mostrar_productos()
        break

#while opciones!=2

#agregar productos a la tienda
tienda.agregar_productos("Pan",0.50)
tienda.agregar_productos("Pepsi",9)
tienda.agregar_productos("Harina",10)
tienda.agregar_productos("Queso",5)
tienda.agregar_productos("Aceite",15)
tienda.agregar_productos("Coca Cola",10)

#mostrar productos de la tienda
tienda.mostrar_productos()