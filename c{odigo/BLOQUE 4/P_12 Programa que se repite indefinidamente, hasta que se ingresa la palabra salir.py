# Programa 12: Programa que se repite indefinidamente, hasta que se ingresa la palabra salir
# Fecha: 2024/11/8
# Elaborado por: Valeria Jaqueline Rodarte García

# Inicializaciòn de variables
palabra = ""
while True:
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a minúsculas
    print("Usted ingreso: ", palabra)
    if palabra == "salir":
        break

print("Fin del programa\U0001F601 \n\n") # Imprime un emoji feliz
print("¡Hasta luego!\U0001F44B \n\n") # Imprime un emoji de saludo
