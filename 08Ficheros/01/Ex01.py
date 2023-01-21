#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
num =input("Que numero quieres conocer su tabla de multiplicar?: ")
name = "tabla-" + str(num) + ".txt"
def tablamult(n):
    archivo = open(name,"a")
    for i in range(0, 11):
        res = n * i
        archivo.write(f"{n} x {i} = {res} \n")
tablamult(int(num))    