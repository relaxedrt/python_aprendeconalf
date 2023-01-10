#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
def aplicador(f, l):
    nl = []
    for i in l:
        nl.append(f(i))
    return nl
def cuadrado(n):
    return n**2
print(aplicador(cuadrado, [1, 2, 3, 4]))
