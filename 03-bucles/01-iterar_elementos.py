# En python, los bucles son for in.
# Todo esto funciona igual que con tuplas, excepto en el caso en donde se usa la manera no optima de recorrer una lista.

animales = ["perro", "gato", "pajaro"]
numeros = [10, 62, 53]

# Recorriendo la lista animales
for animal in animales:
    print(f"En esta iteracion, la variable animal es igual a {animal}")

# Recorriendo la lista numeros y multiplicando cada elemento por 2
for numero in numeros:
    resultado = numero * 2
    print(resultado)

# Para iterar 2 listas a la vez con la funcion zip()
# Se recorren las listas al mismo tiempo. Devuelven los primeros elementos de la correspondiente lista y asi sucesivamente.

for animal, numero in zip(animales, numeros):
    print(f"Reccoriendo lista 1: {animal}")
    print(f"Reccoriendo lista 2: {numero}")

# Recorriendo un rango de numeros:
# El primero del rango esta incluido, el ultimo no.

for numero in range(15, 20):
    print(numero)

# Si le ponemos un solo parametro, recorre del 0 hasta el parametro indicado.

for numero in range(5):
    print(numero)

# Forma no optima de recorrer una lista: IMPORTANTE: No funciona para recorrer conjuntos

for num in range(len(numeros)):
    print(f"Forma no optima: {numeros[num]}")

# Forma correcta de recorrer una lista con su indice:
# Devuelve por cada elemento, una tupla con el indice y el elemento.

for num in enumerate(numeros):
    print("-------------")
    print(f"Tupla: {num}")
    print(f"Indice: {num[0]}")
    print(f"Elemento: {num[1]}")


# Desempaquetando la tupla directamente en el for:

for i, num in enumerate(numeros):
    print(f"Desempaquetando la tupla: indice:{i} numero:{num}")

# Usando el for/else
# El else se ejecuta cuando termina el bucle for. Se ejecuta al menos 1 vez, y al terminal el bucle, aunque no entre.
# funciona igual con las tuplas.

for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")

else:
    print("Fin del bucle for")
