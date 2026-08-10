# Sistema de calificaciones

nombre = input("Ingrese el nombre del estudiante: ")
matricula = input("Ingrese la matrícula: ")
calificacion = float(input("Ingrese la calificación final: "))

# Determinar la calificación literal y el estado
if calificacion >= 90 and calificacion <= 100:
    literal = "A"
    estado = "Aprobó"
elif calificacion >= 80:
    literal = "B"
    estado = "Aprobó"
elif calificacion >= 70:
    literal = "C"
    estado = "Aprobó"
else:
    literal = "F"
    estado = "Reprobó"

# Mostrar los resultados
print("\n===================================")
print("       REPORTE DEL ESTUDIANTE")
print("===================================")
print("Nombre:", nombre)
print("Matrícula:", matricula)
print("Asignatura: Lenguaje de Programación 1")
print("Calificación:", calificacion)
print("Literal:", literal)
print("Estado:", estado)
print("===================================")