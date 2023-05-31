#clase tienda de barrio
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos={}
    #definir metodos o acciones
    def agregar_productos(self,producto,precio):
        self.productos[producto]=precio
    #metodo de mostrar los productos
    def mostrar_productos(self):
        print("productos disponibles en la tienda de barrio",self.nombre)
        for producto, precio in self.productos.items():
            print("el producto: ",producto," - ", "precio: ",precio,"bs")
        
#nombre de la tienda
tienda=Tienda("tienda de barrio la tia pelos",731776037,"corneta mamani entre 6 de octubre y potosi")
#agregar productos por teclado
print("desea seguir agregando productos ")
opciones=int(input("1.- continuar agregando - 2.- salir : "))
while True:
    if opciones==1:
        producto1=input("ingrese el nombre del producto: ")
        precio1=float(input("ingrese el precio del producto: "))
        tienda.agregar_productos(producto1,precio1)
    else:
        tienda.mostrar_productos()
        break
    
#agregar los productos de la tienda
tienda.agregar_productos("pan",0.50)
tienda.agregar_productos("coca cola",15)
tienda.agregar_productos("manyequilla",5)
tienda.agregar_productos("huevo",1.20)
tienda.agregar_productos("aceite",10)
#mostrar los productos de la tienda
tienda.mostrar_productos()
#crear bucle para agregar

