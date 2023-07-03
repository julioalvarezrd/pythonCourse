# Escribir un programa que pregunte al usuario por el número de horas
# trabajadas y el coste por hora. Después debe mostrar por pantalla la
# paga que le corresponde.

horas_trabajadas = input("Ingrese las horas trabajadas: ")
horas_trabajadas = int(horas_trabajadas)
costo_horas = input("Ingrese el costo por hora: ")
costo_horas = int(costo_horas)
print(
    f"El pago total por las horas trabajadas es de RD${horas_trabajadas * costo_horas}")
