# Escribir un programa que pida al usuario dos números
# enteros y muestre por pantalla la <n> entre <m> da
# un cociente <c> y un resto <r> donde <n> y <m> son
# los números introducidos por el usuario, y <c> y <r>
# son el cociente y el resto de la división entera
# respectivamente.

n = input("Ingrese un numero: ")
m = input("Ingrese otro numero: ")

n = int(n)
m = int(m)

c = f"El cociente es: {n/m}"
r = "No sobro nada" if n % m == 0 else f"Sobraron {n%m}"
print(c, r)
