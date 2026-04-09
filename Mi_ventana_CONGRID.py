# type:ignore
import tkinter as tk
from dotenv import load_dotenv
import os
from tkinter import messagebox
    
load_dotenv()
user_password = os.getenv("USER_PASSWORD")

def capturar_valor():
    valor_usuario = campo_entrada_usuario.get()
    valor_password = campo_entrada_password.get()
    print(valor_usuario, valor_password)

    if  valor_usuario == "pedro" and valor_password == "1":
        messagebox.showinfo("Acceso", "Login correcto")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = tk.Tk()  
ventana.title("Mi primera ventana en tkinter")
ventana.geometry("600x400")

label_informacion = tk.Label(ventana, text="Bienbenido a mi pequeña ventana",border=10, foreground="#000000", font=("Arial",20))
label_informacion.grid(row=1 ,padx=75, pady=10)

# Label o texto que se muestra
label_usuario = tk.Label(ventana, text="Usuario",border=10, foreground="#000000",font=("Arial",18, "bold"))
label_usuario.grid(row=2, padx=5, pady=5)

campo_entrada_usuario = tk.Entry(ventana, font=("Arial", 16))
campo_entrada_usuario.grid(row=3,padx=1,pady=10)

label_password = tk.Label(ventana, text="Password", border=10, font=("Arial", 18, "bold"))
label_password.grid(row=4,padx=1,pady=5)

campo_entrada_password = tk.Entry(ventana, show="😐", font=("Arial", 16, "bold"))
campo_entrada_password.grid(row=5,pady=10)

# Botón
boton = tk.Button(ventana, text="Iniciar",border=10 ,width=12, height=2 , command=capturar_valor)
boton.grid( row=6,padx=1,pady=5)

# Bucle principal
ventana.mainloop()