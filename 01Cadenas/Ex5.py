#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
frase = input("Cuentame algo: ")
lista = frase.split(" ")
inv_palabras = list(reversed(lista))
inv_letras = frase[::-1]
print("Aqui lo tienes invertido palabra por palabra:")
print(" ".join(inv_palabras))
print("Y aqui letra por letra:")
print(inv_letras)