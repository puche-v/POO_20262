import math
class Operaciones:
    def __init__(self, suma, x, y):
        self.suma = suma
        self.x = x
        self.y = y

    def sumar(self):
        return self.suma + self.x

    def calcularx(self):
        return self.x + math.pow(self.y, 2)

    def sumafinal(self):
        return self.suma + (self.x/self.y)

suma = float(input("Ingrese cuanto vale la suma: "))
x = float(input("Ingrese cuanto vale X: "))
y = float(input("Ingrese cuanto vale Y: "))
ops = Operaciones(suma, x, y)

print(f"El valor de la suma es: {ops.sumafinal()}")


