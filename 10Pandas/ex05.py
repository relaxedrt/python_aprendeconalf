#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd
data = {"Mes":["Enero","Febrero","Marzo","Abril"],
        "Ventas":[30500,35600,28300,33900],
        "Gastos":[22000,23400,18100,20700]}
df = pd.DataFrame(data)

def balance(d,m):
    d["Balance"] = d.Ventas - d.Gastos
    return d[d.Mes.isin(m)].Balance.sum()

print(balance(df, ['Enero','Marzo']))