from typing import Literal


# Creando una funcion simple:
def saludarSimple():
    print("Hola papu")


saludarSimple()


# Creando una funcion con parametros:
def saludarConParametros(nombre: str, sexo: Literal["hombre", "mujer"]):
    adjetivo: str

    if sexo == "mujer":
        adjetivo = "bella"
    else:
        adjetivo = "titan"

    print(f"Hola {nombre} como estas {adjetivo}?")


saludarConParametros("Jorge", "hombre")

# Crear una funcion que nos retorne la password y el numero ingresado: (Devuelve una tupla)


def crear_password_debil(num: int):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])

    c1 = num - 2
    c2 = num
    c3 = num - 5

    return f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}", num


password_creada, num_ingresado = crear_password_debil(
    3
)  # Desempaquetando la tupla que devuelve la funcion

print(f"La password es {password_creada} y el numero ingresado fue {num_ingresado}")
