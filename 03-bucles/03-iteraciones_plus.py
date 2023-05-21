frutas = ["banana", "manzana", "pera", "uva", "granada", "durazno"]
cadena = "Hola mundo"
numeros = [2, 5, 8, 10]

# Evitando que se coma una granada, con la instruccion continue.
for fruta in frutas:
    if fruta == "granada":
        continue

    print(f"Me voy a comer una {fruta}")
    print("-------------------")

# Evitar que el bucle siga ejecutandose, con la instruccion break.
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")

    if fruta == "pera":
        print("Me comi la pera, y me hizo mal, no como mas...")
        break

else:
    print("Ya no queda nada que comer")

# Recorrer una cadena de texto

for letra in cadena:
    print(letra)

# ----------------------------------------
# For en varias lineas de codigo.

numeros_duplicados: list[int] = list()  # Puedo declararla asi: []

for numero in numeros:
    numeros_duplicados.append(numero * 2)

print(numeros_duplicados)

# For en una sola linea de codigo

numeros_triplicados = [x * 3 for x in numeros]

print(numeros_triplicados)
