
nombre = "Julio"
apellido = "Alvarez"


# Concatenando textos (esta no es la mejor forma de realizarlo)
nombre_completo = nombre+" "+apellido
print(nombre_completo)

# Una mejor forma de realizarlo es:
nombre_completo2 = f"{nombre} {apellido}"
print(nombre_completo2)

# Ejemplo de f de formateo
print(f"Las iniciales del nombre y apellido {nombre[0]}{apellido[0]}")
