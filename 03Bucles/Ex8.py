#https://aprendeconalf.es/docencia/python/ejercicios/bucles/
num = int(input("Cual quieres que sea la altura del triangulo?: "))
for i in range(1, num + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")