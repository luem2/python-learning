# ----- IMPORTANTE -----
# Para la definicion de variables en Python, a contra posicion con Javascript, se recomienda utilizar snake case.
# Recomendacion oficial de la documentacion de Python.

# EJEMPLO:
nombre_completo = "Juan Perez"
ciudad_de_residencia = "Bogota"

# Mostar Hola mundo por consola.
print("Hola mundo")

# Datos simples:

nombre = "Juan"  # string
multipleLineas = """Este texto esta
en multiples
lineas.
"""  # multiple strings, equivalente a las template strings en javascript.
edad = 30  # int
estatura = 1.70  # float
hombre = True  # boolean (True or False)
bienvenida = f"Hola como estas {nombre}, todo bien?"

# Concatenacion: (F String)
# Lo que hace es convertir el tipo de dato a string y concatenarlo con otra cadena.

print(f"Tu edad es {edad}, tu estatura es {estatura} y eres hombre? {hombre}")

# Para borrar una variable:
del nombre
# print(nombre)  # No se puede imprimir ya que la variable ya fue borrada.

# Operadores de pertenencia (in, not in) devuelve un booleano. Busca el string "ola" en la cadena de texto.
# Es de tipo, Case Sensitive. Se respeta las minusculas y las mayusculas.
print("ola" in bienvenida)  # Devuelve True.
print("ola" not in bienvenida)  # Devuelve False.
