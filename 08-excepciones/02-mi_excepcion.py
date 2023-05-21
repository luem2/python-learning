# Creando mi propia excepcion personalizada:
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")


# Lanzando mi propia excepcion:
# raise MiExcepcion("Error de ejemplo")

# Manejando la excepcion:
try:
    raise MiExcepcion("Error de ejemplo")
except:
    print("Como la pifiaste maquinola")

# El equivalente al except en Javascript es el "catch".
# El equivalente al raise en Javascript es el "throw".
