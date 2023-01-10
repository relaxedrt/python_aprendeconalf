#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
def notas(l):
    n = []
    for i in l:
        if i < 5:
            n.append("DEFICIENTE")
        if (i >= 5) and (i < 6) :
            n.append("SUFICIENTE")
        if (i >= 6) and (i < 7): 
            n.append("BIEN")
        if (i >= 7) and (i < 9): 
            n.append("NOTABLE")
        if i >= 9: 
            n.append("SOBRESALIENTE")
    return n
print(notas([1,2,3,4,5,6,7,8,9,10]))