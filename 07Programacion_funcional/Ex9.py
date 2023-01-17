#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
import math as m
def modulo(v=(0, 0, 0)):
    mod = m.sqrt(sum(i ** 2 for i in v))
    return mod
print(modulo((3, 4)))
print(modulo((1, 2, 3)))