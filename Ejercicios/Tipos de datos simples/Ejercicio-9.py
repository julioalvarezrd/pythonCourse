# Escribir un programa que pregunte al usuario una cantidad
# a invertir, el interés anual y el número de años, y
# muestre por pantalla el capital obtenido en la inversión.

cant = input("Ingrese la cantidad a inverir: ")
tasa = input("Ingrese la Tasa de interes anual: ")
periodo = input("Ingrese la cantidad de años: ")

cant = int(cant)
tasa = int(tasa)
periodo = int(periodo)

total = cant * tasa / 100 * periodo

print(total)
