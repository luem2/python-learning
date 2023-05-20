# If Else


def esMayorDeEdad(edad: int):
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")


print(esMayorDeEdad(20))

# Else if (elif)


def ingresoMensual(ingreso: int):
    if ingreso >= 5000:
        print("Tiene un ingreso mensual superior a 5000")
    elif ingreso >= 3000:
        print("Tiene un ingreso mensual superior a 3000")
    else:
        print("Tiene un ingreso mensual inferior a 3000")


print(ingresoMensual(3000))
