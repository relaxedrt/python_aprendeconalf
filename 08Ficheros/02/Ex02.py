#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
num = input("Que numero buscas?: ")
name = "tabla-" + str(num) + ".txt"
try:
    f = open(name, "r")
except FileNotFoundError:
    print(f"No hay un fichero con la tabla del {num}")
else:
    print(f.read())
    f.close()
