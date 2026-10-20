import math 
import tkinter as tk
from tkinter import messagebox
class Figuras():
    def __init__(self):
        self.volumen = 0
        self.superficie = 0
class Cilindro(Figuras):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
    def volumenci(self):
        self.volumen = math.pi * self.radio**2 * self.altura
    def superficieci(self):
        self.superficie = 2 * math.pi * self.radio * (self.radio + self.altura)
class Esfera(Figuras):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
    def volumenes(self):
        self.volumen = (4/3)*math.pi * self.radio**3
    def superficiees(self):
        self.superficie = 4 * math.pi * self.radio**2
class Piramide(Figuras):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
    def volumenpi(self):
        self.volumen = (self.base**2 * self.altura)/3
    def superficiepi(self):
        self.superficie = self.base**2 + 2*(self.base * self.apotema)
class Cubo(Figuras):
    def __init__(self, arista):
        super().__init__()
        self.arista = arista
    def volumencu(self):
        self.volumen = self.arista**3
    def superficiecu(self):
        self.superficie = 6 * (self.arista**2)
class Prisma(Figuras):
    def __init__(self, base, ancho, altura):
        super().__init__()
        self.base = base
        self.ancho = ancho
        self.altura = altura
    def volumenpr(self):
        self.volumen = self.base * self.ancho * self.altura
    def superficiepr(self):
        self.superficie =  2 * (self.base * self.ancho + self.base * self.altura + self.ancho * self.altura)


class VentanaCilindro(tk.Toplevel):
    def __init__(self, principal):
        super().__init__(principal)
        self.title("Cilindro")
        self.resizable(False, False)
        self.valores()

    def valores(self):
        radio = tk.Label(self, text="Radio (cms): ")
        radio.grid(row=0, column=0, pady='5', padx=10)
        self.campo1 = tk.Entry(self, width='15')
        self.campo1.grid(row=0, column=1, padx=10)
        altura = tk.Label(self, text="Altura (cms): ")
        altura.grid(row=1, column=0)
        self.campo2 = tk.Entry(self, width='15')
        self.campo2.grid(row=1, column= 1)

        btncalcular = tk.Button(self, text="Calcular", command=self.calcular)
        btncalcular.grid(row=2, column=1, pady=5)

        self.v_volumenci = tk.Label(self, text="Volumen del cilindro (cms3): ")
        self.v_volumenci.grid(row=3, column=0, columnspan=2)
        self.v_superficieci = tk.Label(self, text="Superficie del cilindro(cms2): ")
        self.v_superficieci.grid(row=4, column=0, columnspan=2)

        self.imagen = tk.PhotoImage(file="codigos_entrega3/cilindro.png").subsample(3)
        foto = tk.Label(self, image=self.imagen)
        foto.grid(row=5, column=0, columnspan=2)

    def calcular(self):
        try:
            radio = float(self.campo1.get())
            altura = float(self.campo2.get())
        except ValueError:
            messagebox.showwarning("Error", "Por favor ingresar los valores en numeros")
            return
        cil = Cilindro(radio, altura)
        cil.volumenci()
        cil.superficieci()

        self.v_volumenci.config(text=f"Volumen del cilindro (cms3): {round(cil.volumen, 2)}")
        self.v_superficieci.config(text=f"Superficie del cilindro (cms2): {round(cil.superficie, 2)}")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, principal):
        super().__init__(principal)
        self.title("Esfera")
        self.resizable(False, False)
        self.valores()

    def valores(self):
        radio = tk.Label(self, text="Radio(cms): ")
        radio.grid(row=0, column=0, pady='5', padx=10)
        self.campo1 = tk.Entry(self, width='15')
        self.campo1.grid(row=0, column=1, padx=10)

        btncalcular = tk.Button(self, text="Calcular", command=self.calcular)
        btncalcular.grid(row=2, column=1, pady=5)

        self.v_volumenes = tk.Label(self, text="Volumen de la esfera (cms3): ")
        self.v_volumenes.grid(row=3, column=0, columnspan=2)
        self.v_superficiees = tk.Label(self, text="Superficie de la esfera(cms2): ")
        self.v_superficiees.grid(row=4, column=0, columnspan=2)

        self.imagen = tk.PhotoImage(file="codigos_entrega3/esfera.png").subsample(3)
        foto = tk.Label(self, image=self.imagen)
        foto.grid(row=5, column=0, columnspan=2)

    def calcular(self):
        try:
            radio = float(self.campo1.get())
        except ValueError:
            messagebox.showwarning("Error", "Por favor ingresar los valores en numeros")
            return
        esf = Esfera(radio)
        esf.volumenes()
        esf.superficiees()

        self.v_volumenes.config(text=f"Volumen de la esfera (cms3): {round(esf.volumen, 2)}")
        self.v_superficiees.config(text=f"Superficie de la esfera (cms2): {round(esf.superficie, 2)}")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, principal):
        super().__init__(principal)
        self.title("Piramide")
        self.resizable(False, False)
        self.valores()

    def valores(self):
        base = tk.Label(self, text="Base (cms): ")
        base.grid(row=0, column=0, pady='5', padx=10)
        self.campo1 = tk.Entry(self, width='15')
        self.campo1.grid(row=0, column=1, padx=10)
        altura = tk.Label(self, text="Altura (cms): ")
        altura.grid(row=1, column=0)
        self.campo2 = tk.Entry(self, width='15')
        self.campo2.grid(row=1, column= 1)
        apotema = tk.Label(self, text="Apotema (cms): ")
        apotema.grid(row=2, column=0)
        self.campo3 = tk.Entry(self, width='15')
        self.campo3.grid(row=2, column= 1)

        btncalcular = tk.Button(self, text="Calcular", command=self.calcular)
        btncalcular.grid(row=3, column=1, pady=5)

        self.v_volumenpi = tk.Label(self, text="Volumen de la piramide (cms3): ")
        self.v_volumenpi.grid(row=4, column=0, columnspan=2)
        self.v_superficiepi = tk.Label(self, text="Superficie de la piramide (cms2): ")
        self.v_superficiepi.grid(row=5, column=0, columnspan=2)

        self.imagen = tk.PhotoImage(file="codigos_entrega3/piramide.png").subsample(3)
        foto = tk.Label(self, image=self.imagen)
        foto.grid(row=6, column=0, columnspan=2)

    def calcular(self):
        try:
            base = float(self.campo1.get())
            altura = float(self.campo2.get())
            apotema = float(self.campo3.get())
        except ValueError:
            messagebox.showwarning("Error", "Por favor ingresar los valores en numeros")
            return
        pir = Piramide(base, altura, apotema)
        pir.volumenpi()
        pir.superficiepi()

        self.v_volumenpi.config(text=f"Volumen de la piramide (cms3): {round(pir.volumen, 2)}")
        self.v_superficiepi.config(text=f"Superficie de la piramide (cms2): {round(pir.superficie, 2)}")

class VentanaPrisma(tk.Toplevel):
    def __init__(self, principal):
        super().__init__(principal)
        self.title("Prisma")
        self.resizable(False, False)
        self.valores()

    def valores(self):
        base = tk.Label(self, text="Base (cms): ")
        base.grid(row=0, column=0, pady='5', padx=10)
        self.campo1 = tk.Entry(self, width='15')
        self.campo1.grid(row=0, column=1, padx=10)
        altura = tk.Label(self, text="Altura (cms): ")
        altura.grid(row=1, column=0)
        self.campo2 = tk.Entry(self, width='15')
        self.campo2.grid(row=1, column= 1)
        ancho = tk.Label(self, text="Ancho (cms): ")
        ancho.grid(row=2, column=0)
        self.campo3 = tk.Entry(self, width='15')
        self.campo3.grid(row=2, column= 1)

        btncalcular = tk.Button(self, text="Calcular", command=self.calcular)
        btncalcular.grid(row=3, column=1, pady=5)

        self.v_volumenpr = tk.Label(self, text="Volumen de la piramide (cms3): ")
        self.v_volumenpr.grid(row=4, column=0, columnspan=2)
        self.v_superficiepr = tk.Label(self, text="Superficie de la piramide (cms2): ")
        self.v_superficiepr.grid(row=5, column=0, columnspan=2)

        self.imagen = tk.PhotoImage(file="codigos_entrega3/prisma.png").subsample(3)
        foto = tk.Label(self, image=self.imagen)
        foto.grid(row=6, column=0, columnspan=2)

    def calcular(self):
        try:
            base = float(self.campo1.get())
            altura = float(self.campo2.get())
            ancho = float(self.campo3.get())
        except ValueError:
            messagebox.showwarning("Error", "Por favor ingresar los valores en numeros")
            return
        pri = Prisma(base, ancho, altura)
        pri.volumenpr()
        pri.superficiepr()

        self.v_volumenpr.config(text=f"Volumen del prisma (cms3): {round(pri.volumen, 2)}")
        self.v_superficiepr.config(text=f"Superficie del prisma (cms2): {round(pri.superficie, 2)}")

class VentanaCubo(tk.Toplevel):
    def __init__(self, principal):
        super().__init__(principal)
        self.title("Cubo")
        self.resizable(False, False)
        self.valores()

    def valores(self):
        arista = tk.Label(self, text="Arista (cms): ")
        arista.grid(row=0, column=0, pady='5', padx=10)
        self.campo1 = tk.Entry(self, width='15')
        self.campo1.grid(row=0, column=1, padx=10)

        btncalcular = tk.Button(self, text="Calcular", command=self.calcular)
        btncalcular.grid(row=2, column=1, pady=5)

        self.v_volumencu = tk.Label(self, text="Volumen del cubo (cms3): ")
        self.v_volumencu.grid(row=3, column=0, columnspan=2)
        self.v_superficiecu = tk.Label(self, text="Superficie del cubo (cms2): ")
        self.v_superficiecu.grid(row=4, column=0, columnspan=2)

        self.imagen = tk.PhotoImage(file="codigos_entrega3/cubo.png").subsample(3)
        foto = tk.Label(self, image=self.imagen)
        foto.grid(row=5, column=0, columnspan=2)

    def calcular(self):
        try:
            arista = float(self.campo1.get())
        except ValueError:
            messagebox.showwarning("Error", "Por favor ingresar los valores en numeros")
            return
        cub = Cubo(arista)
        cub.volumencu()
        cub.superficiecu()

        self.v_volumencu.config(text=f"Volumen del cubo (cms3): {round(cub.volumen, 2)}")
        self.v_superficiecu.config(text=f"Superficie del cubo (cms2): {round(cub.superficie, 2)}")

class Ventanaprincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Areas y superficies")
        self.botones()

    def botones(self):
        btncilindro = tk.Button(self, text="Cilindro", command=self.vcilindro)
        btncilindro.grid(row=0, column=0, padx = '15', pady='15')
        btnesfera = tk.Button(self, text="Esfera", command=self.vesfera)
        btnesfera.grid(row=1, column=0, padx = '15', pady='15')
        btnpiramide = tk.Button(self, text="Piramide", command=self.vpiramide)
        btnpiramide.grid(row=0, column=1, padx = '15', pady='15')
        btnprisma = tk.Button(self, text="Prisma", command=self.vprisma)
        btnprisma.grid(row=1, column=1, padx = '15', pady='15')
        btncubo = tk.Button(self, text="Cubo", command=self.vcubo)
        btncubo.grid(row=0, column=3, padx = '15', pady='15')

    def vcilindro(self):
        VentanaCilindro(self)
    def vesfera(self):
        VentanaEsfera(self)
    def vpiramide(self):
        VentanaPiramide(self)
    def vprisma(self):
        VentanaPrisma(self)
    def vcubo(self):
        VentanaCubo(self)

ventana = Ventanaprincipal()
ventana.mainloop()