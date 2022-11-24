#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
word = input("Introduce una palabra: ")
lword = list(word)
lword.reverse()
rword = list(word)
if lword == rword :
    print(f"{word} es un palindromo.")
else:
    print(f"{word} no es un palindromo.")