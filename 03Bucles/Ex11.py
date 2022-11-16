#https://aprendeconalf.es/docencia/python/ejercicios/bucles/
word = input("Que palabra separaremos?: ")
lword = list(word)
for i in range((len(lword)),0,-1):
    print(lword[i-1])