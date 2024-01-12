
# Otros cursos
duracion_min = 2.5
duracion_max = 7
duracion_prom = 4

# Nuestro curso
nuestro_curso = 1.5

dif_min = 100 - nuestro_curso / duracion_min * 100
dif_max = 100 - nuestro_curso / duracion_max * 100
redondeo = round(dif_max, 2)
dif_prom = 100 - nuestro_curso / duracion_prom * 100

print(f"Dura un {dif_min}% menos que el mas rapido")
print(f"Dura un {redondeo}% menos que el mas lento")
print(f"Dura un {dif_prom}% menos que el mas promedio")

