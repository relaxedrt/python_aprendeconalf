#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd
data = {"Mes":["Enero","Febrero","Marzo","Abril"],
        "Ventas":[30500,35600,28300,33900],
        "Gastos":[22000,23400,18100,20700]}
d = pd.DataFrame(data)
print(d)