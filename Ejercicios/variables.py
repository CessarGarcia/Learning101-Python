# Crea 3 variables que almacene el nombre, el teléfono y el correo electrónico,
# imprime los datos y además especifica el espacio donde esta almacenada la variable 
# y el tipo de variable que es 
nombre: str = "Juan Perez"
telefono: str = "902066047"
correo: str = "hola_soyjuan123@perez.com"

print(f"El nombre es: {nombre}")
print(f"El telefono es: {telefono}")
print(f"El correo es: {correo}")

print(f"La variable nombre esta almacenada en: {id(nombre)}")
print(f"La variable telefono esta almacenada en: {id(telefono)}")
print(f"La variable correo esta almacenada en: {id(correo)}")

print(f"La variable nombre es de tipo: {type(nombre)}")
print(f"La variable telefono es de tipo: {type(telefono)}")
print(f"La variable correo es de tipo: {type(correo)}")