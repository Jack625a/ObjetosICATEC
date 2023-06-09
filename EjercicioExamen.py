#Ejercicio Simulacro EXAMEN
#Crear una clase para la instalacion de un cajero automatico
#Clases, Bucles, Condicionales, Entrada de datos inputs, Diccionarios o Listas
#Paso 1: Determinar los atributos, metodos de la clase
#Definir el nombre de clase: class Cajero
#Metodo 1: Agregar Cuenta de los usuarios => Atributos: numero_cuenta,saldo,usuario
#Metodo 2: Consultar el saldo =>numero_cuenta
#Metodo 3: Depositar dinero a la cuenta=> numero_cuenta, monto a depositar
#Metodo 4: Retirar dinero de la cuenta=>numero_cuenta, monto a retirar
class CajeroAutomatico:
    def __init__(self):
        self.cuentas={}
    def agregarCuenta(self,numero_cuenta,saldo,usuario):
        self.cuentas[numero_cuenta]=saldo

    def consultarSaldo(self,numero_cuenta):
        if numero_cuenta in self.cuentas:
            return self.cuentas[numero_cuenta]
        else: 
            return "Error numero de cuenta invalido"
    def depositar(self,numero_cuenta,monto):
        if numero_cuenta in self.cuentas:
            self.cuentas[numero_cuenta]+=monto
            return "Deposito fue realizado correctamente"
            
        else:
            return "Error numero de cuenta invalido"
    def retirar(self,numero_cuenta,monto):
        if numero_cuenta in self.cuentas:
            saldo_actual=self.cuentas[numero_cuenta]
            if saldo_actual>=monto:
                self.cuentas[numero_cuenta]-=monto
                return "Retiro de dinero fue procesado"
            else:
                return "Saldo insuficiente para continuar con el retiro"
        else:
            return "Error numero de cuenta invalido"


#Paso 2. Creacion de los objetos
cajero1=CajeroAutomatico()
cajero2=CajeroAutomatico()
cajero3=CajeroAutomatico()
#Paso 3. Agregar las instancias a los objetos
#Agregar usuarios a la base de datos del Cajero => Diccionario
#CASO 1 - AGREGAR USUARIOS DE FORMA MANUAL
cajero1.agregarCuenta("123456789",5000,"Kevin Arroyo")
cajero1.agregarCuenta("789456123",6000,"Romer Nina")
cajero1.agregarCuenta("741852963",6500,"Ramiro Ayaviri")
cajero1.agregarCuenta("258963147",9500,"Nayeli Vargas")
cajero1.agregarCuenta("123987456",8800,"Yeltsin Ancachi")

#Paso 4. Creacion de la instancia Principal
while True:
    print("Bienvenido al Cajero Automatico CATEC")
    numero_cuenta=input("Ingrese su numero de cuenta: ")
    if numero_cuenta in cajero1.cuentas:
        print("Seleccione la opcion que desea realizar: ")
        print("1. Consultar Saldo")
        print("2. Depositar en la Cuenta")
        print("3. Retirar de la cuenta")
        opcion=int(input("> "))
        if opcion==1:
            saldo=cajero1.consultarSaldo(numero_cuenta)
            print(f"Saldo Diponible en la cuenta es {saldo}Bs")
        elif opcion==2:
            monto=int(input("Ingrese el monto a Depositar: "))
            deposito=cajero1.depositar(numero_cuenta,monto)
            print(deposito)
            saldoTotal=cajero1.consultarSaldo(numero_cuenta)
            print(f"El saldo total en la cuenta es {saldoTotal}Bs")
        elif opcion==3:
            monto=int(input("Ingrese el monto a Retirar: "))
            retiro=cajero1.retirar(numero_cuenta,monto)
            print(retiro)
            saldoTotal=cajero1.consultarSaldo(numero_cuenta)
            print(f"El saldo total en la cuenta es {saldoTotal}Bs")
        else:
            print("Error opción no valida")
    else:
        print("Cuenta no valida")
    
    continuar=input("Desea realizar alguna operacion adicional? Si para continuar, No para Salir:> ")
    if continuar!='Si':
        break







#CASO 2 . AGREGAR USUARIOS DE FORMA AUTOMATICA