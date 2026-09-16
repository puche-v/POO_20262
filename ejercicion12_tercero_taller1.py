class Salario:
    def __init__(self, horas, valorhora, ret):
        self.horas = horas
        self.valorhora = valorhora
        self.ret = ret

    def salariobruto(self):
        return self.horas * self.valorhora
    
    def retencionf(self):
        return (self.salariobruto() * self.ret)/100
    
    def salarioneto(self):
        return self.salariobruto() - self.retencionf()

valorhora = float(input("Ingrese a cuanto va a pagar la hora: "))
horas = float(input("Ingrese la cantidad de horas trabajadas: "))
ret = float(input("Ingrese el valor de la retencion de fuente: "))
vals = Salario(horas, valorhora, ret)

print(f"El valor del salario bruto es de: {vals.salariobruto()}")
print(f"El valor de la retención es de: {vals.retencionf()}")
print(f"El valor del salario neto es de: {vals.salarioneto()}")

