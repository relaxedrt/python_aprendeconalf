#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
lista = [1.2, 2.9, 3.7, 0.4, 5]
def media(l):
    media = sum(l)/len(l)
    return media
print("La media de tu lista es: ")    
print(media(lista))