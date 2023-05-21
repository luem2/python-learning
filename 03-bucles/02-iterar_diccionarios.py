diccionario = {
    "nombre": "Ismael",
    "apellido": "Gutierrez",
    "edad": 59,
    "profesion": "Ingeniero",
}

print(diccionario)

# Iterando las llaves del diccionario:

for key in diccionario:
    print(f"Key: {key}")

# Iterando los items del diccionario
# Esto nos devuelve por cada par llave, valor. Una tupla, en el indice cero, su llave y en el indice 1 su valor.

for item in diccionario.items():
    print(f"Item: {item}")
