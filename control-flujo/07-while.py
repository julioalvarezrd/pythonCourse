numero = 1
while numero < 100:
    print(numero)
    numero *= 2

# Otro ejemplo de While
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# Loops Infinitos
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
