#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
userin = int(input("Que numero quieres convertir en factorial: "))
def nums(num):
    resp = 1
    for i in range(1,num):
        resp *= i+1
    print(resp)
    return resp
    
nums(userin)