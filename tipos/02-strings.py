nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python,
este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)

# Obtener la longitud que tiene un string en particular.
# Ejemplo len(argumento)
# Argumento son los nombre que le pasamos a una funcion.
print(len(nombre_curso))

# para acceder a un caracter en particular lo podemos hacer
# utilizando la notacion de los [] ejemplo: variable[0]
# recordando que los indices empiezan por 0
print(nombre_curso[0])  # Obtenermos la U
print(nombre_curso[0:8])  # Inicio y fin del indice
print(nombre_curso[8:])  # Desde el indice 8 hasta el final
print(nombre_curso[:8])  # Desde el valor por defecto hasta el indice 8
print(nombre_curso[:])  # Valor por defecto del indice
