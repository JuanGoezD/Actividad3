import tkinter as tk

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Pago de matrícula")
        
        self.label_inscripcion = tk.Label(self.ventana, text="Número de inscripción:")
        self.label_inscripcion.grid(row=0, column=0)
        
        self.entry_inscripcion = tk.Entry(self.ventana)
        self.entry_inscripcion.grid(row=0, column=1)
        
        self.label_nombres = tk.Label(self.ventana, text="Nombres:")
        self.label_nombres.grid(row=1, column=0)
        
        self.entry_nombres = tk.Entry(self.ventana)
        self.entry_nombres.grid(row=1, column=1)
        
        self.label_patrimonio = tk.Label(self.ventana, text="Patrimonio:")
        self.label_patrimonio.grid(row=2, column=0)
        
        self.entry_patrimonio = tk.Entry(self.ventana)
        self.entry_patrimonio.grid(row=2, column=1)
        
        self.label_estrato = tk.Label(self.ventana, text="Estrato social:")
        self.label_estrato.grid(row=3, column=0)
        
        self.entry_estrato = tk.Entry(self.ventana)
        self.entry_estrato.grid(row=3, column=1)
        
        self.boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=4, column=0, columnspan=2)
        
        self.label_pago = tk.Label(self.ventana, text="Pago de matrícula:")
        self.label_pago.grid(row=5, column=0)
        
        self.entry_pago = tk.Entry(self.ventana)
        self.entry_pago.grid(row=5, column=1)
    
    def calcular(self):
        patrimonio = float(self.entry_patrimonio.get())
        estrato = int(self.entry_estrato.get())
        
        if patrimonio > 2000000 and estrato > 3:
            pago = 50000 + patrimonio * 0.03
        else:
            pago = 50000
        
        self.entry_pago.delete(0, tk.END)
        self.entry_pago.insert(0, pago)
    
    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.iniciar()