#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd

inicio = int(input("Introduce el ano de comienzo: "))
fin = int(input("Introduce el ano de final: "))
ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input(f"Introduce las ventas del ano {i}: "))
ventas =pd.Series(ventas)
print("Ventas\n", ventas)
print("Ventas con descuento\n", ventas * 0.9)