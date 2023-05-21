# Dir: Es una funcion de python que muestra los metodos disponibles para una variable, o lo que le pasemos por argumento.
# print(dir(cadena1))

# Upper: Convierte el string a mayusculas.
print("como estas crack".upper())

# Lower: Convierte el string a minusculas.
print("COMO ESTAS CRACK".lower())

# Capitalize: Convierte el primer caracter en mayuscula y lo demas lo convierte en minusculas.
print("bienvenido Crack, Winner, Mastodonte".capitalize())

# Find: Buscamos un string en otra string. Devuelve el indice donde se encuentra. Si devuelve -1 es que no lo encontro.
print("como estas crack".find("como"))  # Devuelve 0

# Index: Igual que el find, la diferencia es que si no encuentra el string devuelve una exepcion (error).
print("como estas crack".index("estas"))  # Devuelve 5

# IsNumeric: Comprueba si el string es numerico.
print("123".isnumeric())  # Devuelve True, aunque sea un string, lo convierte a numero.

# IsAlpha: Comprueba si el string es alfabetico, es decir, no contenga numeros NI TAMPOCO caracteres especiales.
print(
    "soy un pollo".isalpha()
)  # False, porque contiene espacios que es un caracter especial.

# IsAlphaNumeric:  Comprueba si el string es alfanumerico, es decir, contiene numeros y/o letras. Si contiene otro caracter devuelve false.
print("Tengo 22 perros, en casa".isalnum())  # False (contiene espacios)
print("123#".isalnum())  # False

# Count: Cuenta las coincidencias de lo que le pasemos por parametro en una cadena, devuelve la cantidad de coincidencias.
print("como estas crack".count("o"))  # Devuelve 2

# Len: Devuelve la longitud de la cadena.
# Len es una funcion de python que devuelve la longitud de una cadena. NO UN METODO.
print(len("como estas crack"))  # Devuelve 16

# Startswith: Comprueba si una cadena empieza con lo que le pasemos por parametro. Devuelve un booleano.
print("como estas crack".startswith("Como"))  # Devuelve False (Es case sensitive)

# EndsWith: Comprueba si una cadena termina con lo que le pasemos por parametro. Devuelve un booleano.
print("como estas crack".endswith("crack"))  # Devuelve True.

# Replace: Reemplaza una cadena por otra. (en todas las coincidencias)
print(
    "como estas crack, como estas hoy?".replace("como", "hola")
)  # Devuelve hola estas crack, hola estas hoy?
print(
    "como estas crack".replace("pepe", "hola")
)  # Devuelve la cadena ya escrita, ya que no encuentra la cadena pepe.

# Split: Divide una cadena en varias partes. Devuelve una lista.
print("como estas crack".split(" "))  # Devuelve ['como', 'estas', 'crack']
