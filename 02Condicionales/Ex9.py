#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
edad = int(input("Cual es tu edad?: "))
if edad <= 4:
    precio = 0
else:
    if edad > 4 and edad <=18:
        precio = 5
    else:
        if edad > 18:
            precio = 10
print(f"Por tu edad tu entrada costara {precio} euros.")