import tkinter as tk

class SquareRootGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculadora")
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y campo de entrada para el número
        self.number_label = tk.Label(self.master, text="Ingrese un número entero positivo:")
        self.number_label.pack()
        self.number_entry = tk.Entry(self.master)
        self.number_entry.pack()

        # Botón para calcular la raíz cuadrada
        self.sqrt_button = tk.Button(self.master, text="Raíz cuadrada", command=self.sqrt)
        self.sqrt_button.pack()

        # Etiqueta y campo de salida para la raíz cuadrada
        self.sqrt_label = tk.Label(self.master, text="Raíz cuadrada:")
        self.sqrt_label.pack()
        self.sqrt_result = tk.Label(self.master, text="")
        self.sqrt_result.pack()

        # Botón para calcular el cuadrado
        self.square_button = tk.Button(self.master, text="Cuadrado", command=self.square)
        self.square_button.pack()

        # Etiqueta y campo de salida para el cuadrado
        self.square_label = tk.Label(self.master, text="Cuadrado:")
        self.square_label.pack()
        self.square_result = tk.Label(self.master, text="")
        self.square_result.pack()

        # Botón para calcular el cubo
        self.cube_button = tk.Button(self.master, text="Cubo", command=self.cube)
        self.cube_button.pack()

        # Etiqueta y campo de salida para el cubo
        self.cube_label = tk.Label(self.master, text="Cubo:")
        self.cube_label.pack()
        self.cube_result = tk.Label(self.master, text="")
        self.cube_result.pack()

    def sqrt(self):

        num = int(self.number_entry.get())
        sqrt_num = round(num ** 0.5, 2)
        self.sqrt_result.config(text=str(sqrt_num))
        

    def square(self):
        
        num = int(self.number_entry.get())
        square_num = num ** 2
        self.square_result.config(text=str(square_num))
        

    def cube(self):
            
        num = int(self.number_entry.get())
        cube_num = num ** 3
        self.cube_result.config(text=str(cube_num))
        

root = tk.Tk()
app = SquareRootGUI(master=root)
app.mainloop()