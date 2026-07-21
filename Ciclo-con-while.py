# Sistema de Registro de Estudiantes

opcion = "S"

while opcion == "S" or opcion == "s":

    matricula = input("Ingrese la matrícula: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    carrera = input("Ingrese la carrera: ")
    calificacion = float(input("Ingrese la calificación final: "))

    print("\n--- Datos del Estudiante ---")
    print("Matrícula:", matricula)
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Carrera:", carrera)
    print("Calificación Final:", calificacion)

    opcion = input("\n¿Desea registrar otro estudiante? (S/N): ")

print("\nRegistro de estudiantes finalizado.")