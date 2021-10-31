# Ejercicio 4:

# Obtener el precio final que se tiene que pagar sí se aplica el 36% de descuento del total de la compra.

precio = float(input("Ingrese el precio de la compra: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

precioFinal = precio-(precio*(descuento/100))

#descuento con un decimal 
print("El precio final es: {:.2f}".format(precioFinal))