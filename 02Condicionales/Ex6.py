#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
nombre = input("Cual es tu nombre?: ")
sexo = input("Cual es tu sexo M/F?: ")
if sexo == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        group = "B"
print(f"Perteneces al grupo {group}")