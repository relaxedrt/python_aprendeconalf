#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
file = "listin.txt"
def checkexist():
    try:
        f = open(file, "r")
        f.close()
    except FileNotFoundError:
        f = open(file,"a")
        f.write("LISTIN TELEFONICO \n")
def consult(nombre):
    f = open(file, "r")
    lineas = f.readlines()
    for l in lineas:
        if str(nombre) in l:
            return l
def newnum(nombre, numero):
    checkexist()
    f = open(file, "a")
    f.write(f"{nombre},{numero}\n")
    f.close()
def deletenum(nombre):
    f = open(file, "r")
    lineas = f.readlines()
    f.close()
    for l in lineas:
        if str(nombre) in l:
            lineas.remove(l)
    a = open(file, "w")
    for i in lineas:
        a.write(i)
deletenum("Casa")