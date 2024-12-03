# Programa 6: imprime el area de un triangulo solicitando al usuario el valor de la altura y la base
# Fecha: 2024/10/14
# Elaborado por: Valeria Jaqueline Rodarte García
#Solicitar base y altura del triangulo

base= float(input("Introduce la base del triángulo:"))
altura= float(input("Introduce la altura del triangulo:"))
#Calcular area
area = base * altura / 2
#Mostrar el resultado
print("El área del triángulo es:", str(area))
