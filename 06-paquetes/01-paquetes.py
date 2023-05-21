import paquete_maths

import paquete_maths.resta as paquete_resta

from paquete_maths.suma import sumarNumeroPor5, sumar

# Muestra la ruta del paquete, lo identifica gracias a que la carpeta paquete_maths contiene un archivo __init__.py que lo identifica como tal.
print(paquete_maths.__path__)

# Utilizando el metodo resta del paquete
resultadoResta = paquete_resta.resta(5, 2)
print(resultadoResta)

# Utilizando el metodo sumarNumeroPor5 del paquete_maths del archivo suma.py
resultado = sumarNumeroPor5(25)
print(resultado)

resultado = sumar(8, 12)
print(resultado)
