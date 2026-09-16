class Edades:
    def __init__(self, edjuan):
        self.edjuan = edjuan

    def calcular_edalbert(self):
        return 2*self.edjuan/3

    def calcular_edana(self):
        return 4*self.edjuan/3
    
    def calcular_edmama(self):
        return self.edjuan + self.calcular_edana() + self.calcular_edalbert()

valedjuan = float(input("Edad de Juan: ")) 
edjuan = Edades(valedjuan)

print(f"Edad de Alberto: {edjuan.calcular_edalbert()}")
print(f"Edad de Ana: {edjuan.calcular_edana()}")
print(f"Edad de Juan: {valedjuan}")
print(f"Edad de la madre: {edjuan.calcular_edmama()}")


