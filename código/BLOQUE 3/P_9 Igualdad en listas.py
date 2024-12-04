# Programa 9: Igualdad en listas. Compare con todas las demas listas 
# Fecha: 2024/10/31
# Elaborado por: Valeria Jaqueline Rodarte García

puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]

print(puntos == puntos_2) #True
print(puntos == ordenados) #Flase
print(puntos == puntos_texto)#Flase

print(puntos != puntos_2)#Flase
print(puntos != ordenados) #True
print(puntos != puntos_texto) #True
