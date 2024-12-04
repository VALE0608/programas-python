# Programa 4 Programa que calcule los impuestos que debe pagar un empleado 
# Fecha: 2024/10/29
# Elaborado por: Valeria Jaqueline Rodarte García

ingresos = input("¿Cuáles son sus ingresos?")
ingresos = float(ingresos)

if ingresos <= 1000:
    impuestos = ingresos * 0.05
elif ingresos > 1000 and ingresos <= 2500:
    impuestos = ingresos * 0.08
elif ingresos > 2501 and ingresos <= 6000:
    impuestos = ingresos * 0.12
else:
    impuestos = ingresos * 0.15 

salario_total = ingresos - impuestos
print("Tus impuestos son " + str(impuestos) + " y tu salario final es" + str(salario_total))
