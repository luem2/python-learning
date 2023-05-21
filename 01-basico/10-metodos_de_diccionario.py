# Metodos de diccionario
# keys, get, clear, pop, items

diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
}

# --> keys
# Devuelve las claves del diccionario

claves = diccionario.keys()
print(claves)

# --> get
# Devuelve el valor de una clave
# Si no lo encuentra devuelve None (en javascript seria undefined)

valor = diccionario.get("nombre")
print(valor)

# Si buscamos una clave con bracket notation, si no lo encuentra devuelve un error
# diccionar["notfound"] <- Tira error.

# --> pop
# Elimina un elemento del diccionario

diccionario.pop("apellido")
print("diccionario", diccionario)

# --> items
# Devuelve una lista de tuplas con los elementos del diccionario, en el cual podremos iterar.

items = diccionario.items()
print("items", items)

# --> clear
# Elimina todos los elementos del diccionario

diccionario.clear()
print(diccionario)
