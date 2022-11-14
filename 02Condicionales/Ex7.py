#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
renta = int(input("Cual es tu renta anual?: "))
if renta < 10000:
    tipo = 5
else:
    if renta > 10000 and renta < 20000:
        tipo = 15
    else:
        if renta > 20000 and renta < 35000:
            tipo = 20
        else:
            if renta > 35000 and renta < 60000:
                tipo = 30
            else:
                if renta > 60000:
                    tipo = 45
print(f"Por tus ingresos tendras un tipo impositivo del {tipo}%")