import re

texto = """Hola maestro, esta es la cadena 1. Como estas mi rey?
Esta es la segunda linea de texto (linea 2) mi rey.
Y Esta es la final (linea 3) definitiva mi capitan.
tengo 250 pesos en la cartera, pero 200 en realidad me compre un chupetin
"""

# Devuelve el primer resultado que encuentra
resultado = re.search("rey", texto)

# Devuelve todos los resultados que encuentra en una lista.
resultado = re.findall("Esta", texto)

# --> REGEX:

# \d -> Busca digitos numericos del 0 - 9
resultado = re.findall(r"\d", texto)

# \D -> Busca TODO lo que no sea digitos numericos del 0 - 9
resultado = re.findall(r"\D", texto)

# \w -> Busca letras y numeros del a - z, A - Z, 0 - 9 (alfanumericos) y tambien el guion bajo "_"
resultado = re.findall(r"\w", texto)

# \W -> Busca TODO menos los caracteres alfanumericos.
resultado = re.findall(r"\W", texto)

# \s -> Busca espacios en blanco (espacios, tabs, saltos de linea)
resultado = re.findall(r"\s", texto)

# \S -> Busca TODO menos los espacios en blanco
resultado = re.findall(r"\S", texto)

# . -> Busca TODO menos saltos de linea. (Lo contrario seria la regex de abajo)
resultado = re.findall(r".", texto)

# \n -> Busca saltos de linea.
resultado = re.findall(r"\n", texto)

# \ ->  Cancela caracteres especiales, cancelando la funcion del punto (Que es buscar TODO menos saltos de linea) y busca todos los puntos.
resultado = re.findall(r"\.", texto)

# Armando una cadena que busque un numero, seguido de un punto y espacio:
resultado = re.findall(r"\d\.\s", texto)

# Buscando el principio de una linea
# flags=re.M activa la multilinea
resultado = re.findall(r"^Hola", texto)  # Si, lo encuentra y lo devuelve

# Buscando el final de una linea
resultado = re.findall(r"capitan.$", texto, flags=re.M)

# {n} -> Busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
resultado = re.findall(r"\d{3}", texto)

# {n,m} -> busca al menos n, y como maximo m veces.
resultado = re.findall(r"\d{2,4}", texto)

# | -> busca una cosa o la otra
resultado = re.findall(r"maestro|rey", texto)

print(resultado)
