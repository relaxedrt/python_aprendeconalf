#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
numero_tlf  = input("Cual es el numero de telefono? ")
num_div = numero_tlf.split("-")
if len(num_div) == 2:
    print("Este e el numero de telefono que buscas.")
    print(num_div[1])
else :
    print("No has escrito un numero correcto.")
