import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def areac(self):
        return math.pi * (self.radio ** 2)

    def perimetroc(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def arear(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def areacu(self):
        return self.lado ** 2

    def perimetrocu(self):
        return 4 * self.lado

class Triangulorec:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def areat(self):
        return (self.base * self.altura) / 2

    def perimetrot(self):
        return self.base + self.altura + ((self.base ** 2 + self.altura ** 2) ** 0.5)

x = int(input("""Seleccione la figura geometrica que quiere evaluar:
1- Circulo
2- Rectangulo
3- Cuadrado
4- Triangulo rectangulo 
"""))
if x == 1:
    radio = int(input("Ingrese el radio del circulo: "))
    circulo = Circulo(radio)
    print(f"El area del circulo es: {circulo.areac()}")
    print(f"El perimetro del circulo es: {circulo.perimetroc()}")
elif x == 2:
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    rect = Rectangulo(base, altura)
    print(f"El area es: {rect.arear()}")
    print(f"El perimetro es: {rect.perimetro()}")
elif x == 3:
    lado = int(input("Ingrese el valor del lado: "))
    cuad = Cuadrado(lado)
    print(f"El area es: {cuad.areacu()}")
    print(f"El perimetro es: {cuad.perimetrocu()}")
elif x == 4:
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    trirec = Triangulorec(base, altura)
    print(f"El area es: {trirec.areat()}")
    print(f"El perimetro es: {trirec.perimetrot()}")