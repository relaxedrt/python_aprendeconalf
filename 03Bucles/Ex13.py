#https://aprendeconalf.es/docencia/python/ejercicios/bucles/
text = input("Soy un loro: ")
i = 1
while i == 1:
    if text=="salir":
        i = 0
    else:
        print(text)
        text=input("Que?: ")