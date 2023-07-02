# Iterar una lista de elementos

for numero in range(5):
    print(numero, numero * 'hola mundo: ')

# probando for else
buscar = 2
for i in range(5):
    print(i)
    if i == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontrado")

# iterando un string
for char in "Julio Alvarez":
    print(char)
