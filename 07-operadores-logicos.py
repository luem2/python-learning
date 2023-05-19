# AND


def ambosNumerosSonPositivos(a: int, b: int):
    return a > 0 and b > 0


print(ambosNumerosSonPositivos(2, -5))  # False

# OR


def algunoEsPositivo(a: int, b: int):
    defin = a > 0 or b > 0

    return defin


print(algunoEsPositivo(0, 1))  # True

# NOT en Javascript es el signo !


def bandera(bandera: bool):
    return not bandera


print(bandera(True))  # False

# ----------------------------------
# Los operadores &, y | se usan para realizar operaciones a nivel de bits (bitwise).

# "Los operadores & y | se utilizan comúnmente en situaciones donde es necesario realizar manipulaciones a nivel de bits, como en algoritmos de codificación, criptografía, manipulación de datos binarios o cuando se trabaja directamente con representaciones binarias de números."

print(ambosNumerosSonPositivos(2, 5) & bandera(False))  # True
