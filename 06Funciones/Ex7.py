#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [2.3, 3.5, 7.8, 6.9, 9.9, 1.1]
def exp(lin):
    l = []
    for i in lin:
        l.append(i**2)
    return l
print(exp(l1))
print(exp(l2))