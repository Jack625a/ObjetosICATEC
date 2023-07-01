import tkinter as tk
import subprocess

def abrir_archivo(archivo):
    subprocess.Popen(["python", archivo])

root = tk.Tk()

# Crear el menú
menubar = tk.Menu(root)

# Crear el menú "Archivo"
menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir Voz", command=lambda: abrir_archivo("voz.py"))
menu_archivo.add_command(label="Abrir Ventana Contenido", command=lambda: abrir_archivo("VentanaContenido.py"))
menu_archivo.add_command(label="Abrir Generación de Imágenes", command=lambda: abrir_archivo("generacionImagenes.py"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Archivo", menu=menu_archivo)

# Configurar el menú en la ventana principal
root.config(menu=menubar)

root.mainloop()
