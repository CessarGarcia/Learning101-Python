# En un parque de divisiones el costo del ticket de entrada esta dividia de acuerdo a la edad del miño, 
# si el niño tiene menos o igual a 2 años, la entrada es gratis
# si el niño es menor o igual a 6 el costo es de $30
# Si el niño es menor o igual a 10, el costo es de $60
# Si el niño es menor o igual a 16, el costo es de $90
# Cualquier otra edad mayor a 16, el costo es de $100

edad = int(input("Ingrese la edad del niño: "))

if(edad<=2):
    print("La entrada del parque es GRATIS")
elif(edad<=6):
    print("El costo de entrada es de 30 pesos")
elif(edad<=10):
    print("El costo de entrada es de 60 pesos")
elif(edad<=16):
    print("El costo de entrada es de 90 pesos")
else:
    print("El costo de entrada es de 100 pesos")