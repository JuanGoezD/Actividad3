from typing import List
import tkinter as tk

class Mayor:
    @staticmethod
    def calcular_mayor(numeros: List[float]) -> float:
        mayor = numeros[0]
        for numero in numeros:
            if numero > mayor:
                mayor = numero
        return mayor

class Interfaz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calcular valor mayor")
        self.window.geometry("400x200")

        # Entry para ingresar la serie de números
        self.label_numeros = tk.Label(self.window, text="Ingrese los números separados por comas:")
        self.label_numeros.pack()
        self.entry_numeros = tk.Entry(self.window)
        self.entry_numeros.pack()

        # Botón para calcular el mayor
        self.boton_calcular = tk.Button(self.window, text="Calcular", command=self.calcular_mayor)
        self.boton_calcular.pack()

        # Label para mostrar el mayor
        self.label_mayor = tk.Label(self.window, text="El mayor es:")
        self.label_mayor.pack()
        self.resultado_mayor = tk.StringVar()
        self.entry_mayor = tk.Entry(self.window, textvariable=self.resultado_mayor, state="readonly")
        self.entry_mayor.pack()

        self.window.mainloop()

    def calcular_mayor(self):
        serie_numeros = self.entry_numeros.get()
        lista_numeros_string = serie_numeros.split(",")
        lista_numeros = [float(numero) for numero in lista_numeros_string]
        mayor = Mayor.calcular_mayor(lista_numeros)
        self.resultado_mayor.set(str(mayor))

#-----Ejecucion del código--------
if __name__ == "__main__":
    
    Interfaz()