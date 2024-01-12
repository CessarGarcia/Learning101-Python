# Solicitar al usuario un numero, y verificar con que numero inicia
# por ejemplo si el numero es 350, impimir el numero inicia con 3

num = input("Ingresa un numero: ")
primer_digito = num[0]
suma = int(primer_digito) + 3
print(f"El numero {num} inicia con {primer_digito} + 3 = {suma}")
