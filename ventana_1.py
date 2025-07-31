# Se imprta la libreria tkinter con todas sus funciones
from tkinter import *

# -----------------------------
# funciones de la app
# -----------------------------


# -----------------------------
# Ventana principal de la app
# -----------------------------

# Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto de tipo Tk()

ventana_pricipal = Tk()

# Titulo de la ventana
ventana_pricipal.title("Juan Pablo Duran Santos")

# Tamaño de la ventana
ventana_pricipal.geometry("800x500")

# Metodo principal que despliega la ventana en pantalla
ventana_pricipal.mainloop()