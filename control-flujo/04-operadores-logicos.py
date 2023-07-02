# and, or, not

# AND para que se ejecute ambas condiciones deben ser True
gas = True
encendido = True
if gas and encendido:
    print("Puedes avanzar")

# OR para que se ejecute al menos una debe ser true
gas = False
encendido = True
if gas or encendido:
    print("Puedes avanzar")

# NOT para que se ejecute al menos una debe ser true
gas = False
encendido = True
if not gas or encendido:
    print("Puedes avanzar")

gas = True
encendido = True
edad = 18
if gas and (encendido or edad > 17):  # Se evalua primero lo que esta en parentesis
    print("Puedes avanzar")
