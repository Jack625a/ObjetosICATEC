#ejercicio 1- crear un carrito de compras utilizando clases y sub-clases
#clase principal de una tienda en linea - productos , sub clase - carrito compras
#producto - nombreproducto, precio, descripcion
#producto seleccionado - marca de producto, año y garantia
#carrito de compras - ()
#paso 1 - crear la clase principal y definir atributos
class Producto:
    def __init__(self, nombreproducto, precio, descripcion):
        self.nombreproducto=nombreproducto
        self.precio=precio
        self.descripcion=descripcion
#paso 2 - crear las acciones o metodos de clase   
    def verinformacion(self):
        return f"{self.nombreproducto} - precio: {self.precio}bs - descripcion del producto: {self.descripcion} "
    
#
#producto1=Producto("producto 1",1499,"el producto es chingon xD")
class Productoseleccionadocelulares(Producto):
    def __init__(self, nombreproducto, precio, descripcion, marca, camara, garantia):
        super().__init__(nombreproducto, precio, descripcion)
        self.marca=marca
        self.garantia=garantia
        self.camara=camara
    def informacion(self):
        return f"super().verinformacion() - garantia: {self.garantia} años - marca: {self.marca} - camara: {self.camara}"

class productoseleccionadocomputadoras(Producto):
    def __init__(self, nombreproducto, precio, descripcion, descuento, garantias):
        super().__init__(nombreproducto, precio, descripcion)
        self.garantias=garantias
        self.descuento=descuento
    def infocomputadora(self):
        return f"super().verinformacion() - garantia: {self.garantias} años - descuento: {self.descuento} "

class carritocompras(Producto):
    def __init__(self, nombreproducto, precio, descripcion):
        super().__init__(nombreproducto, precio, descripcion)
        self.productos={}
    #definir las acciones del carrito
    def agregarproducto(self, producto,cantidad):
        if producto.nombreproducto in self.productos:
            self.productos[producto.nombreproducto]+=cantidad
        else:
            self.productos[producto.nombreproducto]=cantidad
    def estadocarrito(self):
        print("carrito de compras ")
        for producto, cantidad in self.productos.items():
            print(f"{producto} - cantidad: {cantidad}")
    
    def compratotal(self):
        total=0
        for producto, cantidad in self.productos.items():
            total+=producto.precio *cantidad
        return total

#paso 3 crear los objetos
producto1=Producto("producto 1",1499,"el producto es chingon xD")
producto2=Producto("producto 2",4499,"el producto es mas chingon que el primero xD")
producto3=Producto("producto 3",2339,"el producto no es chingon, lo siento brow xD")
#creacion del carrito de compras
carrito=carritocompras("",0,"")
#agregar el producto seleccionado al carrito de compras
carrito.agregarproducto(producto1,2)
carrito.agregarproducto(producto3,4)
#mostrar el estado del carrito
carrito.estadocarrito()
#mostrar el totol de compras
total=carrito.compratotal()
print(f"el total que debe cancelar es: {total} bs")