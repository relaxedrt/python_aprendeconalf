#https://aprendeconalf.es/docencia/python/ejercicios/bucles/
frase = input("Dame una frase y buscare una letra en ella: ")
lfrase  = list(frase)
letra = input("Que letra buscaremos?: ")
num = 0
for i in range((len(lfrase)),0,-1):
    if lfrase[i-1]==letra:
        num= num + 1
print(f"En la frase ha habido {num} veces la letra {letra}.")
