#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
money = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
div = input("De que divisa quieres conocer el simbolo?: ")
if div != ("Euro" or "Dollar" or "Yen"):
    print(f" La divisa {div} no está en nuestro diccionario")
elif div == "Euro":
    print(money["Euro"])
elif div == "Dollar":
    print(money["Dollar"])
elif div == "Yen":
    print(money["Yen"])