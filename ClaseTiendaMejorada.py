#Ejercicio 1- Crear una clase para una tienda de barrio
class Tienda:
    def __init__(self,nombre,nit,direccion):
        self.nombre=nombre
        self.nit=nit
        self.direccion=direccion
        self.productos=[]
        #self.precios=[]
    #definir los metodos o acciones
    def agregar_productos(self,producto):
        self.productos.append(producto)
        #self.precios.append(precio)
    #metodo mostrar los productos
    def filtrar_productos(self,nombre):
        print("Productos disponibles en la tienda de barrio",self.nombre)
        for producto in self.productos:
            if producto.nombre==nombre:
                return producto
        return None
    def mostrar_productos(self):
        print("Productos disponibles en la tienda de barrio",self.nombre)
        for producto in self.productos:
            return producto
#Clase para permitir al usuario realizar multiples busquedas en la tienda
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

#Crear los objetos de la clase Tienda de Barrio
tienda=Tienda("Tienda de barrio Doña Esperanza",451255656,"6 de octubre y bolivar #785")
#Agregar productos de forma dinamica - se ingres por teclado
#CREAR UN BUCLE REPETITIVO PARA AGREGAR MAS PRODUCTOS A LA TIENDA
#poner 2 opciones- 1 Continuar Agregando 2 Salir
while True:
    print("Desea seguir agregando productos a la tienda")
    opciones=int(input("1. Continuar Agregando - 2. Salir: "))
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
        print("Gracias por comprar en la tienda de barrio Esperanza...")
        break
    productoEncontrado=tienda.filtrar_productos(nombreProducto)
    if productoEncontrado:
        print(f"El producto:'{productoEncontrado.nombre}' fue encontrado correctamente. Precio: {productoEncontrado.precio} Bs")
    else:
        print("El producto no esta disponible en la tienda")