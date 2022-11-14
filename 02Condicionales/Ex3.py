#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
num1 = int(input("Introduce el primer numero de la operacion: "))
num2 = int(input("Introduce el segundo numero de la operacion: "))
if num2 == 0:
    print("El divisor no puede ser igual a 0.")
else:
    print(str(num1/num2))