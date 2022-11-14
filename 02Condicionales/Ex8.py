#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
puntuacion = float(input("Cual es tu puntuacion en la empresa?: "))
if puntuacion < 0.4:
    punreal = 0.0
else:
    if puntuacion >=0.4 and puntuacion <0.6:
        punreal = 0.4
    else:
        if puntuacion >= 0.6:
            punreal = 0.6
print(f"Por el nivel en el que estas cobraras {punreal*2400} euros.")