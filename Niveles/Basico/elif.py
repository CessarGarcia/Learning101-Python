# En un cine se quiere verificar el descuento que se hara de acuerdo a la cantidad comprada y si cuenta con membresia
# Ademas como segundo requisito, el descuento solo aplica si el dia de compra es el martes o jueves

# Si el cliente gasta menos de $300, hacer un rebaje del 5%
# si el cliente gasta mayor o igual de $300, hacer un descuento del 7%
# Si cuenta con membresia hacer un descuento del 5% adicional


total_gastado = float(input("Ingresa el total gastado: "))

# Convertir el texto ingresado a MAYUSCULAS
es_miembro = input("¿Cuenta con membresia? ").upper()

# Convertir el texto ingresado a MAYUSCULAS
es_dia = input("¿El dia es martes o jueves? ").upper()

if(es_dia == "SI"):
    if(total_gastado<300):
        descuento = total_gastado * 0.05
    else:
        descuento = total_gastado * 0.07
    if(es_miembro == "SI"):
        descuento += total_gastado * 0.05
    
    total = total_gastado - descuento
    print("Total a pagar con descuento: ", total)
else:
    print("El costo a pagar es de: ", total_gastado)