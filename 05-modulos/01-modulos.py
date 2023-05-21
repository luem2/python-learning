# Dato interesante: Los modulos integrados de Python estan escritos en C
# Los nombres de los archivos no deben contener guiones medios.

# Es un modulo (namespace)
import modulo_saludar

# Podemos importarlo y asignarle un nickname
import modulo_saludar as ms

# Importar algunas funciones del modulo
from modulo_saludar import saludoEnChino, saludoEnPortugues

print(modulo_saludar.saludar("Jorgito"))
print(ms.saludar("Roberto"))
print(saludoEnChino("Pepe"))
print(saludoEnPortugues("Juan"))

# Tipo de dato de modulo_saludar
print(type(modulo_saludar))

# Para ver las propiedades y metodos de un modulo
print(dir(modulo_saludar))

# Indica el nombre del modulo actual.
print(__name__)  # __main__

# Accedemos al nombre original del modulo.
print(ms.__name__)
