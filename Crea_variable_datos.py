# Datos del estudiante
nombre = "Juan Pérez"
edad = 20
carrera = "Ingeniería en Sistemas"

nota1 = 80
nota2 = 90
nota3 = 85

# Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Determinar estado académico
if promedio >= 70:
    estado = "Aprobado"
else:
    estado = "Reprobado"

# Mostrar resultados
print("===== DATOS DEL ESTUDIANTE =====")
print("Nombre:", nombre)
print("Edad:", edad)
print("Carrera:", carrera)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Promedio:", round(promedio, 2))
print("Estado Académico:", estado)