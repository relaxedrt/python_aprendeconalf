#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
#??Falta terminar porque ahora mismo no esta funcionando
lista = input("Dame una lista de numeros separados por comas: ")
total = 0
def media(l):
    for i in l:
        total = total + i
    media = total / len(l)
    return media
print("La media de tu lista es: ")    
print(media(lista.split(",")))