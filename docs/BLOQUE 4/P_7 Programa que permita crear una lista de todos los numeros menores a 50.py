# Programa 7: Programa que permita crear una lista de todos los numeros menores a 50
# Fecha: 2024/11/7
# Elaborado por: Valeria Jaqueline Rodarte García
edades =  [10, 15, 18, 8, 36, 25, 67, 89, 95, 43, 26, 10, 65, 55, 81, 90]
menores_18 = []
adultos = []
mayores_65 = []


for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad >= 18 and edad < 65:
        adultos.append(edad)
    else:
        mayores_65.append(edad)
# Imprimir resultados
print("\n\U0001F600 La lista de edades es: ", edades)
print("\n\U0001F600 La lista de menores es: ", menores_18)
print("\n\U0001F600 La lista de adultos es: ", adultos)
print("\n\U0001F600 La lista de adultos mayores es: ", mayores_65)
