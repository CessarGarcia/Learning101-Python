texto = input("Ingresa un texto para calcular el tiempo que tardarías en decirlo: ")
palabras_separadas = texto.split(" ")
cant_palabras = len(palabras_separadas)
duracion = cant_palabras/2

print("-------------------")
print("la frase:",texto)
print("Tiene", cant_palabras,"palabras")
print("Y tardarias en decirlo",duracion,"segundos")
print("-------------------")