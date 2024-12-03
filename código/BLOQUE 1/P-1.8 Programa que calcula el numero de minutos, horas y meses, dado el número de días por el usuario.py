# Realice un programa que calcule el numero de minutos, horas y meses, dado el número de días por el usuario
# Fecha: 2024/10/16
# Elaborado por: Valeria Jaqueline Rodarte García
dias = int(input("Introduce el número de dias:"))
horas = dias * 24
minutos = horas * 60
meses = dias / 30

print("El numero de minutos es:", (minutos))
print("El numero de horas es:", (horas))
print("El numero de meses es:", (meses))
