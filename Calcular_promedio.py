# Solicitar datos
nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la Nota 1: "))
nota2 = float(input("Ingrese la Nota 2: "))
nota3 = float(input("Ingrese la Nota 3: "))

# Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Determinar estado
if promedio >= 70:
    estado = "Aprobado"
else:
    estado = "Reprobado"

# Mostrar resultados
print("\n===== RESULTADO =====")
print("Nombre:", nombre)
print("Promedio:", round(promedio, 2))
print("Estado:", estado)