# Programa que identifica el tipo real de dato
# Fecha: 21/11/24
# Elaborado por: Valeria Jaqueline Rodarte García

mensaje = input("Escribe algo: ")

try:
    # Intentar convertir a entero
    valor = int(mensaje)
    print("El tipo de dato es: Entero (int)")
except ValueError:
    try:
        # Intentar convertir a flotante
        valor = float(mensaje)
        print("El tipo de dato es: Decimal (float)")
    except ValueError:
        # Verificar si es booleano
        if mensaje.lower() in ['true', 'false']:
            print("El tipo de dato es: Booleano (bool)")
        else:
            print("El tipo de dato es: Cadena de texto (str)")
