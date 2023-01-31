#https://aprendeconalf.es/docencia/python/ejercicios/pandas/
import pandas as pd
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
def serienotas(n):
    s = pd.Series(n)
    print(f"La nota mas baja es {s.min()}")
    print(f"La nota mas alta es {s.max()}")
    print(f"La nota mas media es {s.mean()}")
    print(f"La nota mas baja es {s.std()}")
serienotas(notas)