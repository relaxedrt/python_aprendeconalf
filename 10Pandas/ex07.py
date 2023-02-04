#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd
file = "10Pandas/titanic.csv"
df = pd.read_csv(file, index_col=0)
def datosdf(d):
    #datos = {"NumDatos":d.size, "NombreCol":d.index, "TipoDato":d.dtype, "Primeras10":d.head(10), "Ultimmas10":d.tail(10)}
    NumDatos = d.size
    NombreCol = d.index
    TipoDato = d.dtypes
    Primeras10 = d.head(10)
    Ultimas10 = d.tail(10)
    return (f"Numero de datos:\n{NumDatos}\nNombre de las columnas\n{NombreCol}\nTipo de dato:\n{TipoDato}\nPrimeras 10  filas:\n{Primeras10}\nUltimas 10 filas:\n{Ultimas10}")
def pasajeron(d, n):
    return d.iloc[n]
def filaspares(d):
    return df.info()
print(filaspares(df))