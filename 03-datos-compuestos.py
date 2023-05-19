# --> 01 - Lista, Tipo de dato List.
lista = ["Luciano", True, 50.8]

print(lista)  # Lista completa
print(lista[2])  # 50.8

# --> 02 - Tupla. Tipo de dato Tupla.
tupla = ("Luciano", True, 50.8)

print("tupla", tupla)  # Tupla completa
print("tupla[2]", tupla[2])  # 50.8

# La listas y las tuplas son estructuras de datos utilizadas para almacenar y organizar elementos en una secuencia ordenada.

# Las tuplas son inmutables. No se pueden modificar los valores de las tuplas.
# Las listas son mutables. Es decir, que pueden ser modificadas.

# tupla[2] = "Hola" (Tira error)  # No se puede modificar el valor de la tupla.
lista[2] = "Hola"
print("Lista[2]", lista[2])  # "Hola"

# --> 03 - Tupla. Tipo de dato Set.
# Creando un conjunto (set)

# No tienen un orden fijo, son elementos desordenados y que pueden cambiar.
# Al igual que la tupla, no podemos modificar sus elementos, pero podemos redifinir si quisieramos la variable con otro conjunto (la tupla tambien se puede redefinir)
# No se puede acceder a un elemento en especifico por indice.
# No se repiten los valores, se omiten los valores repetidos.

conjunto = {"Luciano", "Jorge", True, 50.8}
conjunto = {"pepe", 5}
# conjunto[2] = "Hola" (Tira error)

conjunto = {"pepe", 5, "pepe", 5}
print(conjunto)  # {"pepe", 5}

# Si queremos acceder a los datos de un conjunto, debemos hacerlo con un ciclo for o devolver todo el conjunto.

# --> 04 - Diccionario. Tipo de dato Dictionary.
# El equivalente en Javascript es JSON.

diccionario = {
    "nombre": "Luciano",
    "apellido": "Lopez",
    "edad": 30,
    "profesion": "Ingeniero",
}

print("diccionario", diccionario)  # Diccionario completo
print(diccionario["nombre"])  # Luciano
#  print(diccionario[3])  # Tira error
