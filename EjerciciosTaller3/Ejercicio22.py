import tkinter as tk

class SalaryCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de salario")

        self.label_name = tk.Label(master, text="Nombre del empleado:")
        self.label_name.pack()

        self.entry_name = tk.Entry(master)
        self.entry_name.pack()

        self.label_salary = tk.Label(master, text="Salario básico por hora:")
        self.label_salary.pack()

        self.entry_salary = tk.Entry(master)
        self.entry_salary.pack()

        self.label_hours = tk.Label(master, text="Número de horas trabajadas en el mes:")
        self.label_hours.pack()

        self.entry_hours = tk.Entry(master)
        self.entry_hours.pack()

        self.button_calculate = tk.Button(master, text="Calcular salario", command=self.calculate)
        self.button_calculate.pack()

        self.label_result = tk.Label(master, text="")
        self.label_result.pack()

    def calculate(self):
        name = self.entry_name.get()
        salary = float(self.entry_salary.get())
        hours = float(self.entry_hours.get())

        monthly_salary = salary * hours

        if monthly_salary > 450000:
            self.label_result.config(text=f"{name}, su salario mensual es de ${monthly_salary:.2f}")
        else:
            self.label_result.config(text=f"{name}")
root = tk.Tk()
app = SalaryCalculator(root)
root.mainloop()