#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
vocales = ["a","e","i","o","u"]
palabra = input("En que palabra buscaremos vocales?: ")
lpalabra = list(palabra)
num = [0,0,0,0,0]
for n in range(len(lpalabra)):
    if lpalabra[n] == "a":
        num[0]= num[0]+1
    elif lpalabra[n] == "e":
        num[1]= num[1]+1
    elif lpalabra[n] == "i":
        num[2]= num[2]+1
    elif lpalabra[n] == "o":
        num[3]= num[3]+1
    elif lpalabra[n] == "u":
        num[4]= num[4]+1
for i in range(len(vocales)):
    if num[i] != 0:
        print(f"La palabra {palabra} contiene {num[i]} {vocales[i]}'s")
