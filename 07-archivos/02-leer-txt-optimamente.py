# Abriendo el archivo con with open
# Esta forma es mejor, ya que consume menos recursos y es mas rapido. Cierra automaticamente el archivo.


def leerArchivo():
    with open("./texto.txt", "r", encoding="UTF-8") as archivo:
        # Leemos el archivo y lo asignamos a una variable
        contenido = archivo.read()

        # Mostramos el contenido del archivo
        print(contenido)


leerArchivo()
