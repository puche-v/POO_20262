class Carro:
    def __init__(self, marca, modelo, motor, anio ,npuertas, cantasients, velmax, color, velact):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.anio = anio
        self.npuertas = npuertas
        self.cantasients = cantasients
        self.velmax = velmax
        self.color = color
        self.velact = velact
    def acelerar(self, incrementarv):
        if self.velact + incvel <= self.velmax:
            self.velact += incvel
        else:
            print("No se puede acelerar más de la velocidad maxima")
    def desacelear(self, disminuirv):
        if self.velact + incvel <= self.velmax:
            self.velact -= incvel
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
        print(f"Color: {self.color}")
        print(f"Velocidad actual: {self.velact}")

marca = input("Ingrese la marca del carro: ")
modelo = input("Ingrese el modelo del carro: ")
motor = input("Ingrese el tipo de motor del carro: ")
anio = int(input("Ingrese el año del carro: "))
npuertas = int(input("Ingrese el número de puertas del carro: "))
cantasients = int(input("Ingrese la cantidad de asientos del carro: "))
velmax = float(input("Ingrese la velocidad máxima del carro: "))
color = input("Ingrese el color del carro: ")
velact = float(input("Ingrese la velocidad actual del carro: "))
carro = Carro(marca, modelo, motor, anio, npuertas, cantasients, velmax, color, velact)
carro.carrito()
