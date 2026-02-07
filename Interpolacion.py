# type: ignore
# ? Entradas de datos
prompt = "Ingresa tu nombre: "
nombre = input(prompt)
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))

#print(nombre + " " + apellido)  # Concatenación
print(f"Hola, mi nombre es {nombre} y mi apellido es {apellido}")  # Interpolación
