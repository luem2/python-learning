# Puedo cambiar el orden de los parametros cuando ejecuto la funcion, pero le debo indicar cual es la variable para dicho valor.


def decirFrase(nombre: str, apellido: str, adjetivo: str):
    print(f"Hola, soy {nombre} {apellido} y soy {adjetivo}")


decirFrase(apellido="Gomez", adjetivo="sencillo", nombre="Pedro")
