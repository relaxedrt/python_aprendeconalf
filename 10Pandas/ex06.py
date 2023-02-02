#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd
archivo = "10Pandas/cotizacion.csv"

def resumen():
    df = pd.read_csv(archivo, sep=";", decimal=",", thousands=".", index_col=0)
    return pd.DataFrame([df.min(),df.max(), df.mean()], index=["Mínimo", "Máximo", "Media"])
print(resumen())