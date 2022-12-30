#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
diccionario = {}
userin = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas: ")
for i in userin.split(","):
    clave, valor = i.split(":")
    diccionario[clave] = valor
frase = input("Que frase quieres traducir?: ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end = " ")
    else:
        print(i, end = " ")
