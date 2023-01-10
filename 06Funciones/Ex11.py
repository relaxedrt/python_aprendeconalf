#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
text = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"

def freq(f):
    dic = {}
    l=f.split(" ")
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

def masusada(d):
    w = ""
    r = 0
    for word, freq in d.items():
        if freq > r:
            r = freq
            w = word
    return (w , r)
print(freq(text))
print(masusada(freq(text)))