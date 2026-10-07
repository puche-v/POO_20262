class Persona:
    def __init__(self, nombre, apells, doc, fechanac, paisnac, genero):
        self.nombre = nombre
        self.apells = apells
        self.doc = doc
        self.fechanac = fechanac
        self.paisnac = paisnac
        self.genero = genero

    def mostrar(self):
        print(f"Nombre: {self.nombre} {self.apells}")
        print(f"Documento: {self.doc}")
        print(f"Fecha de nacimiento: {self.fechanac}")  
        print(f"Pais de nacimiento: {self.paisnac}")
        print(f"Genero: {self.genero}")

nombre = input("Ingrese su nombre: ")
apells = input("Ingrese sus apellidos: ")
doc = input("Ingrese su documento: ")
fechanac = input("Ingrese su fecha de nacimiento: ")
paisnac = input("Ingrese su pais de nacimiento: ")
genero = input("Ingrese su genero: ")
persona = Persona(nombre, apells, doc, fechanac, paisnac, genero)
persona.mostrar()