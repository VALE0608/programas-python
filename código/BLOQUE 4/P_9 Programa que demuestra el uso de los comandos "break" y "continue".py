# Programa 9: Programa que demuestra el uso de los comandos "break" y "continue"
# Fecha: 2024/11/8
# Elaborado por: Valeria Jaqueline Rodarte García

# Ejemplo 1 - break
# Imprimir los numeros del 1 al 10 pero si el numero es 5, salir del ciclo while

print("Comando break")
i = 1
while i <= 10:
    if i == 5:
       break
    print(i)
    i += 1 # Equivalente a i = i + 1
print("Fin del programa")


# Ejemplo 2 - continue
# Imprimir los numeros del 1 al 10 pero si el numero 5, omitirlo

print("\nComando continue")
i = 1
while i <= 10:
    if i == 5:
       continue
    print(i)
    i += 1 # Equivalente a i = i + 1
print("Fin del programa")
