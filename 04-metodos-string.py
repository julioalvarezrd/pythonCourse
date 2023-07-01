# Un metodo es un a funcion que se encuentra dentro de un objeto

animal = "chanCHIto fEliz"
animal2 = "    ChanCHIto TriSte    "
print(animal.upper())  # con este metodo convertimos a mayusculas
print(animal.lower())  # con este metodo convertimos de minusculas
print(animal.capitalize())  # con este metodo convertimos a Capitalize
print(animal.title())  # con este metodo convertimos a Title

print(animal2)
# con este metodo eliminamos los espacios de la izquierda y derecha
print(animal2.strip())  # izquierda y derecha
print(animal2.rstrip())  # derecha
print(animal2.lstrip())  # izquierda

# Encadenando metodos
print(animal2.strip().title())

# Buscando el indice en un string
# si no encuantra el lo que pedimos buscar nos arroja -1
print(animal.find("an"))

# remplazando caracteres en un strings y convertirlo en titulo
print(animal.replace("CH", "j").title())

# Viendo si se encuentra una cadena dentro de nuestra variable
print("nCH" in animal)  # True

# Viendo si no se encuentra una cadena dentro de nuestra variable
print("nCH" not in animal)  # False
