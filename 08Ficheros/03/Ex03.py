#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
num1 = int(input("Cual es el primer numero de la multiplicacion?: "))
num2 = int(input("Cual es el segundo numero de la multiplicacion?: "))
name = "tabla-" + str(num1) + ".txt"
try:
    f = open(name, "r")
    lineas = f.readlines()
    print(lineas[num2])
except FileNotFoundError:
    print(f"No hay un fichero con la tabla del {num1}")
finally:
    f.close()