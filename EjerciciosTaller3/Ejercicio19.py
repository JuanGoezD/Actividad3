import tkinter as tk
import math

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Triángulo equilátero")
        
        self.label_lado = tk.Label(self.ventana, text="Lado:")
        self.label_lado.grid(row=0, column=0)
        
        self.entry_lado = tk.Entry(self.ventana)
        self.entry_lado.grid(row=0, column=1)
        
        self.label_perimetro = tk.Label(self.ventana, text="Perímetro:")
        self.label_perimetro.grid(row=1, column=0)
        
        self.entry_perimetro = tk.Entry(self.ventana)
        self.entry_perimetro.grid(row=1, column=1)
        
        self.label_altura = tk.Label(self.ventana, text="Altura:")
        self.label_altura.grid(row=2, column=0)
        
        self.entry_altura = tk.Entry(self.ventana)
        self.entry_altura.grid(row=2, column=1)
        
        self.label_area = tk.Label(self.ventana, text="Área:")
        self.label_area.grid(row=3, column=0)
        
        self.entry_area = tk.Entry(self.ventana)
        self.entry_area.grid(row=3, column=1)
        
        self.boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=4, column=0, columnspan=2)
    
    def calcular(self):
        lado = float(self.entry_lado.get())
        perimetro = 3 * lado
        altura = math.sqrt(3) / 2 * lado
        area = math.sqrt(3) / 4 * lado ** 2
        
        self.entry_perimetro.delete(0, tk.END)
        self.entry_perimetro.insert(0, perimetro)
        
        self.entry_altura.delete(0, tk.END)
        self.entry_altura.insert(0, altura)
        
        self.entry_area.delete(0, tk.END)
        self.entry_area.insert(0, area)
    
    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.iniciar()