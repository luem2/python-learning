# List: crea una lista y le pasamos como argumento una lista de elementos (FUNCION)
lista = list(["hola", "crack", 5])  # crear una lista a traves de la funcion.
lista2 = ["hola", "crack", 5]  # crear una lista de forma literal.

print(lista)

# Len: Devuelve el largo de una lista (FUNCION)
print("largo de la lista", len(lista))

# Append: Agrega un elemento a la lista.
lista.append("nuevo")  # Equivale a un push en javascript.
print("elemento nuevo pusheado", lista)

# Insert: Agrega un elemento a la lista en una posicion especifica.
lista.insert(2, "elementoPosicion2")
print("lista con elemento nuevo en posicion especifica", lista)

# Extend: Agrega una lista a otra lista.
lista.extend([25, False])
print("lista concatenada con otra (extend)", lista)

# Pop:  Elimina el ultimo elemento de una lista, dado un indice.
# Si no le pasamos un indice, elimina el ultimo elemento. (Equivalente como parametro -1)
# Retorna el elemento eliminado.
eliminado = lista.pop(0)
print(lista, f"Elemento eliminado: {eliminado}")

# Remove: Elimina un elemento de una lista, por su valor.
# Si no encuentra el valor, lanza una excepcion (error).

lista.remove("elementoPosicion2")
print("lista con elementoPosicion2 eliminado", lista)

# Sort: Ordena una lista de menor a mayor.
newList = [25, 89, 48, 0, -1, -51, -40]
oldList = newList.copy()
newList.sort()

print(f"lista sin modificar {oldList}")
print(f"lista ordenada {newList}")

# Puede recibir una propiedad para que ordene de mayor a menor.
newList.sort(reverse=True)
print("sorted con reverse en true", newList)

# Reverse: Inverte el orden de una lista (en el orden que estaban).
newList.reverse()
print("reversed", newList)

# Index: Devuelve el indice de un elemento de una lista.
# Si no encuentra el elemento, lanza una excepcion.
print("index", newList.index(48))

# Clear:  Elimina todos los elementos de una lista.
lista.clear()
print("cleared", lista)
