# Creando funcion que suma numeros
def sumarDos():
    # Iniciando un bucle
    while True:
        # Pidiendo al usuario 2 numeros
        a = input("Ingrese un numero: ")
        b = input("Ingrese otro numero: ")

        # Intentando convertir a entero los numeros
        try:
            resultado = int(a) + int(b)

        # Si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print(f"Error, debe ingresar un numero\nERROR: {e}")

        # Si todo salio bien, sale del bucle
        else:
            break

    return resultado


print(f"La suma es: {sumarDos()}")
