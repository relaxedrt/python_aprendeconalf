#https://aprendeconalf.es/docencia/python/ejercicios/funciones/

def exp(lin):
    l = []
    for i in lin:
        l.append(i**2)
    return l
def stats(l):
    dic = {}
    dic["media"] = sum(l)/len(l)
    dic["varianza"] = sum(exp(l))/len(l)-dic['media']**2
    dic["desviacion tipica"] = dic['varianza']**0.5
    return dic
print(stats([1, 2, 3, 4, 5]))
print(stats([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))