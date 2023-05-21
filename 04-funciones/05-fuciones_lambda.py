from typing import Callable

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# En javascript, el equivalente seria una funcion flecha. (=>)

# Las funciones lambda, la podemos utilizar para hacer cosas sencillas, es decir que no son aptas para hacer mas de 1 instruccion. Retorna automaticamente.

# Creando una funcion lambda para multiplicar por dos
# El tipo Callable para indicar que es una funcion. El primer parametro recibe una lista, con el tipo o tipos de argumentos permitidos, y el segundo parametro es el tipo de retorno.

multiplicar_por_dos: Callable[[int | float], int | float] = lambda x: x * 2

print(multiplicar_por_dos(5.8))

# Creando funcion comun que diga si es par o no:


# con -> le indico que retorna la funcion.. (si es que queremos ponerlo explicitamente) -> bool
def esPar(num: int) -> bool:
    return num % 2 == 0


print(esPar(5))  # False

# Usando filter con una funcion comun. Filter es una clase. El primer argumento reciba la funcion, para la cual va a filtrar, y el segundo argumento es el objeto iterable.

numeros_pares = filter(
    esPar, numeros
)  # numeros_pares es un objeto iterable, por lo que podemos convertirlo a una lista.

print(list(numeros_pares))  # 2, 4, 6, 8

# haciendo lo mismo  pero con lambda, pero en esta retorna los numeros impares

numeros_pares = filter(lambda numero: numero % 2 != 0, numeros)
print(list(numeros_pares))  # 1, 3, 5, 7, 9
