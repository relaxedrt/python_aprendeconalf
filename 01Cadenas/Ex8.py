#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
precio = input("Cual es el precio del producto?: ")
preciosep = precio.split(".")
print("El producto vale " + preciosep[0] + " euros con " + preciosep[1] + " centimos")