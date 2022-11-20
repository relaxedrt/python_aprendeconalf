#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
premios = []
for i in range(6):
    premios.append(int(input("Introduce uno de los numeros ganadores?: ")))
premios.sort()
print(f"Lo  numeros ganadores son {premios}")