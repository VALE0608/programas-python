# Programa 11: Programa que se repite hasta que el usiario ingresa la palabra "salir"
# Fecha: 2024/11/8
# Elaborado por: Valeria Jaqueline Rodarte García

# Inicializaciòn de variable
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() #  Convierte la palabra a minusculas
    print("Usted ingreso: ", palabra)
print("Fin del programa")
