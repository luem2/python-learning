# Funciones build-in (integradas) que tiene python para reutilizar.

numeros = [4, 8, 1, 58, 25]

# Encontrando el numero mayor de una lista o tupla.
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrando el numero menor de una lista o tupla.
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando el numero con tres decimales.
numero_redondeado = round(15.549281, 3)
print(numero_redondeado)

# Retorna False => 0, datos vacios, False, None, "".
# Retorna True => distinto de 0, True, cadena con caracteres, datos no vacios.

print("bool() de diccionario vacio", bool({}))  # False
print("bool() de lista con 1 elemento", bool(["asd"]))  # True

# Retorna True, si todos los valores de un iterable, son verdadero.

print("all() de lista con elementos verdaderos", all(["texto", 1, [5, 8]]))  # True
print("all() de lista con 1 elemento negativo", all(["asd", "asd", 0]))  # False

# Suma todo los valores de un iterable.
print("suma de todos los elementos de la lista numeros: ", sum(numeros))
