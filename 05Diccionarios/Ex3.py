#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
frutas = {'banana':1.35,'apple':0.8,'pear':0.85,'orange':0.7}
want = input("Que fruta quieres?: ")
kg = int(input("Cuantos kilos vas a querer?: "))
if want != ("platano" or "manzana" or "pera" or "natanja"):
    print(f"Esta fruta no está disponible en nuestro catalogo.")
elif want == "platano":
    print(f"Todo serán {frutas['banana']*kg} euros")
elif want == "manzana":
    print(f"Todo serán {frutas['apple']*kg} euros")
elif want == "pera":
    print(f"Todo serán {frutas['pear']*kg} euros")
elif want == "naranja":
    print(f"Todo serán {frutas['orange']*kg} euros")