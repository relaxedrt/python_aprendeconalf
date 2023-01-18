#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
name = "tabla-n.txt"
def tablamult(n):
    archivo = open(name,"a")
    archivo.write(f"------------------------\n")
    for i in range(0, 11):
        res = n * i
        archivo.write(f"{n} x {i} = {res} \n")
tablamult(int(input("Que numero quieres conocer su tabla de multiplicar?: ")))    