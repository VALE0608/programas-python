# Programa 6: Programa que permita crear una lista de todos los numeros menores a 50
# Fecha: 2024/11/6
# Elaborado por: Valeria Jaqueline Rodarte García

print("The filter pattern(filtros)")
numeros = [10, 50, 25, 13, 10, 28, 100, 500, 29, 29]
menores_50 = [ ] # crea una lista vacía
for numero in numeros:
    if numero < 50:
        menores_50.append(numero)
print("La lista original es: ", numeros)
print("La nueva lista es: ", menores_50)
