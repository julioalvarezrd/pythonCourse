# Ejercicio de Calculadora Mejorado
print("""
Bienvenido a la calculadora
Para salir, escribe salir
Las operaciones son sum, res, div, mul.
""")
resultado = ""  # declaramos como un strings vacio fuera del buble
while True:
    if not resultado:  # se evaluara como falso ya que esta vacio
        # no pedira que ingresemos el numero
        resultado = input("Ingrese número: ")
       # esto convierte lo que el usuario ingreso en minusculas
       # y evalua si el usuario escribio salir
        if resultado.lower() == "salir":
            break  # si el usuario escribio salir el break nos saca del buble
        # De lo contrario resultado se convierte en un numero entero
        resultado = int(resultado)

    # Solicitamos el tipo de operacion la convertimos en minusculas y
    # evaluamos si es igual a salir, si es igual se ejecutara el break
    op = input("Ingrese operacion: ")
    if op.lower() == "salir":
        break

    # solicitamos numero lo convertimos en munusculas y evaluamos
    # si es igual a salir, si es igual se ejecutara el break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)  # En caso de que sea un numero sera convertido a entero

    # en este bloque convertiremos la operacion que ingreso el
    # usuario en minusculas y comparar a que operacion corresponde
    if op.lower() == "sum":
        resultado += n2
    elif op.lower() == "res":
        resultado -= n2
    elif op.lower() == "mul":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break
    print(f"El resultado es {resultado}")
