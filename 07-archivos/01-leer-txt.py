# Usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("./texto.txt", encoding="UTF-8")

# NOTA IMPORTANTE: Una vez que uso algun metodo para leer el archivo, no puedo usar otro metodo para leerlo, a menos de que abra de nuevo el archivo, con open()

# Leer el archivo completo:
# print(archivo.read())

# Lee linea por linea y lo devuelve en una lista:
# print(archivo.readlines())

# Leer una sola linea, se le puede pasar un int como parametro, para indicarle hasta cuantos caracteres puede leer.
print(archivo.readline())

# Cerrar el archivo
# Siempre se debe cerrar el archivo al terminar de usarlo.
archivo.close()
