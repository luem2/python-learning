# Pedir un dato al usuario
# El dato que devuelve, siempre es un string. Aunque le pasemos un numero.
nombre = input("¿Cuál es tu nombre? \n")

print(f"Tu nombre es {nombre}")

# Aca convertimos el input que es un string en un entero y devolvemos el doble del numero.
numero_doble = int(input("Introduce un numero: \n")) * 2

print("Numero doble: ", numero_doble)
