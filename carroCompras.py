#tienda computadoras
#1 crear carrito de compras clases y subclases
#clase principal PRODUCTOS  sub clase CARRITOcompras
#producto, nomProducto, precio, descripcion
#paso 1 crear la clase principal y los atributos
class Producto:
    def __init__(self,nomProducto, precio, descrip):
        self.nomProducto=nomProducto
        self.precio=precio
        self.descrip=descrip
#pas2 crear las acciones o metodos de la clase
    def verInformacion(self):
        return f"{self.nomProducto}-precio:{self.precio}Bs descripcion Producto:{self.descrip}"
#ejemplo  funcionamiento clase
#producto1=Producto("producto 1",4550,"laptop 8 ram 256gb ssd ryzen 5")
#print(producto1.verInformacion())
class ProductoSeleccionado(Producto):
    def __init__(self,nomProducto, precio, descrip,marca,año,garantia,camara):
        super().__init__(nomProducto,precio,descrip)
        self.marca=marca
        self.garantia=garantia
        self.camara=camara
    def informacion(self):
        return f"super().verInformacion()-garantia:{self.garantia} años-marca:{self.marca}"
class ProductosSeleccionadosComputadoras(Producto):
    def __init__(self,nomProducto,precio,descrip,garantia,descuento):
        super().__init__(nomProducto,precio,descrip)
        self.garantia=garantia
        self.descuento=descuento
    def inforComputadora(self):
        return f"super().verInformacion()-garantia:{self.garantia}años-descuento:{self.descuento}"
class CarritoCompras:
    def __init__(self):
        self.productos={}
        #definir las acciones del carrito
        def agregarProducto(self,producto,cantidad):
            





















