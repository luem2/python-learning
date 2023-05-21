# Estos operadores nos devuelven un valor boolean.

a = 5
b = 7
c = 12


def sonIguales(a: int, b: int):
    return a == b


def sonDistintos(a: int, b: int):
    return a != b


def esMayor(a: int, b: int):
    return a > b


def esMenor(a: int, b: int):
    return a < b


def esMayorIgual(a: int, b: int):
    return a >= b


def esMenorIgual(a: int, b: int):
    return a <= b


print(sonIguales(5, 5))
