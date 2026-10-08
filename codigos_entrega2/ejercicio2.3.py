from enum import Enum

class Tipocarro(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class Tipocom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GASNATURAL = "GASNATURAL"

class Color(Enum):
    ROJO = "ROJO"
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    VIOLETA = "VIOLETA"
    AZUL = "AZUL"

class Carro:
    def __init__(self, marca, modelo, motor, anio ,npuertas, cantasients, velmax, velact, color, tipo, tipocomb, automatico, multas):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.anio = anio
        self.npuertas = npuertas
        self.cantasients = cantasients
        self.velmax = velmax
        self.velact = velact
        self.color = color
        self.tipo = tipo
        self.tipocomb = tipocomb
        self.automatico = automatico
        self.multas = multas

    def acelerar(self, incrementarv:int):
        if incrementarv <= 0:
            print("El incremento debe ser mayor que 0")
        elif self.velact + incrementarv <= self.velmax:
            self.velact += incrementarv
        else:
            print("No se puede acelerar más de la velocidad maxima")
            self.multas += 1

    def desacelear(self, disminuirv:int):
        if disminuirv <= 0:
            print("La disminución debe ser mayor que 0")
        elif self.velact + disminuirv >= 0:
            self.velact -= incrementarv
        else:
            print("No se puede desacelerar más de la velocidad minima")
    
    def frenar(self):
        self.velact = 0

    def carrito(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor}")
        print(f"Año: {self.anio}")
        print(f"Número de puertas: {self.npuertas}")
        print(f"Cantidad de asientos: {self.cantasients}")
        print(f"Velocidad máxima: {self.velmax}")
        print(f"Velocidad actual: {self.velact}")
        print(f"Color: {self.color.value}")
        print(f"Tipo de carro: {self.tipo.value}")
        print(f"Tipo de combusitble: {self.tipocomb.value}")
        print(f"Es autoamtico: {self.automatico}")
        print(f"La velocidad actual es: {velact}")
        print(f"Cantidad de multas: {self.multas}")
    def mostrarmultas(self):
        print(f"Cantidad de multas luego de acelerar o desacelerar: {self.multas}")

marca = input("Ingrese la marca del carro: ")
modelo = input("Ingrese el modelo del carro: ")
motor = input("Ingrese el tipo de motor del carro: ")
anio = int(input("Ingrese el año del carro: "))
npuertas = int(input("Ingrese el número de puertas del carro: "))
cantasients = int(input("Ingrese la cantidad de asientos del carro: "))
velact = float(input("Ingrese la velocidad actual del carro: "))
velmax = 120
automatico = input("Es automatico: ")
color = Color.ROJO
tipo = Tipocarro.FAMILIAR
tipocomb = Tipocom.BIODIESEL
multas = 0

carro = Carro(marca, modelo, motor, anio, npuertas, cantasients, velmax, velact, color, tipo, tipocomb, automatico, multas)
carro.carrito()

incrementarv = 20
disminuirv = 30
carro.acelerar(incrementarv)
print(f"Velocidad después de acelerar {incrementarv}: {carro.velact}")
carro.desacelear(disminuirv)
print(f"Velocidad después de desacelerar {disminuirv}: {carro.velact}")
carro.mostrarmultas()