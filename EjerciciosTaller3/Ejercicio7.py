import tkinter as tk

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Comparar valores")
        
        self.label_a = tk.Label(self.ventana, text="Valor A:")
        self.label_a.grid(row=0, column=0)
        
        self.entry_a = tk.Entry(self.ventana)
        self.entry_a.grid(row=0, column=1)
        
        self.label_b = tk.Label(self.ventana, text="Valor B:")
        self.label_b.grid(row=1, column=0)
        
        self.entry_b = tk.Entry(self.ventana)
        self.entry_b.grid(row=1, column=1)
        
        self.label_resultado = tk.Label(self.ventana, text="Resultado:")
        self.label_resultado.grid(row=2, column=0)
        
        self.entry_resultado = tk.Entry(self.ventana)
        self.entry_resultado.grid(row=2, column=1)
        
        self.boton_comparar = tk.Button(self.ventana, text="Comparar", command=self.comparar)
        self.boton_comparar.grid(row=3, column=0, columnspan=2)
    
    def comparar(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        
        if a > b:
            resultado = "A es mayor que B"
        elif a < b:
            resultado = "A es menor que B"
        else:
            resultado = "A es igual a B"
        
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.insert(0, resultado)
    
    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.iniciar()