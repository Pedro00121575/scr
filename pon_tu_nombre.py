import tkinter as tk
from tkinter import messagebox

# Fromato de mi ventana principal
ventana = tk.Tk()
ventana.title("Ventanamostrar info")
ventana.geometry("400x400")
ventana.resizable

nombreusuario = str("Juan perez")
edadusuario = int(20)
carrerausuario = str(" Ingeniería de Software")
Ciudadusuario = str("Santo Domingo")


def mostrar_informacion():
   
    if nombreusuario  == str("perez"):
        messagebox.showwarning("Advertencia", "Por favor, escribe tu nombre y las demas informacion.")
    else:
       print("Informacion", f"Aqui tu informacion, Tu nombre es {nombreusuario} \n y tu tienes {edadusuario} años de edad y tu carrera  {carrerausuario} \ny esta viviendo en {Ciudadusuario}")


# etiqueta para el label de texto escribe tu nombre 

# Botón
btn_mostrar = tk.Button(ventana, text="Aceptar", command=mostrar_informacion)
btn_mostrar.pack(pady=20)


ventana.mainloop()