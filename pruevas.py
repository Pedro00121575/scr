oficio = ("mecanico", "perro","carro")

personas =[]

for _ in range(1):
    nombre = input("ponga su nombre :")
    apellido = input("ponga su apellido: ")
    edad = int(input("ponga su edad: "))
    oficio = int(input("ponga su oficio (0-mecanico, 1-perro, 2-carro): :"))

    nueva_persona = (nombre, apellido, edad, oficio)
    personas.append(nueva_persona)

    print("")

for persona in personas:
    nombre = persona[0]
    apellido = persona[1]
    edad = persona[2]
    nombre_oficio = oficio[3]

    print(f"SU NOMBRE ES, {nombre} Y SU APELLIDO ES, {apellido} y su edad es {edad} y su oficio es {oficio}")


