import tkinter as tk
from tkinter import messagebox

# Fromato de mi ventana principal
ventana = tk.Tk()
ventana.title("Ventana de mi trabajo")
ventana.geometry("300x300")
ventana.resizable



def mostrar_informacion():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    carrera = entrada_carrera.get()

    if nombre.strip() == "":
        messagebox.showwarning("Advertencia", "Por favor, escribe tu nombre y las demas informacion.")
    else:
        messagebox.showinfo("Informacion", f"Aqui tu informacion,     Tu nombre es {nombre} \n y tu tienes {edad} años de edad y tu carrera es Ing de {carrera}")


# etiqueta para el label de texto escribe tu nombre 
P1_nombre = tk.Label(ventana, text="Escribe tu nombre:")
P1_nombre.pack(pady=30)


entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

P2_Edad = tk.Label(ventana, text="Escribe tu Edad:")
P2_Edad.pack(pady=10)

entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack()

P3_carrera = tk.Label(ventana, text="Escribe tu Carrera:")
P3_carrera.pack(pady=10)

entrada_carrera = tk.Entry(ventana, width=30)
entrada_carrera.pack()


# Botón
btn_mostrar = tk.Button(ventana, text="Aceptar", command=mostrar_informacion)
btn_mostrar.pack(pady=20)


ventana.mainloop()