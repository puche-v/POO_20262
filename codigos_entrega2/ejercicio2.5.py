class CuentaBanco:
    def __init__(self, nombre, apells, num, tipocuenta, saldo):
        self.nombre = nombre
        self.apells = apells
        self.num = num
        self.tipocuenta = tipocuenta
        self.saldo = saldo

    def tipocuenta(self):
        if tipocuenta == 1:
            return "Ahorros"
        elif tipocuenta == 2:
            return "Corriente"

    def cuenta(self):
        print(f"Titular: {self.nombre} {self.apells}")
        print(f"Numero de cuenta: {self.num}")
        print(f"Tipo de cuenta: {self.tipocuenta}")
        print(f"Saldo: {self.saldo}")
    
    def consignar(self, consignacion):
        self.consignacion = consignacion
        if consignacion <= 0:
            print("Error al consignar")
        else: 
            self.saldo = self.saldo + consignacion
            print(f"Consignacion exitosa, se han consignado {consignacion} pesos")

    def retirar(self, monto):
        self.monto = monto
        if monto > self.saldo:
            print("Fondos insuficientes para retirar")
        else: 
            self.saldo = self.saldo - monto
            print(f"Retiro exitoso, se han retirado {monto} pesos")

Cuenta1 = CuentaBanco("Juanito", "Diez Miranda", 4040222167, 1, 0)
x = 0
while x != 5:
    x = int(input("""Seleccione la operación a realizar:
        1- Consultar cuenta
        2- Consignar
        3- Retirar
        4- Modificar cuenta
        5- salir
    """))
    if x == 1:
        Cuenta1.cuenta()
        
    elif x == 2:
        consignacion = int(input("Ingrese la cantidad a consignar: "))
        Cuenta1.consignar(consignacion)
        
    elif x == 3:
        monto = int(input("Ingrese el monto a retirar: "))
        Cuenta1.retirar(monto)
        
    elif x == 4:
        y = int(input("""Ingrese que dato quiere modificar
        1- Nombre del titular
        2- Apellidos del titular
        3- Tipo de cuenta

        """))
        if y == 1:
            Cuenta1.nombre = input("Ingrese el nuevo nombre: ")
            
        elif y == 2:
            Cuenta1.apells = input("Ingrese los nuevos apellidos: ")
            
        elif y == 3:
            Cuenta1.tipocuenta = int(input("""Ingrese el nuevo tipo de cuenta
            1- Ahorros
            2- Corriente

            """))
            
    elif x == 5:
        break