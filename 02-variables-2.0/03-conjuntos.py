# Creando un conjunto con set()
conjunto = set(["dato1", "dato2", "dato3"])

print(conjunto)

# Si le paso una lista dentro de un conjunto, me va a tirar error porque no puedo guardar datos que muten, ya que el conjunto es inmutable.
# conjunto = set(["dato1", "dato2", "dato3", [1,2,3]]) <- ERROR.

# Lo que si puedo pasarle es una tupla, ya que no se puede mutar.
conjunto_2 = set(["dato1", "dato2", "dato3", ("dato_tupla1", "dato_tupla2")])

print(conjunto_2)

# Otro dato que no puedo pasarle es un diccionario, ya que tambien puede mutar.
# conjunto2 = set(["dato1", "dato2", "dato3", {"key_diccionario1": "value_diccionario1"}]) <- ERROR.

# Si quisiera guardar un conjunto dentro de otro conjunto. Debo crear un conjunto con la funcion frozenset()
# Y agregarlo al nuevo conjunto.
conjunto = frozenset(["dato1", "dato2"])

conjunto_2 = {conjunto, "dato3"}

print(conjunto_2)

# Teoria de conjuntos

conjunto = {1, 3, 5, 7}
conjunto_2 = {1, 3, 7}

# --> Subconjunto

# El conjunto_2 es subconjunto de conjunto
resultado = conjunto_2.issubset(conjunto)  # True
print(resultado)

# Otra forma de verificar si un conjunto es subconjunto de otro.
resultado = conjunto_2 <= conjunto
print(resultado)

# --> Superconjunto

resultado = conjunto_2.issuperset(conjunto)  # False
print(resultado)

# Otra forma de verificar si un conjunto es el superconjunto de otro.
resultado = conjunto_2 > conjunto  # False
print(resultado)

# Verifica si los conjuntos son totalmente distintos, es decir que no tengan elementos en comun.
resultado = conjunto_2.isdisjoint(conjunto)  # False
print(resultado)
