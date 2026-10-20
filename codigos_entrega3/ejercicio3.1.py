import math
import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self, nota1, nota2, nota3, nota4, nota5):
        self.notas = [nota1, nota2, nota3, nota4, nota5]

    def promedio(self):
        prom = sum(self.notas)/5
        return prom
    
    def desvest(self):
        suma = sum((notica - self.promedio())**2 for notica in self.notas)
        valdesvest = suma / 5
        return math.sqrt(valdesvest)

    def mayor(self):
        return max(self.notas)
        
    def menor(self):
        return min(self.notas)

class VentanaNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcular notas")
        self.resizable(False, False)
        self.camponotas()
        self.botones()
        self.resultados()

    def camponotas(self):
        nota1 = tk.Label(self, text="Nota 1: ")
        nota1.grid(row = 0, column = 0, padx='10', pady='5')
        self.campo1 = tk.Entry(self, width='15')
        self.campo1.grid(row = 0, column = 1, padx='10')

        nota2 = tk.Label(self, text="Nota 2: ")
        nota2.grid(row = 1, column = 0, pady='5')
        self.campo2 = tk.Entry(self, width='15')
        self.campo2.grid(row = 1, column = 1)

        nota3 = tk.Label(self, text="Nota 3: ")
        nota3.grid(row = 2, column = 0, pady='5')
        self.campo3 = tk.Entry(self, width='15')
        self.campo3.grid(row = 2, column = 1)

        nota4 = tk.Label(self, text="Nota 4: ")
        nota4.grid(row = 3, column = 0, pady='5')
        self.campo4 = tk.Entry(self, width='15')
        self.campo4.grid(row = 3, column = 1)

        nota5 = tk.Label(self, text="Nota 5: ")
        nota5.grid(row = 4, column = 0, pady='5')
        self.campo5 = tk.Entry(self, width='15')
        self.campo5.grid(row = 4, column = 1)

    def botones(self):
        btncalcular = tk.Button(self, text="Calcular", command=self.calcular)
        btncalcular.grid(row=5, column=0, padx='25')
        btnlimpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        btnlimpiar.grid(row=5, column=1)

    def calcular(self):
        nota1 = self.campo2.get()
        nota2 = self.campo1.get()
        nota3 = self.campo3.get()
        nota4 = self.campo4.get()
        nota5 = self.campo5.get()
        self.resprom.config(text="Promedio: ")
        self.resdesvest.config(text="Desviacion estandar: ")
        self.resmayor.config(text="Mayor nota: ")
        self.resmenor.config(text="Menor nota: ")
        if nota1 == "" or nota2 == "" or nota3 == "" or nota4 == "" or nota5 == "":
            messagebox.showwarning("Error", "Por favor ingresas las 5 notas en numeros")
            return
        
        try:
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)
            nota4 = float(nota4)
            nota5 = float(nota5)
        except ValueError:
            messagebox.showwarning("Error", "Las notas deben ser numericas")
            return

        v = Notas(nota1, nota2, nota3, nota4, nota5)

        prom = v.promedio()
        desvest = v.desvest()
        mayor = v.mayor()
        menor = v.menor()

        self.resprom.config(text=f"promedio: {prom}")
        self.resdesvest.config(text=f"Desviacion estandar: {round(desvest, 2)}")
        self.resmayor.config(text=f"Mayor nota: {mayor}")
        self.resmenor.config(text=f"Menor nota: {menor}")
        

    def limpiar(self):
        self.campo1.delete(0, tk.END)
        self.campo2.delete(0, tk.END)
        self.campo3.delete(0, tk.END)
        self.campo4.delete(0, tk.END)
        self.campo5.delete(0, tk.END)

        self.resprom.config(text="Promedio: ")
        self.resdesvest.config(text="Desviacion estandar: ")
        self.resmayor.config(text="Mayor nota: ")
        self.resmenor.config(text="Menor nota: ")

    def resultados(self):
        self.resprom = tk.Label(self, text="Promedio: ")
        self.resprom.grid(row=6, column=0)
        self.resdesvest = tk.Label(self, text="Desviacion estandar: ")
        self.resdesvest.grid(row=7, column=0)
        self.resmayor = tk.Label(self, text="Mayor nota: ")
        self.resmayor.grid(row=8, column=0)
        self.resmenor = tk.Label(self, text="Menor nota: ")
        self.resmenor.grid(row=9, column=0)

ventana = VentanaNotas()
ventana.mainloop()

