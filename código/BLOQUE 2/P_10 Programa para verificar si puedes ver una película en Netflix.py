# Programa para verificar si puedes ver una película en Netflix

# Solicita al usuario si compró la película
compra_pelicula = input("¿Has comprado la película? (si/no): ")

# Verifica si el usuario compró la película
if compra_pelicula == "si":
    # Si ha comprado la película, solicita su edad
    edad = int(input("¿Cuál es tu edad? "))

    # Verifica si el usuario es mayor de edad
    if edad >= 18:
        print("Puedes ver la película en Netflix. ¡Disfruta!")
    else:
        print("Lo siento, no tienes la edad suficiente para ver esta película.")
else:
    # Si no ha comprado la película
    print("No puedes ver la película porque no la has comprado.")
