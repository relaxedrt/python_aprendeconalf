#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
def booleanos(n):
    if (n == 1) or (n == 0):
        return True
    else:
        return False
def aplicadora(f, l):
    for i in l:
        print(f(i))
aplicadora(booleanos, [0,1,10,22,33,1,3,0])