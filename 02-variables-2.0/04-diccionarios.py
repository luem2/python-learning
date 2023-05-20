# Creando diccionario con la funcion dict()
diccionario = dict(nombre="Juan", edad=30, email="juancito@gmail.com")

print(diccionario)

# Las listas y los conjuntos no pueden ser claves. Ya que son mutables.
# diccionario = {[1, 2, 3]: "Hola",} <- Error.
# diccionario = {{"Juan", "Jorge"}: "Valor"} <- Error.

# Las tuplas y los frozenset, si pueden ser claves. Ya que son inmutables.
diccionario = {
    (1, 2, 3): "Hola",
    frozenset([1, 2, 3]): "Hola",
    "nombre": "Homero",
    "edad": 47,
    "direccion": "Av. Siempreviva 4002",
}

print(diccionario)

# Creando diccionario con fromkeys(), que es un metodo de la clase dict.

diccionario = dict.fromkeys(["nombre", "edad", "direccion"], "Valor por defecto")

print(diccionario)

diccionario = dict.fromkeys(
    "ABCDE"
)  # Valor por defecto sera None. Y las propiedades la cantidad de letras.

print(diccionario)
