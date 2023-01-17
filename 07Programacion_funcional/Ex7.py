#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
def notas(n):
    nret = {}
    for i in n:
        if n[i] < 5:
            nret[i.upper()] = "DEFICIENTE"
        if (n[i] >= 5) and (n[i] < 6) :
            nret[i.upper()] = "SUFICIENTE"
        if (n[i] >= 6) and (n[i] < 7): 
            nret[i.upper()] = "BIEN"
        if (n[i] >= 7) and (n[i] < 9): 
            nret[i.upper()] = "NOTABLE"
        if n[i] >= 9: 
            nret[i.upper()] = "SOBRESALIENTE"
    return nret
print(notas({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))