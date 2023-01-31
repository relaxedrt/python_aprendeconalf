#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
def aprobadosordenados(n):
    s = pd.Series(n)
    return (s[s > 5].sort_values(ascending = False))
aprobadosordenados(notas)