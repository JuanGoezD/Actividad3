import tkinter as tk
from tkinter import messagebox

class QuadraticEquationSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Solución de ecuación cuadrática")

        # Labels
        tk.Label(self.root, text="Valor de A:").grid(row=0, column=0)
        tk.Label(self.root, text="Valor de B:").grid(row=1, column=0)
        tk.Label(self.root, text="Valor de C:").grid(row=2, column=0)

        # Entries
        self.a_entry = tk.Entry(self.root)
        self.a_entry.grid(row=0, column=1)
        self.b_entry = tk.Entry(self.root)
        self.b_entry.grid(row=1, column=1)
        self.c_entry = tk.Entry(self.root)
        self.c_entry.grid(row=2, column=1)

        # Button
        tk.Button(self.root, text="Calcular", command=self.solve).grid(row=3, column=1, pady=10)

    def solve(self):
        try:
            # Obtener valores de las entradas
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            # Calcular el discriminante
            discriminant = b**2 - 4*a*c

            # Calcular las soluciones
            if discriminant > 0:
                x1 = (-b + discriminant**0.5) / (2*a)
                x2 = (-b - discriminant**0.5) / (2*a)
                message = f"Las soluciones son x1 = {x1:.2f} y x2 = {x2:.2f}"
            elif discriminant == 0:
                x = -b / (2*a)
                message = f"La solución es x = {x:.2f}"
            else:
                message = "La ecuación no tiene solución real"

            # Mostrar mensaje de salida
            messagebox.showinfo("Resultado", message)

        except ValueError:
            messagebox.showerror("Error", "Por favor, introduzca valores numéricos para A, B y C")


# Crear ventana principal
root = tk.Tk()

# Crear objeto del solucionador de ecuaciones cuadráticas
quadratic_equation_solver = QuadraticEquationSolver(root)

# Ejecutar la aplicación
root.mainloop()