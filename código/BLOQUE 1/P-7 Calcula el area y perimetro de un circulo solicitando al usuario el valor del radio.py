# Programa 6: Calcula el area y perimetro de un circulo solicitando al usuario el valor del radio
# Fecha: 2024/10/14
# Elaborado por: Valeria Jaqueline Rodarte García

#Solicitar el radio de un círculo
radio = float(input("Introduce el radio de un círculo:"))
#Calcular area
area = (3.1416 * radio **2)
#Mostrar el resultado
print("El área del círculo es: ", str(area))
#Calcular el perimetro
perimetro = (2 * 3.1416 * radio)
#Mostrar el resulted
print("El perimetro del círculo es: ", str(perimetro))
