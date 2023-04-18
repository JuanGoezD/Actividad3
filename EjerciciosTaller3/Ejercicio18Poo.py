import tkinter as tk

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion
    
    def calcular_salario_bruto(self):
        salario_bruto = self.horas_trabajadas * self.valor_hora
        return salario_bruto
    
    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = salario_bruto * (1 - self.retencion/100)
        return salario_neto

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Salario de empleado")
        
        self.label_codigo = tk.Label(self.ventana, text="Código")
        self.label_codigo.grid(row=0, column=0)
        
        self.entry_codigo = tk.Entry(self.ventana)
        self.entry_codigo.grid(row=0, column=1)
        
        self.label_nombres = tk.Label(self.ventana, text="Nombres")
        self.label_nombres.grid(row=1, column=0)
        
        self.entry_nombres = tk.Entry(self.ventana)
        self.entry_nombres.grid(row=1, column=1)
        
        self.label_horas = tk.Label(self.ventana, text="Horas trabajadas al mes")
        self.label_horas.grid(row=2, column=0)
        
        self.entry_horas = tk.Entry(self.ventana)
        self.entry_horas.grid(row=2, column=1)
        
        self.label_valor = tk.Label(self.ventana, text="Valor hora trabajada")
        self.label_valor.grid(row=3, column=0)
        
        self.entry_valor = tk.Entry(self.ventana)
        self.entry_valor.grid(row=3, column=1)
        
        self.label_retencion = tk.Label(self.ventana, text="% Retención en la fuente")
        self.label_retencion.grid(row=4, column=0)
        
        self.entry_retencion = tk.Entry(self.ventana)
        self.entry_retencion.grid(row=4, column=1)
        
        self.boton_calcular = tk.Button(self.ventana, text="Calcular salario", command=self.mostrar_salario)
        self.boton_calcular.grid(row=5, column=0,  columnspan=2)
        
            
        self.label_salario_bruto = tk.Label(self.ventana, text="Salario bruto:")
        self.label_salario_bruto.grid(row=6, column=0)
        
        self.entry_salario_bruto = tk.Entry(self.ventana)
        self.entry_salario_bruto.grid(row=6, column=1)
        
        self.label_salario_neto = tk.Label(self.ventana, text="Salario neto:")
        self.label_salario_neto.grid(row=7, column=0)
        
        self.entry_salario_neto = tk.Entry(self.ventana)
        self.entry_salario_neto.grid(row=7, column=1)

    def mostrar_salario(self):
        codigo = self.entry_codigo.get()
        nombres = self.entry_nombres.get()
        horas_trabajadas = float(self.entry_horas.get())
        valor_hora = float(self.entry_valor.get())
        retencion = float(self.entry_retencion.get())
        
        empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion)
        salario_bruto = empleado.calcular_salario_bruto()
        salario_neto = empleado.calcular_salario_neto()
        
        self.entry_salario_bruto.delete(0, tk.END)
        self.entry_salario_bruto.insert(0, salario_bruto)
        
        self.entry_salario_neto.delete(0, tk.END)
        self.entry_salario_neto.insert(0, salario_neto)

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.iniciar()
