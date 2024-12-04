# Programa para calcular el promedio de 5 unidades y verificar si se aprobó o no
# Fecha: 2024/10/24
# Elaborado por: Valeria Jaqueline Rodarte García

# Pide al usuario las calificaciones de las 5 unidades
unidad1 = float(input("Introduce la calificación de la unidad 1: "))
unidad2 = float(input("Introduce la calificación de la unidad 2: "))
unidad3 = float(input("Introduce la calificación de la unidad 3: "))
unidad4 = float(input("Introduce la calificación de la unidad 4: "))
unidad5 = float(input("Introduce la calificación de la unidad 5: "))

# Calcula el promedio
promedio = (unidad1 + unidad2 + unidad3 + unidad4 + unidad5) / 5

# Muestra el promedio
print(f"Tu promedio es: {promedio:.2f}")

# Verifica si aprobó o no la materia
if promedio >= 7:
    print("¡Felicidades! Has aprobado la materia.")
else:
    print("Lo siento, no has aprobado la materia.")
