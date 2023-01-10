#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
def longitudes(frase):
    l = frase.split(" ")
    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = len(i)
    return dic
print(longitudes("como quieres que te quiera si no estas aqui"))
