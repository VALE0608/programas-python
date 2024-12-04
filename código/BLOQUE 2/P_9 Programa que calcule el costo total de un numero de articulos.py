# Programa que calcule el costo total de un numero de articulos si:
# Son 3 articulos o menos precio unitario: $45.00 
# Mas de 3 articulos, precio unitario: $30.00
# Fecha: 2024/10/25
# Elaborado por: Valeria Jaqueline Rodarte García

cantidad = int(input("¿Cuántos articulos compro? "))

if cantidad > 3:
    total = cantidad * 30

else: 
    total = cantidad * 45

print("El total a pagar es: $" + str(total))
print("Gracias por su compra!!!\U0001F600")
