# Programa que calcula los impuestos de un valor
# Fecha: 2024/10/22
# Elaborado por: Valeria Jaqueline Rodarte García
def calcular_impuesto(valor, tasa_impuesto):
    impuesto = valor * (tasa_impuesto / 100)
    return impuesto

valor = float(input("Introduce el valor: "))
tasa_impuesto = float(input("Introduce la tasa de impuesto en %: "))

print(f"El impuesto sobre {valor} con una tasa del {tasa_impuesto}% es: {calcular_impuesto(valor, tasa_impuesto):.2f}""\nGracias por usar nuestro sistema")
