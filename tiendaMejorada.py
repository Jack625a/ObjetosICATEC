#crear clase para tienda
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos=[]
        self.precios=[]
    def agregar_productos(self,producto):
        self.productos.append(producto)

    #metodo mostrar lso productos
    def filtrar_productos(self,nombre):
        print("Productos Disponibles Tienda",self.nombre)
        for producto in self.productos:
            if producto.nombre==nombre:
                return producto
        return None
    
    def mostrar_productos(self):
        print("productos disponibles en la tienda",self.nombre)
        for producto  in self.productos:
            return producto
#clase para realizar multiples busquedas
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    

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
        productoAgregado=Producto(producto1,precio1)
        tienda.agregar_productos(productoAgregado)
    else:
        totalProductos=tienda.mostrar_productos()
        print(f"Producto: '{totalProductos.nombre}'- Precio: {totalProductos.precio} Bs")
        break


#Bucle para el filtrado de los productos
while True:
    print("Seleccionar un opcion para la busqueda del producto")
    nombreProducto=input("Ingrese el producto que desea buscar ó ingrese Salir para finalizar:  ")
    if nombreProducto=="Salir":
        print("Gracias por comprar en la tienda...")
        break
    productoEncontrado=tienda.filtrar_productos(nombreProducto)
    if productoEncontrado:
        print(f"El producto:'{productoEncontrado.nombre}' fue encontrado correctamente. Precio: {productoEncontrado.precio} Bs")
    else:
        print("El producto no esta disponible en la tienda")

