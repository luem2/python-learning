import csv


def leerArchivoCSV():
    with open("datos.csv", "r") as archivo:
        reader = csv.reader(archivo)

        for fila in reader:
            print(fila)


leerArchivoCSV()
