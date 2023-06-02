#clase tienda de barrio
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos=[]
        self.precios=[]
    #definir metodos o acciones
    def agregar_productos(self,producto,precio):
        self.productos.append(producto)
        self.precios.append(precio)
    #metodo de mostrar los productos
    def filtrar_productos(self,nom):
        print("productos disponibles en la tienda de barrio",self.nombre)
        for producto in self.productos:
            if producto.nom==nom:
                return producto
        return None
    def mostrar_productos(self):
        print("productos disponibles en la tienda son: ",self.nombre)
        for producto in self.productos:
            print("el productos: ",producto," - ", "precio: ",precio,"bs")
    
#clase
print("desea seguir agregando productos ")
opciones=int(input("1.- continuar agregando - 2.- salir : "))
while True:
    if opciones==1:
        producto1=input("ingrese el nombre del producto: ")
        precio1=float(input("ingrese el precio del producto: "))

        Tienda.agregar_productos(producto1,precio1)
    else:
        Tienda.mostrar_productos()
        break

