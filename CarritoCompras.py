#Tienda Computadoras.
#Ejercicio 1 - Crear un carrito de compras- Utilizando clases y subclases.
#Clase Principal - Productos => Subclase - CarritoCompras => SubClase ProductoSeleccionado 
#Producto- NombreProducto, Precio, Descripcion
#ProductoSeleccionado- Marca, Año, Garantia
#CarritoCompras- ()
#PASO 1 - CREAR LA CLASE PRINCIPAL Y DEFINIR LOS ATRIBUTOS
class Producto:
    def __init__(self, NombreProducto, Precio, Descripcion):
        self.NombreProducto = NombreProducto
        self.Precio = Precio
        self.Descripcion = Descripcion

    def verInformacion(self):
        return f"Producto: {self.NombreProducto}, Precio: {self.Precio}Bs, Descripcion del Producto: {self.Descripcion}"


class ProductoSeleccionadoCelulares(Producto):
    def __init__(self, NombreProducto, Precio, Descripcion, Marca, Garantia, Camara):
        super().__init__(NombreProducto, Precio, Descripcion)
        self.Marca = Marca
        self.Garantia = Garantia
        self.Camara = Camara

    def Informacion(self):
        return f"{super().verInformacion()} - Garantia: {self.Garantia} años - Marca: {self.Marca}"


class ProductoSeleccionadoComputadoras(Producto):
    def __init__(self, NombreProducto, Precio, Descripcion, Garantias, Descuento):
        super().__init__(NombreProducto, Precio, Descripcion)
        self.Garantias = Garantias
        self.Descuento = Descuento

    def InforComputadora(self):
        return f"{super().verInformacion()} - Garantia: {self.Garantias} años - Descuento: {self.Descuento}"


class CarritoCompras:
    def __init__(self):
        self.productos = {}

    def agregarProducto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def estadoCarrito(self):
        print("Carrito de Compras")
        for producto, cantidad in self.productos.items():
            print(f"Nombre: {producto.NombreProducto} - Precio: {producto.Precio} - Cantidad: {cantidad}")

    def compraTotal(self):
        total = 0
        for producto, cantidad in self.productos.items():
            total += producto.Precio * cantidad
        return total


# Crear instancias de productos
producto1 = Producto("Produc1", 4550, "Como gama alta que es, el Galaxy S10 incorpora el último procesador Exynos, 8 GB de memoria RAM y una pantalla AMOLED Infinity-O con resolución 2K+, así como una triple cámara trasera.")
producto2 = Producto("Produ2", 6500, "Como gama alta que es, el Galaxy S10 incorpora el último procesador Exynos, 8 GB de memoria RAM y una pantalla AMOLED Infinity-O con resolución 2K+, así como una triple cámara trasera.")
producto3 = Producto("Produc3", 8550, "Como gama alta que es, el Galaxy S10 incorpora el último procesador Exynos, 8 GB de memoria RAM y una pantalla AMOLED Infinity-O con resolución 2K+, así como una triple cámara trasera.")

# Creación del carrito de compras
carrito = CarritoCompras()

# Agregar productos seleccionados al carrito de compras - de forma manual
carrito.agregarProducto(producto1, 2)
carrito.agregarProducto(producto3, 4)

# Mostrar el estado del carrito
carrito.estadoCarrito()

# Mostrar el total a pagar
total = carrito.compraTotal()
print(f"El total que debe cancelar es: {total}Bs")

