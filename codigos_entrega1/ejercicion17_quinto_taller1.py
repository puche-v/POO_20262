import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * math.pow(self.radio, 2)
    def long(self):
        return 2 * math.pi * self.radio

vradio = float(input("Ingrese el valor del radio: "))
radio = Circulo(vradio)

print(f"El area del circulo es {radio.area()}")
print(f"La longitud de la circunferencia es {radio.long()}")

