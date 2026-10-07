class Planeta:
    def __init__(self, nombre, cantsat, masa, volumen, diametro, distsol, tipoplaneta, obsv):
        self.nombre = nombre
        self.cantsat = cantsat
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distsol = distsol
        self.tipoplaneta = tipoplaneta
        self.obsv = obsv
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
        print(f"Tipo de planeta: {self.tipoplaneta}")
        print(f"Es observable: {self.obsv}")
        print(f"Densidad: {self.dens()}")
        print(f"Ubicación: {self.intext()}")
nombre = input("Ingrese el nombre del planeta: ")
cantsat = int(input("Ingrese la cantidad de satelites: "))
masa = float(input("Ingrese la masa del planeta: "))
volumen = float(input("Ingrese el volumen del planeta: "))
diametro = float(input("Ingrese el diametro del planeta: "))
distsol = float(input("Ingrese la distancia al sol del planeta: "))
tipoplaneta = input("Ingrese el tipo de planeta: ")
obsv = input("Ingrese si el planeta es observable: ")
planeta = Planeta(nombre, cantsat, masa, volumen, diametro, distsol, tipoplaneta, obsv)
planeta.mostrar()