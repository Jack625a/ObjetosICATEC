import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RegistroEstudiantesFormulario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Estudiantes")
        self.ventana.geometry("400x300")
        self.ventana.config(bg="#F0F0F0")

        self.etiqueta_titulo = tk.Label(self.ventana, text="Registro de Estudiantes", font=("Arial", 20), bg="#F0F0F0")
        self.etiqueta_titulo.pack(pady=20)

        self.etiqueta_nombre = tk.Label(self.ventana, text="Nombre:", font=("Arial", 12), bg="#F0F0F0")
        self.etiqueta_nombre.pack()

        self.entry_nombre = tk.Entry(self.ventana, font=("Arial", 12))
        self.entry_nombre.pack()

        self.etiqueta_edad = tk.Label(self.ventana, text="Edad:", font=("Arial", 12), bg="#F0F0F0")
        self.etiqueta_edad.pack()

        self.entry_edad = tk.Entry(self.ventana, font=("Arial", 12))
        self.entry_edad.pack()

        self.boton_registrar = tk.Button(self.ventana, text="Registrar", font=("Arial", 12), command=self.enviar_datos)
        self.boton_registrar.pack(pady=20)

    def enviar_datos(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()

        if nombre and edad:
            mensaje = f"Nombre: {nombre}\nEdad: {edad}"
            messagebox.showinfo("Registro Exitoso", mensaje)
            self.entry_nombre.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")


if __name__ == "__main__":
    ventana = tk.Tk()
    formulario = RegistroEstudiantesFormulario(ventana)
    ventana.mainloop()
