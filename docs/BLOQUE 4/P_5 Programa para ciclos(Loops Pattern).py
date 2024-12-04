# Programa 5: Programa para ciclos(Loops Pattern)
# Fecha: 2024/11/5
# Elaborado por: Valeria Jaqueline Rodarte García
print("Loops Pattern")
letras = ["a", "b", "c", "d", "e"]
contador = 0

for letra in letras:
    contador = contador + 1
print("La lista\"letras\"tiene", contador, "letras")

print("\nThe sum pattern")
numeros = [100, 200, 300, 400]
sumatoria = 0

for numero in numeros:
    sumatoria = sumatoria + numero
print("La sumatoria es", sumatoria)

print("\nThe accumulation pattern")
palabras = ["Hoy", " ", "hace", " ", "frío"]
mensaje = " "
for palabra in palabras:
    mensaje = mensaje + palabra
print(mensaje)

print("\nThe Map Parttern")
lista_anterior = ["Manzana", "Piña", "Uva"]
lista_nueva = []
print("La lista vacía", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es", lista_nueva)
