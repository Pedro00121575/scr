# Datos del estudiante
nombre = "María Pérez"
matricula = "2025-1234"
carrera = "Ingeniería de Software"
calificacion = 85

# Determinar el estado
if calificacion >= 70:
    estado = "APROBADO"
else:
    estado = "REPROBADO"

# Mostrar el reporte
print("===================================")
print("       REPORTE DEL ESTUDIANTE")
print("===================================")
print("Nombre:", nombre)
print("Matrícula:", matricula)
print("Carrera:", carrera)
print("Calificación:", calificacion)
print("Estado:", estado)
print("fin del reporte")
print("===================================")