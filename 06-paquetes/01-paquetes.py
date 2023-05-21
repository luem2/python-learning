import paquete_maths

import paquete_maths.resta as paquete_resta

from paquete_maths.resta import restarNumeroPor5

# Muestra la ruta del paquete, lo identifica gracias a que la carpeta paquete_maths contiene un archivo __init__.py que lo identifica como tal.
print(paquete_maths.__path__)

# Utilizando el metodo resta del paquete
resultadoResta = paquete_resta.resta(5, 2)
print(resultadoResta)

# Utilizando el metodo restarNumeroPor5 del paquete_maths del archivo resta.py
resultadoRestarNumeroPor5 = restarNumeroPor5(25)
print(resultadoRestarNumeroPor5)
