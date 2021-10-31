# Ejercicio 3

import math
r = float(input("Ingrese el radio del círculo: "))
area = math.pi * r ** 2
longitud=2*math.pi*r

print("El área del círculo es: ", area)
print("La longitud del círculo es: ", longitud)


# Un solo decimal
print("\n")
print("El área del círculo es: {:.1f}".format(area))
print("La longitud del círculo es: {:.1f}".format(longitud))
