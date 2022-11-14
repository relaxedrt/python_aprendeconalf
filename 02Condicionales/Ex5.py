#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
edad = int(input("Cual es tu edad?: "))
ingresos = int(input("Cuales son tus ingresos mensuales?: "))
if (edad>=16) and (ingresos>=1000):
    print("Por tu edad y tus ingresos deberas tributar.")
else:
    print("No eres elegible para esta tribbutacion.")
