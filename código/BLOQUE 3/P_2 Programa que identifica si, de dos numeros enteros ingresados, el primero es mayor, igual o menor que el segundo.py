# Programa 2 Programa que identifica si, de dos numeros enteros ingresados, el primero es mayor, igual o menor que el segundo
# Fecha: 2024/10/28
# Elaborado por: Valeria Jaqueline Rodarte García

n1 = input("Ingresa el primer número: ")
n1 = int(n1)    # Convierto a entero el string ingresado desde el teclado  

n2 = int(input("Ingresa el segundo número: "))  # Tambien puedo convertir a entero de esta forma

if (n1 > n2):
    print(str(n1) +" es mayor que " + str(n2))
elif n1 == n2:
    print(str(n1) +" es igual que " + str(n2))
else:
   print(str(n1) +" es menor que " + str(n2)) 

print("¡Gracias por usar mi programa!")
