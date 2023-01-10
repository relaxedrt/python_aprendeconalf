#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
from math import sin, cos, tan, exp, log
def aplicacion(f, n):
    funcions = {"seno":sin, "coseno":cos, "tangente":tan, "exp":exp, "log":log}
    result = {}
    for i in range(1, n+1):
        result[i] = funcions[f](i)
    return result
def calculator():
    f = input("Introduce la aplicacion que deseas aplicar (seno, coseno, tangente, exp, log): ")
    n = int(input("Introduce un numero positivo: "))
    for i, j in aplicacion(f, n).items():
        print(i, "\t", j)
calculator()