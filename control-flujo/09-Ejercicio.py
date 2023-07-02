print("""
Bienvenido a la calculadora
Para salir, escribe salir
Las operaciones son sum, res, div, mul.
""")
num1 = input("Ingresa un numero: ")

salir = False if str(num1).lower() == "salir" else True

while salir:
    num2 = input("Ingresa otro numero: ")

    if str(num2).lower() == "salir":
        break

    operacion = input("Ingresa la Operacion: ")

    if str(operacion).lower() == "salir":
        break
    elif str(operacion).lower() == "sum":
        resultado = int(num1) + int(num2)
        print(f"El resultado de la Suma es {resultado}")
    elif str(operacion).lower() == "res":
        resultado = int(num1) - int(num2)
        print(f"El resultado de la Resta es {resultado}")
    elif str(operacion).lower() == "mul":
        resultado = int(num1) * int(num2)
        print(f"El resultado de la Multiplicacion es {resultado}")
    elif str(operacion).lower() == "div":
        resultado = int(num1) / int(num2)
        print(f"El resultado de la Division es {resultado}")
    else:
        print("Ingrese una operacion valida")
