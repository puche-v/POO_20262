import math
class Operacion:
    def __init__(self, x):
        self.x = x
    def cuadrado(self):
        return math.pow(self.x, 2)
    def cubo(self):
        return math.pow(self.x, 3)
valorx = float(input("Ingrese el número a operar: "))
x = Operacion(valorx)
print(f"El cuadrado de {valorx} es {x.cuadrado()}")
print(f"El cubo de {valorx} es {x.cubo()}")

