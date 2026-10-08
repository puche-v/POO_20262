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
    def hipotenusa(self):
        return math.sqrt((self.base**2)+(self.altura**2))
    def tipo(self):
        if self.base == self.altura:
            return "Isosceles"
        else:
            return "Escaleno"
class Rombo:
    def __init__(self, diagmayor, diagmenor, lado):
        self.diagmayor = diagmayor
        self.diagmenor = diagmenor
        self.lado = lado
    def arearo(self):
        return (self.diagmayor*self.diagmenor)/2
    def perimetroro(self):
        return self.lado * 4
class Trapecio:
    def __init__(self, basemayor, basemenor, altura, lado1, lado2, lado3, lado4):
        self.basemayor = basemayor
        self.basemenor = basemenor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4
    def areatra(self):
        return ((self.basemayor + self.basemenor)*self.altura) / 2
    def perimetrotra(self):
        return lado1 + lado2 + lado3 + lado4


x = int(input("""Seleccione la figura geometrica que quiere evaluar:
1- Circulo
2- Rectangulo
3- Cuadrado
4- Triangulo rectangulo 
5- Rombo
6- Trapecio
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
    print(f"El valor de la hipotenusa es {trirec.hipotenusa()}")
    print(f"El triangulo es: {trirec.tipo()}")
elif x == 5:
    diagmayor = int(input("Ingrese el valor de la diagonal mayor: "))
    diagmenor = int(input("Ingrese el valor de la diagonal menor: "))
    lado = int(input("Ingrese el valor del lado: "))
    rombo = Rombo(diagmayor, diagmenor, lado)
    print(f"El area es: {rombo.arearo()}")
    print(f"El perimetro es: {rombo.perimetroro()}")
elif x == 6:
    basemayor = int(input("Ingrese el valor de la base mayor: "))
    basemenor = int(input("Ingrese el valor de la base menor: "))
    altura = int(input("Ingrese el valor de la altura: "))
    lado1 = int(input("Ingrese el valor del lado 1: "))
    lado2 = int(input("Ingrese el valor del lado 2: "))
    lado3 = int(input("Ingrese el valor del lado 3: "))
    lado4 = int(input("Ingrese el valor del lado 4: "))
    trapecio = Trapecio(basemayor, basemenor, altura, lado1, lado2, lado3, lado4)
    print(f"El area es: {trapecio.areatra()}")
    print(f"El perimetro es: {trapecio.perimetrotra()}")