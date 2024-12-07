# Programa 13: Nombre, edad y calificación
# Fecha: 2024/11/12
# Elaborado por: Valeria Jaqueline Rodarte García

nombre = "Edinguer"
edad = 27
calificación = 93.8

# Método 1: Concatenación con conversión explícita
print("Mi nombre es: " + nombre + ", mi edad es: " + str(edad) + ", mi calificación es: " + str(calificación))

# Método 2: Uso de f-strings
print(f"Mi nombre es: {nombre}, mi edad es: {edad}, mi calificación es: {calificación}")

# Método 3: Uso de formato antiguo (%)
print("Mi nombre es: %s, mi edad es: %d, mi calificación es: %.2f" % (nombre, edad, calificación))
