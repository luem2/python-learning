# Forma no optima de sumar valores:


def suma(lista: list[int | float]):
    total: int | float = 0

    for num in lista:
        total += num

    return total


suma_1 = suma([5, 4, 2, 1, 3.5])
print("Forma no optima: ", suma_1)

# ---------------------------------------


def sumaOptima(nombre: str, *numeros: int | float):
    # numeros es una tupla.. por el operador *.
    return f"Hola {nombre}, la suma de tus numeros son:{sum(numeros)}"


suma_2 = sumaOptima(
    "Juan", 5, 4, 2, 1, 3.5
)  # puedo agregar, tantos numeros como quisiera.
print("Forma optima: ", suma_2)
