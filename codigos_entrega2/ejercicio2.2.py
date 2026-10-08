from enum import Enum

class Tipoplaneta(Enum):
    TERRESTRE = "TERRESTRE"
    GASEOSO = "GASEOSO"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre, cantsat, masa, volumen, diametro, distsol, obsv, perdorbital, rotacion, tipo):
        self.nombre = nombre
        self.cantsat = cantsat
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distsol = distsol
        self.obsv = obsv
        self.perdorbital = perdorbital
        self.rotacion = rotacion
        self.tipo = tipo

    def dens(self):
        densidad = self.masa/self.volumen
        return densidad
    def intext(self):
        if distsol < 149597870:
            return "Interior"
        else:
            return "Exterior"

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satelites: {self.cantsat}")
        print(f"Masa: {self.masa}")
        print(f"Volumen: {self.volumen}")
        print(f"Diametro: {self.diametro}")
        print(f"Distancia al sol: {self.distsol}")
        print(f"Es observable: {self.obsv}")
        print(f"Densidad: {self.dens()}")
        print(f"Ubicación: {self.intext()}")
        print(f"Periodo orbital: {self.perdorbital}")
        print(f"Periodo de rotación: {self.rotacion}")
        print(f"Tipo de planeta: {self.tipo.value}")

tipo = "TERRESTRE"
perdorbital = "3 años"
rotacion = "1.5 días"
nombre = input("Ingrese el nombre del planeta: ")
cantsat = int(input("Ingrese la cantidad de satelites: "))
masa = float(input("Ingrese la masa del planeta: "))
volumen = float(input("Ingrese el volumen del planeta: "))
diametro = float(input("Ingrese el diametro del planeta: "))
distsol = float(input("Ingrese la distancia al sol del planeta: "))
obsv = input("Ingrese si el planeta es observable: ")
tipo = Tipoplaneta.TERRESTRE
planeta = Planeta(nombre, cantsat, masa, volumen, diametro, distsol, obsv, perdorbital, rotacion, tipo)
planeta.mostrar()
