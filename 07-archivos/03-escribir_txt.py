# La clausula o keyword "with" se utiliza en una declaracion conocida como "context manager" (administrador de contexto),. El objetivo principal de "with" es simplificar la gestion de recursos al garantizar que ciertos objetos se inicialicen y se liberen adecuadamente.


def sobreEscribirElArchivo():
    # Abrimos el archivo con with open, el segundo parametro es la forma en que se abrira el archivo. En este caso es de escritura (write), es decir que sobreescribe el archivo.
    with open("./texto.txt", "w", encoding="UTF-8") as archivo:
        # Sobreescribe el archivo con esta linea:
        # archivo.write("Hola, soy el texto nuevo UWU")

        # Recibe como parametro un iterable, de strings.
        archivo.writelines(["Hola, soy una linea nueva\n", "Y esta es otra\n"])


def escribirLineasEnArchivo():
    # Recibe como segundo parametro "a" (append), que agrega 5 lineas nuevas.
    with open("./texto.txt", "a", encoding="UTF-8") as archivo:
        for i in range(5):
            archivo.write(f"Esta es la linea numero: {i}")
            archivo.write("\n")


# sobreEscribirElArchivo()
escribirLineasEnArchivo()
