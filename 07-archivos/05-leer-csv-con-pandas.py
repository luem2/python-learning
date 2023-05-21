import pandas as pd

# DF = Data frame, son estructuras de datos bidimensionales, similares a hojas de calculo.
# Sus valores son filas y columnas.
df = pd.read_csv("datos.csv")
df2 = pd.read_csv("datos.csv")

print("Data Frame:")
print(df)

# Obteniendo los datos de la columna nombre
nombres = df["nombre"]
print("-------------")
print(nombres)

# Ordenando el dataframe por la edad:
df_ordenado_asc = df.sort_values("edad")
print(df_ordenado_asc)
print("-------------")

# Ordenando por edad de forma descendente:
df_ordenado_desc = df.sort_values("edad", ascending=False)
print(df_ordenado_desc)
print("-------------")

# Concatenando 2 data frames
df_concatenado = pd.concat([df, df2])
print(df_concatenado)
print("-------------")

# Accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)
print(primeras_filas)
print("-------------")

# Accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)
print(ultimas_filas)
print("-------------")

# Accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape
# Es una tupla, en el indice cero se encuentra  la cantidad de filas y en el indice 1 la cantidad de columnas
print(filas_y_columnas_totales)
print("-------------")

# Desempaquetando df.shape
filas, columnas = df.shape
print(f"Hay {filas} filas y {columnas} columnas")
print("-------------")

# Obteniendo data estaditica del dataframe:
df_info = df.describe()
print(df_info)

# Accediendo a un elemento especifico del df con loc:
elemento_especifico_loc = df.loc[2, "edad"]
print("-------------")
print(f"La columna edad, fila 2.. el dato es:{elemento_especifico_loc}")

# Accediendo a un elemento especifico del df con iloc:
elemento_especifico_iloc = df.iloc[2, 1]
print("-------------")
print(f"La columna apellido (1), fila 2.. el dato es:{elemento_especifico_iloc}")

# Accediendo a todos los apellidos con loc:
apellidos = df.loc[:, "apellido"]
print("-------------")
print(f"Todos los apellidos con loc: \n{apellidos}")

# Accediendo a todos los apellidos con iloc:
apellidos = df.iloc[:, 1]
print("-------------")
print(f"Todos los apellidos con iloc: \n{apellidos}")

# Accediendo a la fila 3 con loc:
fila_3 = df.loc[3, :]

# Accediendo a la fila 3 con iloc:
fila_3 = df.iloc[3, :]

print("-------------")
print(f"fila_3: \n{fila_3}")

# Accediendo a filas con edad mayor a 50
mayor_que_50 = df.loc[df["edad"] > 50, :]

print("-------------")
print(f"mayor_que_50: \n{mayor_que_50}")
