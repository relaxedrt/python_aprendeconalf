#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abcm3 = []
for i in range(len(abc)):
    if i % 3 != 0:
        abcm3.append(abc[i-1])
print(abcm3)

