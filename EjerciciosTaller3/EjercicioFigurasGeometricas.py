import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self, unidades='cm'):
        self.unidades = unidades

    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio, unidades='cm'):
        super().__init__(unidades)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura, unidades='cm'):
        super().__init__(unidades)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado, unidades='cm'):
        super().__init__(unidades)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo(FiguraGeometrica):
    def __init__(self, base, altura, unidades='cm'):
        super().__init__(unidades)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        hipotenusa = self.calcular_hipotenusa()
        return self.base + self.altura + hipotenusa

    def calcular_hipotenusa(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def tipo_triangulo(self):
        if self.base == self.altura:
            return "Equilátero"
        elif self.base == self.calcular_hipotenusa() or self.altura == self.calcular_hipotenusa():
            return "Isósceles"
        else:
            return "Escaleno"

#-----Clase Ventana que manejará el frame para visualizar los diferentes widgets-----
class Ventana:
    def __init__(self, master):
        #----Hereda de la clase Tk(). 
        self.master = master
        master.title("Calculadora de figuras geométricas")
        #----Frame del circulo para visualizacion de los diferentes widgets. La misma Operacion con
        #las demás figuras geometricas-------------------------------------------------------------
        self.frame_circulo = tk.Frame(master)
        self.frame_circulo.pack(side=tk.TOP, padx=10, pady=10)

        self.label_radio = tk.Label(self.frame_circulo, text="Radio:")
        self.label_radio.pack(side=tk.LEFT)

        self.entry_radio = tk.Entry(self.frame_circulo)
        self.entry_radio.pack(side=tk.LEFT)

        self.label_unidades_circulo = tk.Label(self.frame_circulo, text="cm")
        self.label_unidades_circulo.pack(side=tk.LEFT)

        self.button_circulo = tk.Button(master, text="Calcular círculo", command=self.calcular_circulo)
        self.button_circulo.pack(side=tk.TOP, padx=10, pady=10)

        self.frame_rectangulo = tk.Frame(master)
        self.frame_rectangulo.pack(side=tk.TOP, padx=10, pady=10)

        self.label_base = tk.Label(self.frame_rectangulo, text="Base:")
        self.label_base.pack(side=tk.LEFT)

        self.entry_base = tk.Entry(self.frame_rectangulo)
        self.entry_base.pack(side = tk.LEFT)
        self.label_altura = tk.Label(self.frame_rectangulo, text="Altura:")
        self.label_altura.pack(side=tk.LEFT)

        self.entry_altura = tk.Entry(self.frame_rectangulo)
        self.entry_altura.pack(side=tk.LEFT)

        self.label_unidades_rectangulo = tk.Label(self.frame_rectangulo, text="cm")
        self.label_unidades_rectangulo.pack(side=tk.LEFT)

        self.button_rectangulo = tk.Button(master, text="Calcular rectángulo", command=self.calcular_rectangulo)
        self.button_rectangulo.pack(side=tk.TOP, padx=10, pady=10)

        self.frame_cuadrado = tk.Frame(master)
        self.frame_cuadrado.pack(side=tk.TOP, padx=10, pady=10)

        self.label_lado = tk.Label(self.frame_cuadrado, text="Lado:")
        self.label_lado.pack(side=tk.LEFT)

        self.entry_lado = tk.Entry(self.frame_cuadrado)
        self.entry_lado.pack(side=tk.LEFT)

        self.label_unidades_cuadrado = tk.Label(self.frame_cuadrado, text="cm")
        self.label_unidades_cuadrado.pack(side=tk.LEFT)

        self.button_cuadrado = tk.Button(master, text="Calcular cuadrado", command=self.calcular_cuadrado)
        self.button_cuadrado.pack(side=tk.TOP, padx=10, pady=10)

        self.frame_triangulo = tk.Frame(master)
        self.frame_triangulo.pack(side=tk.TOP, padx=10, pady=10)

        self.label_base_triangulo = tk.Label(self.frame_triangulo, text="Base:")
        self.label_base_triangulo.pack(side=tk.LEFT)

        self.entry_base_triangulo = tk.Entry(self.frame_triangulo)
        self.entry_base_triangulo.pack(side=tk.LEFT)

        self.label_altura_triangulo = tk.Label(self.frame_triangulo, text="Altura:")
        self.label_altura_triangulo.pack(side=tk.LEFT)

        self.entry_altura_triangulo = tk.Entry(self.frame_triangulo)
        self.entry_altura_triangulo.pack(side=tk.LEFT)

        self.label_unidades_triangulo = tk.Label(self.frame_triangulo, text="cm")
        self.label_unidades_triangulo.pack(side=tk.LEFT)

        self.button_triangulo = tk.Button(master, text="Calcular triángulo", command=self.calcular_triangulo)
        self.button_triangulo.pack(side=tk.TOP, padx=10, pady=10)

    #---Metodos que calcularán y mostrarán los resultados de lo que se le ponga en los Entries
    #Estos se muestran en una messagebox para economizar espacio------------------------------
    def calcular_circulo(self):
            radio = float(self.entry_radio.get())
            circulo = Circulo(radio)
            resultado_area = circulo.area()
            resultado_perimetro = circulo.perimetro()
            messagebox.showinfo("Resultados", f"Área del círculo: {resultado_area:.2f} cm²\nPerímetro del círculo: {resultado_perimetro:.2f} cm")

    def calcular_rectangulo(self):
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            rectangulo = Rectangulo(base, altura)
            resultado_area = rectangulo.area()
            resultado_perimetro = rectangulo.perimetro()
            messagebox.showinfo("Resultados", f"Área del rectángulo: {resultado_area:.2f} cm²\nPerímetro del rectángulo: {resultado_perimetro:.2f} cm")
    
    def calcular_cuadrado(self):
        lado = float(self.entry_lado.get())
        cuadrado = Cuadrado(lado)
        resultado_area = cuadrado.area()
        resultado_perimetro = cuadrado.perimetro()
        messagebox.showinfo("Resultados", f"Área del cuadrado: {resultado_area:.2f} cm²\nPerímetro del cuadrado: {resultado_perimetro:.2f} cm")

    def calcular_triangulo(self):
        base = float(self.entry_base_triangulo.get())
        altura = float(self.entry_altura_triangulo.get())
        triangulo = TrianguloRectangulo(base, altura)
        resultado_area = triangulo.area()
        resultado_perimetro = triangulo.perimetro()
        resultado_hipotenusa = triangulo.calcular_hipotenusa()
        resultado_tipo       = triangulo.tipo_triangulo()
        messagebox.showinfo("Resultados", f"El área del triángulo es: {resultado_area:.2f}cm²\n Perímetro: {resultado_perimetro:.2f}cm\n Hipotenusa: {resultado_hipotenusa:.2f}\nTipo Triangulo = {resultado_tipo} ")

#------Ejecución de Código---------------
if __name__ == "__main__":
    root = tk.Tk()
    mi_ventana = Ventana(root)
    root.mainloop()
